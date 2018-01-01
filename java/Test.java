public class Test{
public static boolean sameStarChar(String str) {
  int start = 0;
  int found;
  while(true){
    found = str.indexOf("*",start);
    if(ifsame(str,found,start)!=0)
    	return false;
   	else{
   		if(found+1>str.length()-1) break;
   		else start = found+1;
   	}
  
  }
  return true;
}
    

public static int ifsame(String str, int found, int start){
	int flag = 0;
	if(found == -1){
		if(start==0) flag = 0;
		else  flag = 0;
	}
	else{
		if(found-1<0 || found+1>str.length()-1) flag=0;
		else{
			if(str.charAt(found-1) != str.charAt(found+1)) flag = 1;
			else flag = 0;
		}
	}
	return flag;
}

    public static void main(String[] args){
        System.out.println(sameStarChar("12*2*3*"));
        }
    }
