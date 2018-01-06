public class Test{
public static int maxMirror(int[] nums) {
  int len = nums.length;
  int count = 0;
  int max = 0;
  int i,j;
  for(int start = 0; start<len; start++){
    for(int reverseStart = len-1; reverseStart >= 0; reverseStart--){
      if(nums[start] == nums[reverseStart]){
        i = start;
        j = reverseStart;

        while(i<len && j>=0 &&nums[i]==nums[j]){
          count++;
          i++;
          j--;
        }
        max = Math.max(max,count);
        count = 0;
      }
    }
  }
  return max;
  
}

    
public static void main(String[] args){
  int[] k = new int[]{1, 2, 3, 8, 9, 3, 2, 1};
      System.out.println(maxMirror(k));
        }
    }
