#include <M5Core2.h>
#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

String filename;
char filename_array[20];
char key;

    
void setup() {
  M5.begin();
  SerialBT.begin("M5Stack");
}
 
void loop() {

  if ( SerialBT.available() ) {       
    key = SerialBT.read();  

    if (key == 0x6e) {//"n"のASCIIコード
      filename="/jyanken.jpg";}
    else if (key == 0x67) {//"g"のASCIIコード
      filename="/pa.jpg";}
    else if (key == 0x63) { //"c"のASCIIコード
      filename="/gu.jpg";}
    else if (key == 0x70) {//"p"のASCIIコード
      filename="/ch.jpg";}
  }

  filename.toCharArray(filename_array, 20);

  M5.Lcd.drawJpgFile(SD, filename_array,0,0);
  M5.update();
  
}
