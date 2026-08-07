class Solution {
    public boolean isAnagram(String s, String t) {
        /* Given two strings s and t, return true if the two strings are anagrams 
        of each other, otherwise return false. 
        
        An anagram is a string that contains the exact same characters as another string,
        but the order of the characters can be different.
        */

        /* Normalize the strings */
        /* Convert both strings to lowercase to handle insensitivity.
           Remove any whitespace and special characters if they are not 
           considered part of the anagram comparison.*/
        s = s.toLowerCase().replaceAll("\\s", "");
        t = t.toLowerCase().replaceAll("\\s", "");

        /* Check lengths */
        if (s.length() != t.length()) return false;

        /* Convert to Character Array */
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        /* Sort Character Arrays */
        Arrays.sort(sArr);
        Arrays.sort(tArr);

        /* Compare Character Arrays */
        return Arrays.equals(sArr, tArr);
    }
}
