class Node:

    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
    def get(self, index: int) -> int:
        current = self.head
        cnt = 0
        while cnt<index and current is not None:
            current = current.next
            cnt += 1
        if current is None:
            return -1
        return current.data


    def insertHead(self, val: int) -> None:
        new_node = Node()
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node()
        new_node.data = val
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return None
        current = self.head

        while current.next is not None:
            current = current.next
        
        current.next = new_node
        

    def remove(self, index: int) -> bool:

        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        
        current = self.head
        cnt = 0
        while (cnt < index - 1) and current is not None:
            current = current.next
            cnt += 1
        if current is None or current.next is None:
            return False
        current.next = current.next.next
        return True

        

    def getValues(self) -> List[int]:
        iter_list = []
        current = self.head
        while current is not None:
            iter_list.append(current.data)
            current = current.next

        return iter_list
        
