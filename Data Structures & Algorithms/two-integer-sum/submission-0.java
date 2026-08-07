class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
          starting indices: i = 0, j = 1
          loop j to nums.length()
          increment both i and j until j = nums.length() and i = nums.length() - 1
          if nums[i] + nums[j] = target, return [i,j]
        */
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                System.out.println(String.format("i: %d, j: %d, i+j: %d", i, j, nums[i]+nums[j]));
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}
