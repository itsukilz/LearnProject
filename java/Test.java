public class Test{
public static int count8(int n) {
  System.out.println(n);
  int flag;
  if(n<10) {
    if(n==8) return 1;
    else return 0;
  }
  else if(n>9 && n<100){
    if(n%10==8){
      if(n/10==8) flag=2;
      else flag= 1;
    }
    else flag= 0;
    return flag+count8((n/10));
  }
  else return count8(n%100)+count8(n/10);
  
}


    
public static void main(String[] args){
      System.out.println(count8(8088));
        
    }
  }
