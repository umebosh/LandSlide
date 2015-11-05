import java.util.LinkedList;

class DegQueue{  //n個分の角度を保存しておきその平均値を返す
  int Quesize = 10;
  LinkedList<Float> llist = new LinkedList<Float>();
  
  void add(float f){
    if(llist.size()<Quesize){
      llist.add(f);
    }
  }
  
  void remove(){
    if(llist.size()==Quesize){
      llist.poll();
    }
  }
  
  float average(){
    float size = llist.size();
    float sum = 0;
    for(float f: llist){
      sum += f;
    }
    
    if(llist.size()>0){
      return sum/size;
    }
    
    return 0;
  }
  
}
