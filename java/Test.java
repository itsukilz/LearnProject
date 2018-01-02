public class Test{
public static int countYZ(String str) {
  int count = 0;
  for(int i = 0; i<str.length(); i++){
    if(ifyz(str.charAt(i))){
      if(i==str.length()-1)
        count++;
      else{
        if(i>=1 && !Character.isLetter(str.charAt(i-1)))
        count++;
      }
    }
  }
  return count;
}

public static boolean ifyz(char x){
  if( x== 'y' ||x== 'z' || x == 'Y' ||x == 'Z')
    return true;
  else 
    return false;
}
    
    public static void main(String[] args){
        System.out.println(countYZ(""));
        }
    }
