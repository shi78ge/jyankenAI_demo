import numpy as np
from tflite_runtime.interpreter import Interpreter
import time
import cv2
import serial

ser = serial.Serial('/dev/rfcomm1') #通信に使うシリアルポート指定
camera = cv2.VideoCapture(0)  # カメラCh.(ここでは0)を指定

# TFLiteモデルの読み込み
interpreter = Interpreter(model_path="jyanken_model_unquant.tflite")
# メモリ確保
interpreter.allocate_tensors()

# 学習モデルの入力層・出力層のプロパティをGet.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

start_time = time.time()


# 画像推論関数
def detect(image):
    frame = cv2.resize(image, (224, 224)) #Teachable Machineモデルの入力サイズに合わせる
    frame = frame / 255  # 0.0~1.0に正規化

    frame = np.expand_dims(frame, 0) # モデルの入力次元に合わせる

    # float32形式にキャストする
    frame = frame.astype(np.float32)

    # indexにテンソルデータのポインタをセット
    interpreter.set_tensor(input_details[0]['index'], frame)
    interpreter.invoke()  # 推論実行

    # get results
    label = interpreter.get_tensor(output_details[0]['index'])
    return label


# 画像にFPS、推論結果重畳表示関数
def draw_debug(image, elapsed_time, label2, accuracy):
    # Inference elapsed time
    cv2.putText(image,
                "Elapsed Time : " + '{:.1f}'.format(elapsed_time * 1000) + "ms" + " / " + '{:.2f}'.format(
                    1 / elapsed_time) + "fps",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,
                cv2.LINE_AA)

    # 推論結果ラベル表示
    cv2.putText(image,
                "Label : " + label2 + " accuracy :" + str(accuracy),
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,
                cv2.LINE_AA)

    # FPSとラベルをターミナルにも表示
    print("FPS:" + str(1 / elapsed_time))
    print("Label:" + label2 + " accuracy:" + str(accuracy))

    return image


if __name__ == '__main__':

    while True:

        ret, frame = camera.read()  # フレームを取得
        frame = frame[:, 420:1500]  # 正方形にトリミング。
        height = frame.shape[0]
        width = frame.shape[1]
        # WEBカメラ画像が大きいと表示に時間がかかるので適当に縮小
        frame = cv2.resize(frame, (int(width * 0.4), int(height * 0.4)))

        num = detect(frame)  # 推論結果の保存

        #推論結果ラベルに応じて文字列格納
        if np.argmax(num) == 0:
            label2 = "n"
        elif np.argmax(num) == 1:
            label2 = "g"
        elif np.argmax(num) == 2:
            label2 = "c"
        elif np.argmax(num) == 3:
            label2 = "p"

        accuracy = np.amax(num)

        elapsed_time = time.time() - start_time
        start_time = time.time()

        # 推論時間を重畳表示
        debug_image = draw_debug(
            frame,
            elapsed_time,
            label2,
            accuracy
        )

        #キャプチャ画像表示
        cv2.imshow('camera', debug_image)

        #シリアル通信で推論結果を送信
        ser.write(str.encode(label2))

        # キー操作があればwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 撮影用オブジェクトとウィンドウの解放
    camera.release()
    cv2.destroyAllWindows()

