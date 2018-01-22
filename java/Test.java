public class Test{
public static boolean groupSumClump(int start, int[] nums, int target) {
  int count = 1;
  if(start >= nums.length)
    return target==0;
  else{
    if(start< nums.length-1 && nums[start] == nums[start+1]){
      for(int i=start; i<nums.length-1; i++){
        if(nums[i]==nums[i+1])
          count++;
        else
          break;
      }
      System.out.println(count);
      if(groupSumClump(start+count,nums,target-nums[start]*count)) return true;
      return false;
    }
    else{
      if(groupSumClump(start+1,nums,target-nums[start])) return true;
      if(groupSumClump(start+1,nums,target)) return true;
      return false;
    }
  }  
}


    
public static void main(String[] args){
	int[] a = new int[]{2,4,4,8};
  System.out.println(groupSumClump(0,a,14));
}
}
`