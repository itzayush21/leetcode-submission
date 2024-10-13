class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        cur=""
        j=0
        for i in path+"/":
            print(j+1,"  ",cur)
            if i=="/":
                print(stack)
                if cur=="..":
                    if stack:stack.pop()
                elif cur!="" and cur!=".":
                    stack.append(cur)
                cur=""
            else:
                cur+=i
        print(stack)
        return "/"+"/".join(stack)
