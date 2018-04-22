
#Given a 2D array, and each line has only 0 and 1, the front part is 0, and the latter part is 1. 
#Find the number of columns in the leftmost 1 of all the rows in the array.

#Given arr = [[0,0,0,1],[1,1,1,1]], return 0.

#Given arr = [[0,0,0,1],[0,1,1,1]], return 1.


class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        # Write your code here
        
        startRow = 0
        endRow = len(arr) - 1
        
        minCol = len(arr[0]) - 1
        #limit the col range
        rightBound = len(arr[0]) -1
        
        while startRow <= endRow:
            pos = self.binarySearch(arr[startRow],rightBound)
            if pos == 0:
                return pos
            elif pos > 0:
                minCol = min(minCol,pos)
                rightBound = pos - 1
            startRow += 1
        return minCol
    
    #find the first index of 1's in arr
    def binarySearch(self,arr,rightBound):
        low = 0
        high = rightBound
        while low <= high:
            mid = low + (high - low ) // 2
            if arr[mid] == 1 and (mid == 0 or arr[mid-1] == 0):
                return mid
            elif arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return -1
