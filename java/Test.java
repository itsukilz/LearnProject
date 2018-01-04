public class Test{
public static String notReplace(String str) {
  int start = 0;
  int found;
  String r = "";
  while(start<str.length()){
    found = str.indexOf("is",start);
    if(found!=-1){
      if(check(str,found))
        r = r+str.substring(start,found)+"is not";
      else
        r =  r+str.substring(start,found+2);
      start = found+2;

    }
    else{
      r = r+str.substring(start);
      break;
    }
  }
  return r;
}

public static boolean check(String str, int found){
  boolean left, right;
  if(found==0 || (found>=1 && !Character.isLetter(str.charAt(found-1))))
    left = true;
  else
    left = false;
    
  if(found+1==str.length()-1 || (found+1<=str.length()-1 && !Character.isLetter(str.charAt(found+2))))
    right = true;
  else
    right = false;
  return right&&left;
}
    
public static void main(String[] args){
      System.out.println(notReplace("Dis is bliss is"));
        }
    }
