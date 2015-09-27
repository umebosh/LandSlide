//10DoFからとった本番用のデータをUSBシリアル軽油で流すだけ

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_LSM303_U.h>
#include <Adafruit_BMP085_U.h>
#include <Adafruit_L3GD20_U.h>
#include <Adafruit_10DOF.h>

/* Assign a unique ID to the sensors */
Adafruit_LSM303_Accel_Unified accel = Adafruit_LSM303_Accel_Unified(30301);
Adafruit_LSM303_Mag_Unified   mag   = Adafruit_LSM303_Mag_Unified(30302);
Adafruit_BMP085_Unified       bmp   = Adafruit_BMP085_Unified(18001);
Adafruit_L3GD20_Unified       gyro  = Adafruit_L3GD20_Unified(20);

/* プロトタイプ宣言 */
String getHexString(float);

int times = 0; //経過時間を記録

void setup(){
  Serial.begin(115200);

  Serial.print("Initializing sensors...");
    /* Initialise the sensors */
  if(!accel.begin())
  {
    /* There was a problem detecting the ADXL345 ... check your connections */
    Serial.println(F("Ooops, no LSM303 detected ... Check your wiring!"));
    while(1);
  }
  if(!mag.begin())
  {
    /* There was a problem detecting the LSM303 ... check your connections */
    Serial.println("Ooops, no LSM303 detected ... Check your wiring!");
    while(1);
  }
  if(!bmp.begin())
  {
    /* There was a problem detecting the BMP085 ... check your connections */
    Serial.print("Ooops, no BMP085 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  if(!gyro.begin())
  {
    /* There was a problem detecting the L3GD20 ... check your connections */
    Serial.print("Ooops, no L3GD20 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  Serial.println("sensors initialized.");
  Serial.println("");

  Serial.println("times,ax,ay,az,mx,my,mz,gx,gy,gz,press,temp");    //書き込みデータ一覧


}

void loop(){
  String data = "";      //データ保存用の変数
  String asii = ":00A012FF ";    //書式モードのアスキーモードで親に送るコマンド

  //経過時間を記録
  sensors_event_t event;
  data += times;
  data += ",";
  asii += getHexString((float)times);
  asii += ",";

  //加速度を記録
  accel.getEvent(&event);
  data += event.acceleration.x;
  asii += getHexString((float)event.acceleration.x);
  asii += ",";
  data += ",";
  data += event.acceleration.y;
  asii += getHexString((float)event.acceleration.y);
  asii += ",";
  data += ",";
  data += event.acceleration.z;
  asii += getHexString((float)event.acceleration.z);
  asii += ",";
  data += ",";

  //地磁気を記録
  mag.getEvent(&event);
  data += event.magnetic.x;
  asii += getHexString((float)event.magnetic.x);
  asii += ",";
  data += ",";
  data += event.magnetic.y;
  asii += getHexString((float)event.magnetic.y);
  asii += ",";
  data += ",";
  data += event.magnetic.z;
  asii += getHexString((float)event.magnetic.z);
  asii += ",";
  data += ",";

  //ジャイロを記録
  gyro.getEvent(&event);
  data += event.gyro.x;
  asii += getHexString((float)event.gyro.x);
  asii += ",";
  data += ",";
  data += event.gyro.y;
  asii += getHexString((float)event.gyro.y);
  asii += ",";
  data += ",";
  data += event.gyro.z;
  asii += getHexString((float)event.gyro.z);
  asii += ",";
  data += ",";

  //気圧と気温を記録
  bmp.getEvent(&event);
  if (event.pressure)
  {
    data += event.pressure;
    asii += getHexString((float)event.pressure);
    asii += ",";
    data += ",";

    float temperature;
    bmp.getTemperature(&temperature);
    data += temperature;
    asii += getHexString((float)event.temperature);
    asii += "X";
  }


  Serial.println(data);
  Serial.println(asii);

  delay(1000);
  times += 1;
}

String  getHexString(float num){
    int sign, intg, dcml;

    //正負の判定
    if(num < 0){
            sign = 1;
        }else{
                sign = 0;
            }
    String sSign = String(sign, HEX);
    sSign.toUpperCase();

    //整数部分の判定
    int temp = abs(num);   //絶対値を取得
    intg = (int)temp;   //intにして小数点以下切り捨て
    String sIntg = String(intg, HEX);
    //sIntgを24bitにする
    int len = sIntg.length();
    if(len > 3){    //24bitから溢れたらその部分を切り捨て
            sIntg = sIntg.substring(len-3, len);
        }
    if(len == 2){
            sIntg = "0" + sIntg;
        }
    if(len == 1){
            sIntg = "00" + sIntg;
        }
    sIntg.toUpperCase();

    //小数部分の判定
    float temp2 = (abs(num) - temp)*100;   //小数部分の取得numのキャストでエラーでそう
                                             //*100で小数点以下2桁を取り出す
    dcml = abs((int)temp2);  //小数点以下切り捨て
    String sDcml = String(dcml, HEX);
    //dcmlが2バイトになるように調整
    if(sDcml.length() < 2){
            sDcml = "0" + sDcml;
        }
    sDcml.toUpperCase();

    //Twe-Liteのアスキーモードの都合上UpperCaseで返す
    return sSign + "" + sIntg + "" + sDcml;
}
