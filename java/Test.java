public class Test{
public static boolean array220(int[] nums, int index) {
  if(index < nums.length){
    if(arrayfind(nums, nums[index])) return true;
    else return array220(nums, index+1);
  }
  else return false;
}


public static boolean arrayfind(int[] nums, int find){
  System.out.println(find);
  for(int i : nums){
    if(i==find*10)
      return true;
  }
  return false;
}


    
public static void main(String[] args){
	int[] a = new int[]{20,2,21};
  System.out.println(array220(a,0));
}
}
