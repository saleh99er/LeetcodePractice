// My attempt at Problem 48: Rotate Image, 0 ms "faster than 100% of java 
// online submissions", memory usage 39.5 MB, less than 60.88% of submissions


class Coordinate{
    int x;
    int y;

    Coordinate(int x, int y){
        this.x = x;
        this.y = y;
    }
    
    public Coordinate rotations(int n, int turns){
        final int Y_MAX = n - 1;
        int x_rotated = this.x;
        int y_rotated = this.y;
        int temp_y = this.y;
        for(int rotations = 0; rotations < turns; rotations++){
            y_rotated = x_rotated;
            x_rotated = Y_MAX - temp_y;
            temp_y = y_rotated;
        }

        return new Coordinate(x_rotated, y_rotated);
    }

    public void printPoint(String append){
        System.out.println( (append + " = (" + this.x + ", " + this.y + ")") );
    }
}

class Solution {

    public static void printMatrix(int[][] matrix){
        for(int[] row : matrix){
            for(int el : row){
                System.out.print( (el + ","));
            }
            System.out.println("");
        }
    }
    
    public static void rotate(int[][] matrix) {
        int midPoint = matrix.length / 2;
        boolean isDimEven = matrix.length % 2 == 0;
        int stopPoint = isDimEven ? midPoint : midPoint + 1;

        for(int row = 0; row < stopPoint; row++){
            for(int col = 0; col < stopPoint; col++){

                if(!isDimEven && row == midPoint){
                    continue; // midpoint, no need to rotate
                }
                
                // Compute 4 points of rotated matrix data in respect to
                // the "pixel" in the matrix at (row, col)
                Coordinate origPoint = new Coordinate(col, row);
                //origPoint.printPoint("p_0");
                Coordinate point_90 = origPoint.rotations(matrix.length, 1);
                //point_90.printPoint("p_90");
                Coordinate point_180 = point_90.rotations(matrix.length, 1);
                //point_180.printPoint("p_180");
                Coordinate point_270 = point_180.rotations(matrix.length, 1);
                //point_270.printPoint("p_270");
                
                // Copy pixel data
                int origPoint_temp_data = matrix[origPoint.y][origPoint.x];
                matrix[origPoint.y][origPoint.x] = matrix[point_270.y][point_270.x];
                matrix[point_270.y][point_270.x] = matrix[point_180.y][point_180.x];
                matrix[point_180.y][point_180.x] = matrix[point_90.y][point_90.x];
                matrix[point_90.y][point_90.x] = origPoint_temp_data;

                // Debugging
                //System.out.println("Finished rotations for (" + row + "," + col + ")");
                //printMatrix(matrix);
            }
        }
    }    

    public static void main(String[] args){
        int[][] test_matrix = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        //printMatrix(test_matrix);
        // System.out.println("--------------");
        rotate(test_matrix);
        //printMatrix(test_matrix);
    }
}