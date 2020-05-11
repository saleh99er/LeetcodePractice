// My attempt at Problem 27: Remove Element Problem, faster than 100% of submissions but less memory than 5% of submissions

class Solution {
    public static int indexOfLastValidEl(int elementsRemovedSoFar, int n){
        return n-1-elementsRemovedSoFar;
    }

    public static int removeElement(int[] nums, int val) {
        int elRemoved = 0;
        for(int i = nums.length-1; i >= 0; i--){
            if(nums[i] == val){ // swap with valid elements near end of the array 
                int swapIndex = indexOfLastValidEl(elRemoved, nums.length);
                int temp = nums[swapIndex];
                nums[swapIndex] = nums[i];
                nums[i] = temp;
                elRemoved++;
            }
        }
        return nums.length - elRemoved;
    }

    public static void main(String[] args){
        int[] arr = {3, 2, 3, 5, 7};
        int x = removeElement(arr, 3);
        System.out.println(""+x);
    }
}