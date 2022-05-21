# jyankenAI
 

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
Tensorflow Liteの浮動小数点形式でモデルを出力しました。  

## ラズパイ設定  
・ラズパイ4B 8GB  
・32GB SDカード  
・OS  
![image](https://user-images.githubusercontent.com/67863963/169652507-1f116953-8e8b-41c3-b645-a5a522155df2.png)
