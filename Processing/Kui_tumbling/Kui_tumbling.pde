//まずｃｓｖの読み込み
//そのデータを元に３Dモデルの描画
//フレームレートを変えられると良い

//Table table;
//void setup() {
//  table = loadTable("csv/logger1-acc-mag.csv");//acc-x,y,z mag-x,y,z
//  println(table.getColumnCount() + " total columns in table"); 
//
//  for (TableRow row : table.rows ()) {
////    for (int i=0; i<table.getColumnCount(); i++) {
////      println(row.getString(i));
////    }
//    println("accX:" + row.getFloat(0) + " accY:" + row.getFloat(1) + " accZ:" + row.getFloat(2));
//  }
//}

//void loop(){
//  
//}
/////////////////////////////
import saito.objloader.*;
OBJModel model;
//float rotX=0, rotY=0;
Table table;

int frame;
int maxFrame;

Orientation ori = new Orientation();
DegQueue queX = new DegQueue();
DegQueue queY = new DegQueue();
DegQueue queZ = new DegQueue();

// 初期設定
void setup() {  
  table = loadTable("csv/logger1-acc-mag.csv");//acc-x,y,z mag-x,y,z

  frame = 0;
  maxFrame = table.getRowCount();

  // 画面サイズ
  size(400, 300, P3D);
  // フレームレート
  frameRate(60);
  // OBJファイルの読み込み
  model = new OBJModel(this, "elzup.obj");
  model.enableDebug();
  // 座標保存
  model.scale(3);
  model.translateToCenter();  // 中央に配置
  stroke(255);
  noStroke();
}

void draw() {
  if (frame < maxFrame) {

    setDataFromTable(frame);
    println("frame:" + frame + "roll:" + ori.getRoll() + " pitch:"+ ori.getPitch() + " heading:" + ori.getHeading());
    // 座標保存
    background(255);
    // 照明追加
    lights();
    // 座標保存
    pushMatrix();
    // オブジェクトの移動
    translate(width/2, height/2, 0);
    // オブジェクトの回転(引数はラジアン)
    rotateX(queX.average());
    rotateY(queY.average());
    rotateZ(queZ.average());
    // モデルの描画
    model.draw();
    // 座標保存
    popMatrix();
    // 回転角の増加
//    rotX = rotX + 0.01;
//    rotY = rotY + 0.01;
//    // 回転角が360[deg](=6.28[rad])以上なら0に戻す
//    if (rotX >= 6.28) rotX = 0;
//    if (rotY >= 6.28) rotY = 0;
  }

  frame++;
}

void setDataFromTable(int frame) {
  ori.setAccX(table.getRow(frame).getFloat(0));
  ori.setAccY(table.getRow(frame).getFloat(1));
  ori.setAccZ(table.getRow(frame).getFloat(2));

  ori.setMagX(table.getRow(frame).getFloat(3));
  ori.setMagY(table.getRow(frame).getFloat(4));
  ori.setMagZ(table.getRow(frame).getFloat(5));
  
  queX.add(ori.getRoll());
  queX.remove();
  queY.add(ori.getPitch());
  queY.remove();
  queZ.add(ori.getHeading());
  queZ.remove();
}
