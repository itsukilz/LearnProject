// Leetcode 682
// tag: Stack, easy
public class BaseBallGame{
	public static void main(String[] args) {
		String[] ops = new String[]{"5","2","C","D","+"};
		newStack s = new newStack();

		for (String i:ops){
			
			if(i.equals("C")){
				s.pop();
			}
			else if(i.equals("D")){

				s.push(2*s.peek_first());
				
			}
			else if(i.equals("+")){
				
				s.push(s.peek_first()+s.peek_second());
				
			}
			else{
				s.push(Integer.parseInt(i));
			}
			System.out.println(i+" "+s.show());
		}
		
	}
}