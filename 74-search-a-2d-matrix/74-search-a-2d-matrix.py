class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while(i<len(matrix)):
            low , high = 0 , len(matrix[i]) - 1
            if  matrix[i][low] <= target <= matrix[i][high]:
                while(low<=high):
                    mid = (low+high)//2
                    if matrix[i][mid] < target:
                        low = mid + 1
                    elif matrix[i][mid] > target:
                        high = mid - 1
                    else:
                        return True
            i += 1
        return False

                
            