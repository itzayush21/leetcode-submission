class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for(int i = 0 ; i < image.length; i++) {
            int x = image[0].length - 1;
            for(int j = 0; j <= x; j++, x--) {
                int temp = 1 - image[i][j];
                image[i][j] =  1 - image[i][x];
                image[i][x] = temp;
            }
        }
        return image;
    }
}