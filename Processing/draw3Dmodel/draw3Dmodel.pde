import saito.objloader.*;
OBJModel model;
float rotX=0, rotY=0;

import processing.serial.*;
Serial myPort;

DegQueue queX = new DegQueue();
DegQueue queY = new DegQueue();
DegQueue queZ = new DegQueue();


float[] rph = {0.0, 0.0, 0.0};

void setup(){
 
  size(400, 300, P3D);
  frameRate(30);
  model = new OBJModel(this, "elzup.obj", "absolute", TRIANGLES);
  model.enableDebug();
 
  model.scale(3);
  model.translateToCenter();
  stroke(0);
  noStroke();
 
  printArray(Serial.list());
  myPort = new Serial(this, Serial.list()[5], 115200);
  
}

void draw(){
  
  serialRcv();
  
  background(0,255,0);
  lights();
  directionalLight(200, 200, 200, -1, 1, -1);
  ambientLight(200, 200, 200);
  pushMatrix();
  translate(width/2, height/2, 0);
//  rotateY(rotY);
  rotateX(radians(queX.average()));
  rotateY(radians(queZ.average()));
//  rotateZ(radians(queY.average()));

  model.draw();
  popMatrix();
  if(rotX >= radians(360)) rotX = 0;
  if(rotY >= radians(360)) rotY = 0;
 
} //<>//

void serialRcv(){
    while (myPort.available() > 0) {
    String inBuffer = myPort.readString();
    if (inBuffer != null) {
      println(inBuffer);
      String[] splitStr = split(inBuffer,",");
      if(splitStr.length!=4){
        continue;
      }
      if(splitStr[3].indexOf("e") != -1
         && splitStr[0].length() > 0 && splitStr[1].length() > 0 && splitStr[2].length() > 0){
        rph[0] = Float.valueOf(splitStr[0]);
        rph[1] = Float.valueOf(splitStr[1]);
        rph[2] = Float.valueOf(splitStr[2]);
        
        queX.remove();
        queX.add(rph[0]);
        queY.remove();
        queY.add(rph[1]);
        queZ.remove();
        queZ.add(rph[2]);
      }
    }
  }
}

void keyPressed(){
  if(key == CODED){
    if(keyCode == UP){
      rotX += 0.1;
    }
        if(keyCode == DOWN){
      rotX -= 0.1;
    }
        if(keyCode == LEFT){
      rotY += 0.1;
    }
        if(keyCode == RIGHT){
      rotY -= 0.1;
    }
  }
}
