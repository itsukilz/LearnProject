public class Test {
public static String deFront(String str) {    
  int l = str.length();
  if(l==0) return "";
  else if(l==1) {
    if(str.equals("a")) return "a";
    else return "";
  }
  else{
    String f = (str.substring(0,1).equals("a")) ? "a":"";
    String s = (str.substring(1,2).equals("b")) ? "b":"";
    String last = (l>2) ? str.substring(2) : "";
    return f+s+last;
  }
}



	public static void main(String[] args) {
		// int[] k = new int[]{6, 7, 2, 6,6,7,9};
		System.out.println(deFront("blueasdfa"));
		System.out.println(deFront("abad"));
		System.out.println(deFront("a"));
		System.out.println(deFront(""));


	}
}