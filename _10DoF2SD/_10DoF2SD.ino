#include <SD.h>

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

const int chipSelect = 10;
int times = 0; //経過時間を記録

void setup(){
  Serial.begin(115200);
  Serial.print("Initializing SD card...");
  pinMode(10,OUTPUT);
  if(!SD.begin(chipSelect)){
      Serial.println("Card failed, or not present");
      return;
  }
  Serial.println("card initialized.");
  
  Serial.println("");

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
  
  //経過時間を記録
  sensors_event_t event;
  data += times;
  data += ",";
  
  //加速度を記録
  accel.getEvent(&event);
  data += event.acceleration.x;
  data += ",";
  data += event.acceleration.y;
  data += ",";
  data += event.acceleration.z;
  data += ",";
  
  //地磁気を記録
  mag.getEvent(&event);
  data += event.magnetic.x;
  data += ",";
  data += event.magnetic.y;
  data += ",";
  data += event.magnetic.z;
  data += ",";
  
  //ジャイロを記録
  gyro.getEvent(&event);
  data += event.gyro.x;
  data += ",";
  data += event.gyro.y;
  data += ",";
  data += event.gyro.z;
  data += ",";
  
  //気圧と気温を記録
  bmp.getEvent(&event);
  if (event.pressure)
  {
    data += event.pressure;
    data += ",";
    
    float temperature;
    bmp.getTemperature(&temperature);   
    data += temperature;
  }
  

  
  
  //SDカードへの書き込み処理
  File logData = SD.open("logData.csv", FILE_WRITE);
  
  //ファイルが存在すれば書き込み
  if(logData){
    logData.println(data);
    Serial.println(data);
    logData.close ();
  }
  else{
        Serial.println("error opening logData.csv");
  }
  
  delay(1000);
  times += 1;
}
