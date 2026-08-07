// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        int n = pairs.size();
        List<List<Pair>> res = new ArrayList<>(); // To store the intermediate states of the array

        for (int i = 0; i < n; i++) {
            int j = i - 1;

            // Move elements that are greater than key one position ahead
            while (j >= 0 && pairs.get(j).key > pairs.get(j + 1).key) {
                Pair temp = pairs.get(j);
                pairs.set(j, pairs.get(j + 1));
                pairs.set(j + 1, temp);
                j--;
            }

            // Clonse and save the entire state of the array at this point
            List<Pair> cloneList = new ArrayList<>(pairs);
            res.add(cloneList);
        }
        return res;
    }

    // public static void insertionSort(int[] arr) {
    //     int n = arr.length;
    //     for (int i = 1; i < n; i++) { // Start from the second element
    //         int key = arr[i]; // Store the current element
    //         int j = i - 1; // Index of the Last element in the sorted portion

    //         // Move elementsof arr[0..i-1] that are greater than key,
    //         // to one position ahead of their current position
    //         while (j >= 0 && arr[j] > key) {
    //             arr[j + 1] = arr[j];
    //             j = j - 1;
    //         }
    //         arr[j + i] = key;// Place the key in its correct position
    //     }
    // }
}
