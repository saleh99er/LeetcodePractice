from typing import List

class SubrectangleQueries:
    """
    Implement the class SubrectangleQueries which receives a rows x cols 
    rectangle as a matrix of integers in the constructor and supports 
    two methods:

    1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

    Updates all values with newValue in the subrectangle whose upper 
    left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).

    Assuming coords are within the index range of the rectangle and first pair
    is more to the left and higher than the second pair. 

    2. getValue(int row, int col)

    Returns the current value of the coordinate (row,col) from the rectangle.

    Approach analysis (for update):
        Time is O(nm) where n is row2-row1 and m is col2-col1


    Performance:
        Runtime: 200 ms, faster than 59.14% of Python3 
        Memory Usage: 16.1 MB, less than 18.67% of Python3
    """
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.rows = len(rectangle)
        if len(rectangle) > 0:
            self.cols = len(rectangle[0])
        else:
            self.cols = 0

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:

if __name__ == '__main__':
    rectangle = [ [0, 0, 0], [0, 0, 0], [0, -1, 0]]
    obj = SubrectangleQueries(rectangle)
    row1, col1 = 0,0
    row2, col2 = 2,2
    newValue = 9
    obj.updateSubrectangle(row1,col1,row2,col2,newValue)
    row, col = 2, 1
    param_2 = obj.getValue(row,col)
    print(param_2)