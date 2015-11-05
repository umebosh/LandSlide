class Orientation{
  float[] mag = new float[3];
  float[] acc = new float[3];

  void setMagX(float x){
    mag[0] = x;
  }

  void setMagY(float y){
    mag[1] = y;
  }


  void setMagZ(float z){
    mag[2] = z;
  }


  void setAccX(float x){
    acc[0] = x;
  }

  void setAccY(float y){
    acc[1] = y;
  }


  void setAccZ(float z){
    acc[2] = z;
  }

  float getRoll(){
    return atan2(acc[1],acc[2]);
  }

  float getPitch(){
    if(acc[1]*sin(getRoll()) + acc[2]*cos(getRoll()) == 0){
      return acc[0] == 0 ? (PI/2) : (-PI/2);
    }
    else{
        return atan(-acc[0] /
            (acc[1] * sin(getRoll()) + acc[2] * cos(getRoll())));
    }
  }

  float getHeading(){
    return atan2(mag[2] * sin(getRoll()) - mag[1] * cos(getRoll()),
        mag[0] * cos(getPitch()) +
        mag[1] * sin(getPitch()) *  sin(getRoll()) +
        mag[2] * sin(getPitch()) * cos(getRoll()));
  }
}
