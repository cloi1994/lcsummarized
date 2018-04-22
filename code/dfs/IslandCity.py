
'''
Given a matrix of size n x m, the elements in the matrix are 0、1、2. 0 for the sea, 1 for the island, 
and 2 for the city on the island(You can assume that 2 is built on 1, ie 2 also represents the island).
If two 1 are adjacent, then these two 1 belong to the same island. Find the number of islands with at least one city.

Given mat =
[
     [1,1,0,0,0],
     [0,1,0,0,1],
     [0,0,2,1,2],
     [0,0,0,0,0],
     [0,0,0,0,2]
]

return 2.

Explanation:
There are 3 islands, and two of them have cities.
'''

class Solution:
    """
    @param grid: an integer matrix
    @return: an integer 
    """
    def numIslandCities(self, grid):
        # Write your code here
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                hasCities = [False]
                if grid[i][j] == 1 or grid[i][j] == 2:
                    self.dfs(i,j,grid,hasCities)
                    if hasCities[0]:
                        count += 1
        
        return count          
    def dfs(self,i,j,grid,hasCities):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        if grid[i][j] == 2:
            hasCities[0] = True

        grid[i][j] = 0
        
        self.dfs(i+1,j,grid,hasCities)
        self.dfs(i-1,j,grid,hasCities)
        self.dfs(i,j+1,grid,hasCities)
        self.dfs(i,j-1,grid,hasCities)
          
          
        
