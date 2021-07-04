import java.util.*;
import java.util.HashMap;


// Since the MergeSort algorithm is very well-known, I got a template from GeeksForGeeks so that I don't have to re-invent the wheel. Nonetheless, my searching algorithm uses divide and conquer with recursion, and it's my own unique solution.
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
        // Find sizes of two subarrays to be merged
        int n1 = m - l + 1;
        int n2 = r - m;
        /* Create temp arrays */
        int L[] = new int[n1];
        int R[] = new int[n2];
        /*Copy data to temp arrays*/
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];
        /* Merge the temp arrays */
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;
        // Initial index of merged subarry array
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        /* Copy remaining elements of L[] if any */
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        /* Copy remaining elements of R[] if any */
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
        if (l < r) {
            // Find the middle point
            int m =l+ (r-l)/2;
            // Sort first and second halves
            sort(arr, l, m);
            sort(arr, m + 1, r);
            // Merge the sorted halves
            merge(arr, l, m, r);
        }
    }
    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}


class Solution {
    
    //My unique divide and conquer solution using recursion
    public int[] find_numbers(int[] nums, int index_og, int index_now, int target, Set<Integer> dictionary) { //index determines the index the count is on
        // Make sure that a solution exists, otherwise, move on to the next chosen number in the array
        if (!dictionary.contains(target - nums[index_og])) {
            return find_numbers(nums, index_og+1, index_og+2, target, dictionary);
        }
        // Base Case the current number is equal (target - chosen number), return the two indexes
        if (nums[index_now] == (target - nums[index_og])) {
            int[] answer = new int[] {nums[index_now], nums[index_og]} ;
            return answer;
        }
        //If the index goes out of bounds, change the pivot index
        else if (index_now == (nums.length-1)) {
            return find_numbers(nums, index_og+1, index_og+2, target, dictionary);
        }
        // If the current number is less than (target - chosen number), restart the function and move to the next number in the array
        if (nums[index_now] < (target - nums[index_og])) {
           return find_numbers(nums, index_og, index_now+1, target, dictionary);
        }
        // If the current number is greater than (target - chosen number), move on to a new chosen number
        if (nums[index_now] > (target - nums[index_og])) {
            return find_numbers(nums, index_og+1, index_og+2, target, dictionary);
        }
        // If the iteration reached the end of the array
        return find_numbers(nums, index_og, index_now+1, target, dictionary);
    }
    
    //Main Function
    public int[] twoSum(int[] nums, int target) {
        // Put the array in a Set with value as key and index as value
        Set<Integer> dictionary = new HashSet<>();
        int[] orderedList = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            orderedList[i] = nums[i];
            dictionary.add(nums[i]);
        }
        
        // Sort the array
        MergeSort place_holder = new MergeSort();
        place_holder.sort(orderedList, 0, orderedList.length - 1);
        
        // Call recursive algorithm to find the two indices
        int[] numbers = find_numbers(orderedList,0,1,target, dictionary);
        
        //Create two for-loops to find the two indexes in the original array
        int[] solution = new int[2];


        for (int i = 0; i < nums.length; i++) {
            if (numbers[0] == nums[i]) {
                solution[0] = i;
                //render the element empty to avoid duplicates
                nums[i] = 999999999;
                break;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (numbers[1] == nums[i]) {
                solution[1] = i;
                nums[i] = 999999999;
                break;
            }
        }
        
        //Return the solution
        return solution;
    }
}