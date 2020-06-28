/**
 * My attempt at Problem 1037, First attempted to use OOP / data structs but it hurt runtime performance
 * This solution runs "in 0 ms" and "faster than 100%" of other submissions.
 * memory usage is 37.4 MB, less than 28.57% of other submissions.
 */
class Solution {
    
    public static boolean isDifferent(int[][] points, int p1, int p2){
        return (points[p1][0] != points[p2][0]) || (points[p1][1] != points[p2][1]);
    }

    public static boolean allDistinct(int[][] points){
        return isDifferent(points, 0, 1) && isDifferent(points, 1, 2) && isDifferent(points, 0, 2);
    }
    
    public static float slopeCalculate(int[][] points, int p1, int p2){
        return ((float) points[p2][1] - points[p1][1])/(points[p2][0]-points[p1][0]);
    }
    
    public static boolean isBoomerang(int[][] points) { 
        
        float dy_dx_1_2 =  slopeCalculate(points, 0, 1);
        float dy_dx_2_3 = slopeCalculate(points, 1, 2);
        
        return allDistinct(points) && (dy_dx_2_3 != dy_dx_1_2);
        
    }
}