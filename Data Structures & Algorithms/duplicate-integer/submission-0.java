
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> intNums = new HashSet<>();
        for (int num: nums) {
            if (!intNums.add(num)) {
                return true;
            }
        }
        return false;
    }
}