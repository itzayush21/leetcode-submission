class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        num_books = len(books)
        min_height = [0] * (num_books + 1)

        for i, (width, height) in enumerate(books, 1):
            min_height[i] = min_height[i - 1] + height
            total_width = width

            for j in range(i - 1, 0, -1):
                total_width += books[j - 1][0]

                if total_width > shelfWidth:
                    break

                height = max(height, books[j - 1][1])
                min_height[i] = min(min_height[i], min_height[j - 1] + height)

        return min_height[num_books]
