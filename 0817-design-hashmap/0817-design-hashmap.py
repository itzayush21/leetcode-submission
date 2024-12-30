class Node:
    def __init__(self,key=-1,value=-1,next=None):
        self.key=key
        self.value=value
        self.next=next

class MyHashMap(object):

    def __init__(self):
        self.set=[Node() for i in range(10**4)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        head=self.set[key%len(self.set)]
        temp=head
        while temp.next:
            if temp.next.key==key:
                temp.next.value=value
                return
            temp=temp.next
        temp.next=Node(key,value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        head=self.set[key%len(self.set)]
        temp=head
        while temp.next:
            if temp.next.key==key:
                return temp.next.value
            temp=temp.next
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        head=self.set[key%len(self.set)]
        temp=head
        while temp.next:
            if temp.next.key==key:
                temp.next=temp.next.next
                return
            temp=temp.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)