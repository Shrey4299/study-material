class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Insert after a given node
    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must be in the linked list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head node holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Key not found
        if temp == None:
            print("Node with value", key, "not found.")
            return

        prev.next = temp.next
        temp = None

    # Search for a node by value
    def search_node(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    # Traverse and print the linked list
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Usage example:
if __name__ == "__main__":
    ll = LinkedList()

    # Insert some nodes
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_beginning(0)

    # Traverse the linked list
    print("Linked List:")
    ll.traverse()

    # Insert after a node
    print("\nInsert 1.5 after node with value 1:")
    node_to_insert_after = ll.head.next  # Node with value 1
    ll.insert_after_node(node_to_insert_after, 1.5)
    ll.traverse()

    # Delete a node
    print("\nDelete node with value 2:")
    ll.delete_node(2)
    ll.traverse()

    # Search for a node
    print("\nSearch for node with value 1.5:")
    if ll.search_node(1.5):
        print("Node found.")
    else:
        print("Node not found.")

    # Reverse the linked list
    print("\nReverse the linked list:")
    ll.reverse()
    ll.traverse()

# **********************************************************************************************************************

# To add LinkedList into a list

# new_head = ListNode(ans[0], None)
# ans_head = new_head

# for i in range(1, len(ans)):
#     new_head.next = ListNode(ans[i], None)
#     new_head = new_head.next

# ***************************************************************************************************

# Using reverse with problem question

class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
     # Utility function to create a copy of a linked list
    def copyList(self, head):
        if not head:
            return None
        
        new_head = Node(head.data)
        current_new = new_head
        current_original = head.next
        
        while current_original:
            new_node = Node(current_original.data)
            current_new.next = new_node
            current_new = new_node
            current_original = current_original.next
        
        return new_head
    
    # Function to add one to the linked list
    def addOne(self, head):
        # Step 1: Reverse the linked list
        head = self.reverse(head)

        # # Step 1: Create a reversed version of the linked list
        # reversed_head = self.reverse(self.copyList(head))
        
        # Step 2: Traverse the list and add one
        current = head
        carry = 1  # Initialize carry as 1 because we are adding 1
        
        while current:
            new_sum = current.data + carry
            carry = new_sum // 10
            current.data = new_sum % 10

            if carry == 0:
                break

            if carry == 1 and not current.next:
                current.next = Node(1)
                break

            current = current.next
        
        # Step 3: Reverse the list back to the original order
        head = self.reverse(head)
        
        return head
