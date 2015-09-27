int time = 3877;
float ax = -0.55, ay = 0.08, az = 10.24;
float mx = -9.73, my = 3.55, mz = -86.02;
float gx = 0.04,  gy = 0.20, gz = 0.03;
float press = 1010.51;
float temp = 27.80;
//アスキーデータのバイト数
//time,ax,ay,az,mx,my,mz,gx,gy,gz,press,temp
//2, 3,3,3, 3,3,3, 3,3,3, 3,3

int nums[3]; //1つ目が正負のフラグ0なら正，1なら負，2つ目が整数値，3つ目が少数値

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
    float temp2 = ((float)num - temp)*100;   //小数部分の取得numのキャストでエラーでそう
                                             //*100で小数点以下2桁を取り出す
    dcml = abs((int)temp2);  //小数点以下切り捨て
    String sDcml = String(dcml, HEX);
    //dcmlが2バイトになるように調整
    if(sDcml.length() < 2){
        sDcml = "0" + sDcml;
    }
    sDcml.toUpperCase();

    /* Serial.print("temp2:"); */
    /* Serial.println(temp2); */
    /* Serial.print("dcml:"); */
    /* Serial.println(dcml); */

    //Twe-Liteのアスキーモードの都合上UpperCaseで返す
    return sSign + "  " + sIntg + "  " + sDcml;
}

void setup(){
    Serial.begin(9600);
    Serial.print("time:");
    Serial.println(time);
    Serial.println(getHexString((float)time));
    Serial.print("ax:");
    Serial.println(ax);
    Serial.println(getHexString(ax));
    Serial.print("ay:");
    Serial.println(ay);
    Serial.println(getHexString(ay));
    Serial.print("az:");
    Serial.println(az);
    Serial.println(getHexString(az));
}


void loop(){
}
