class Solution {
    public int fib(int n) {
        return res(n);
    }
    public int res(int n)
    {
        if(n==1)
        {
            return 1;
        }
        if(n==0)
        {
            return 0;
        }

        return res(n-1)+res(n-2);

    }
}