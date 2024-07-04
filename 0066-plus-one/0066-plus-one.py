class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=digits[::-1]
        c=1
        i=0
        while c:
            if i<len(digits):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    c=0
            else:
                digits.append(1)
                c=0
            i+=1
        return(digits[::-1])

            
        
        