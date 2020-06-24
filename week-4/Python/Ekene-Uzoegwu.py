class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linkedList class

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    

    # append function
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    # reverse function
    def sentence_reverse(self,sentence):
        previous = None
        current = sentence.head
        After = current.next

        while current:
            current.next = previous # revere the link list
            previous = current
            current = After 
            if After:
                After = After.next
        
        sentence.head = previous


    def sum_two_lists(self, llist):
        p = self.head  
        q = llist.head

        sum_of_two_list = LinkedList()

        carry = 0
        while p or q:
            if not p:
                x = 0
            else:
                x = p.data
            if not q:
                y = 0 
            else:
                y = q.data
            sum = x + y + carry
            if sum >= 10:
                carry = 1
                # working with remainder
                remainder = sum % 10
                sum_of_two_list.append(remainder)
            # a case without remainder
            else:
                carry = 0
                sum_of_two_list.append(sum)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_of_two_list.print_list()




llist1 = LinkedList()
llist1.append(7)
llist1.append(6)
llist1.append(5)

llist2 = LinkedList()
llist2.append(3)
llist2.append(4)
llist2.append(2)

print(567 + 242)
# llist1.sum_two_lists(llist2)


print(f"Reverse string function is below")

ReverseSentence = LinkedList()
ReverseSentence.append("lvoe")
ReverseSentence.append("Now")
ReverseSentence.append("lets")
ReverseSentence.append("Bye")

print(f"before reverse")
ReverseSentence.print_list()

print("After reversing")

ReverseSentence.sentence_reverse(ReverseSentence)
ReverseSentence.print_list()