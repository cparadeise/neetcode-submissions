class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
         the solution involves using prefix and suffix 
            products from the current index
        */
        int nLen = nums.length;
        // Creates a mutable list of nums.length items, all initialized to 1
        int[] products = new int[nums.length];
        Arrays.fill(products, 1);
        
        int prefix = 1;
        int suffix = 1;
        for (int i = 0; i < nLen; i++) {
                products[i] *= prefix;
                prefix *= nums[i];
        }

        for (int i = nLen - 1; i >= 0; i--) {
            products[i] *= suffix;
            suffix *= nums[i];
        }

        return products;
    }
}  
