class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r_len,c_len=len(matrix),len(matrix[0])
        max_of_row=0
        for i in range(r_len):
            max_r=min(matrix[i])
            max_of_row=max(max_of_row,max_r)
        for j in range(c_len):
            max_c=0
            for k in range(r_len):
                max_c=max(max_c,matrix[k][j])
            if max_c==max_of_row:
                return[max_c]
        return []
        