class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[][] arr = new int[m][n];
        int res=0;
        for(int[] e:indices)
        {
            for(int i=0;i<n;i++)
            {
                arr[e[0]][i]+=1;
                if(arr[e[0]][i]%2==1)
                {
                    res++;
                }
                else
                {
                    res--;
                }
            }
            for(int j=0;j<m;j++)
            {
                arr[j][e[1]]+=1;
                if(arr[j][e[1]]%2==1)
                {
                    res++;
                }
                else
                {
                    res--;
                }

            }
        } 
        return res;
    }
}