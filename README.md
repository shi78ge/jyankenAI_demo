# jyankenAI_demo
 

https://user-images.githubusercontent.com/67863963/169651920-9f1daf9c-0622-4407-a4d2-7b82cf599de8.mp4


[Teachable Machine](https://teachablemachine.withgoogle.com/)で作成したじゃんけんAIをラズパイで動作させるデモです。  
認識結果をもとに、M5Stack Core2で勝つ手を表示させています。  
  
## Teachable Machine  
非常に簡単に機械学習モデルが作れてしまうサービスです。  
tflite形式で出力もできるので、ラズパイへの実装にももってこいです。  
使い方は、Googleによってまとめられた資料があるのでこちらを参照ください。  
https://services.google.com/fh/files/misc/ai_programming_booklet.pdf  
これを使って、WEBカメラで撮影した手の画像から、グー/チョキ/パーを判定する分類モデルを作成します。  
  
![image](https://user-images.githubusercontent.com/67863963/169652078-1d8eb358-41f1-4bc6-a7ae-49cda8e1e76f.png)  
標準の画像モデルを選択しました。  
  
![image](https://user-images.githubusercontent.com/67863963/169652211-a45d1b4d-a3bd-4193-9598-94a839afa70f.png)  
こんな感じです。  
何も映っていない背景画像も撮るのがポイントです。    
![image](https://user-images.githubusercontent.com/67863963/169652332-4c7f8e27-16f0-40e5-8151-878db505025f.png)  
TensorFlowLiteの浮動小数点形式でモデルを出力しました。  
※私が作成したじゃんけん判定モデルを公開していますが、汎化性能は非常に低いと思うので、自分の手でモデル作成するのがよいと思います。  

## ラズパイ設定  
・ラズパイ4B 8GB  
・32GB SDカード  
・OS  
![image](https://user-images.githubusercontent.com/67863963/169652507-1f116953-8e8b-41c3-b645-a5a522155df2.png)  
ラズパイにはopenCV, numpy, TensorFlowLiteの導入が必要です。  
[karaage](https://github.com/karaage0703)さんのこちらの記事を参考にお願いします。  
https://zenn.dev/karaage0703/articles/3d3d443244da2c  
ただしこちらの記事は64bit版OSなので、32bit版では一部異なります。以下のようにコマンドを変更して下さい。  
```
wget "https://raw.githubusercontent.com/PINTO0309/TensorflowLite-bin/main/2.8.0/download_tflite_runtime-2.8.0-cp39-none-linux_aarch64.whl.sh"　
　↓
wget "https://raw.githubusercontent.com/PINTO0309/TensorflowLite-bin/main/2.8.0/download_tflite_runtime-2.8.0-cp39-none-linux_armv7l.whl.sh"
```
それ以降のコマンドも、aarch64の部分をarmv7lに変更して下さい。
あと、他のパッケージをpipでインストールする際、「ハッシュが一致しない」みたいなエラーが出ることがありました。  
この場合、pipインストール時に表示されるURLをコピーして、  
wget "URL" として.whlをダウンロードし、そのあと`sudo pip3 install ** .whl` みたいにすればうまくいきました。  
  
tfliteモデル実行環境としては以上ですが、今回Bluetoohシリアルで推論結果をM5Core2に飛ばすようにしたので、Bluetoohの設定が必要になります。  
こちらの記事を参考にお願いします。  
https://ossyaritoori.hatenablog.com/entry/2019/01/11/M5stack%E3%81%A8Raspberry_Pi_zero%E3%81%AEBluetooth_%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB%E9%80%9A%E4%BF%A1  
ただし先にM5側にBluetoothシリアルを有効にするプログラムを書き込んでおく必要があります。  
  
## M5Core2設定
M5の設定は特に難しいことはないのですが、推論結果に応じて表示させる画像ファイルをSDカードに保存しておく必要があります。  
SDフォルダの以下のファイルをコピーしてください。  
![image](https://user-images.githubusercontent.com/67863963/169654122-942207c2-4d36-42a1-ac0f-640259d48f8f.png)  
340 * 240 ピクセルのサイズになっています。  
ちなみにjpgとpng両方試しましたが、jpgのほうが表示が速かったです。  
グー/チョキ/パーの画像素材はこちらから頂きました。  
http://lmsnn.fc2web.com/material/janken.html  
  
## 全体構成
全体的な構成は以下のようになります。  
PCからVNC接続でラズパイを遠隔操作しています。正直ラズパイ使う必要なかったですが、ラズパイの環境は気軽にリセットできる点がメリットかと思います。  
![image](https://user-images.githubusercontent.com/67863963/169654474-b21f7f76-b15d-4626-8850-9c41ed825626.png)
