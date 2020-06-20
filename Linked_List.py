# Linked List Implementation in Python By Ashutosh Deshpande
# All the comments are written for future understanding.

# Singly Linked List

# This implementation requires 2 classes

# 1. Node class

class Node:                     # This Class will specify the properties of the node
    def __init__(self,data):    # Initialize
        self.data = data        # Data is the data container of the node in linked list and Data is initailized here for the node
        self.next = None        # Next is the next part of the node that contains the address of the next node

# 2. Linked List class

class Linked_List:              # This Class specifies the properties of the linked list and contains all the operations of the linked list
    def __init__(self):         # Initialization
        self.head = None        # The head of the linked list is initialized here

# Inserting Elements in a Singly Linked List
# Types:
# 1. At the end of the list ; 
    
    def append(self,data):       # Append Class does the work of appending the new node at the end of the linked list
        new_node = Node(data)    # New Node is created here and initialized with the data

        if self.head is None:    # Check whether the list is empty and if empty
            self.head = new_node # then head will be the new node
            return               # return the list   
        
        last_node = self.head    # As we are appending the node to the last so the new node will be the last node and head is pointed to that node

        while last_node.next:    # Traverse the list until we reach the last node and when the next node is none then the loop will break
            last_node = last_node.next  # When we reach the last node then last node's next pointer should be pointing to the new last node
        last_node.next = new_node   # Last node's next pointer is now pointing to the new node


# 2. At the start of the list ; 

    def prepend(self, data):    # Prepend class does the work of insertig a node at the start of the list
        new_node = Node(data)   # Initialize the new node
        new_node.next = self.head # Assigning head to the next pointer of the new node
        self.head = new_node    # new node is the first node so head is now pointing to the new node

# 3. Somewhere in between the list

    def insert_after_node(self, prev_node, data):   # This function does the work of after a specified node that is passed as a parameter to this function
        
        new_node = Node(data)   # Initialize new node
        curr_node = self.head   # Current node is set here as the head node
        
        while(curr_node.data != prev_node): # This loop finds whether the current node's data is same as the passed node data string and traverses the list until the same is found
            curr_node = curr_node.next      # Until the passed node is not equal to the current node while traversing the list this will assign the next pointer to the next node to move forward
            if curr_node is None:           # if current node is none at this stage then diretly it prints out that node is not in the list and breaks out of the function 
                print("Previous node is not in the list")
                return
                                            # Here that node is now found i.e current node is now equal to the passed node
        new_node.next = curr_node.next      # we assign the new node's next pointer to the current node's next pointer so to attach that node to the new node
        curr_node.next = new_node           # and the current node's next pointer is the new node so in this way we establish the connection

# Singly Linked List : Deleting a node
# We Encounter 2 cases here:
# 1. The node to be deleted is the head node
# 2. The node to be deleted is other than head
    
    def delete_node(self, key):
        
        curr_node = self.head            #  We assign head pointer to a node
        
# In 1st case: 
# i) Change where head is pointing 
# ii) Remove next pointer of that node i.e point that next pointer to none so the node is now deleted

        if curr_node and curr_node.data == key: # if the curr_node is not none i.e the list is not empty -and- curr_node's data matches with the passed data key then...
            self.head = curr_node.next      #   we first assign the next pointer of the current node i.e the next node itself to be the head and then...
            curr_node = None                #   the current node is discarded or deleted from the list by pointing it to nothing
            return                          #   return the function

# In 2nd case:
# i) Loop through the list
# ii) Keep track of what node proceeds the current nod

        prev = None                                 # Previous variable is taken and assigned None, it represents the previous node of the node that is going to be deleted here

        while curr_node and curr_node.data != key:  # case 2 scenario: traverse the list until we find the key that we are looking for here, so when we find that then it will come out of the loop
            prev = curr_node                        # prev node is initialized by the current node
            curr_node = curr_node.next              # and next pointer of the current node is also put here so to move along in the loop

        if curr_node.next is None:                  # Now if current node's next pointer is None then the list is empty
            return                                  # so return    
        
        prev.next = curr_node.next                  # Now as we have found the node to be deleted so we put the previous node's next pointer to be the current node's next means next node, so we break the connection of the node to be deleted 
        curr_node = None                            # and the current node is now assigned none so it's deleted

# Deleting node at given position: Here we are going to delete node at given position
# Same concept : At head or not at head

    def delete_node_at_pos(self, pos):  # This function will delete node at specified position
        curr_node = self.head           # head is pointed to the current node

        # At head   
        if pos == 0:                    # This checks whether the position is 0 that is head of the list
            self.head = curr_node.next  # head is pointed to the next node of the current node
            curr_node.next = None       # the node is deleted hence by assigning the current node's next pointer to None
            return                      # return
        
        # Not at head
        prev = None                     # Here we need to see the previous node too, so initialize it to None for now
        count = 1                       # We take a count variable here to see our position
        while curr_node and count != pos:   # here we loop through till the curr_node node is not none i.e is active and the count is not equal to the position 
            prev = curr_node            # Traversing through the list, curr_node is the previous node now
            curr_node = curr_node.next  # current node's next is now put as current node
            count += 1                  # Count is incremented by 1 to move forward ; this loop goes on till we find the required position

        if curr_node is None:           # Checking whether current node is none
            return                      # return if current node is none

        prev.next = curr_node.next      # Once we find the current node, then previous node's next is set to current node's next pointer means the next node of current node
        curr_node.next = None           # and the current node's next pointer is set to None so it is deleted now



# Print the linked list
    def print_list(self):
        current_node = self.head            # Head is pointing to the first node here
        while current_node:                 # Loop until current node is none
            print(current_node.data)        # Print the data of the current node
            current_node = current_node.next    # Current node's next is pointing to the next in line node


# Create an object of the Linked List class to use it further onwards
linkedlist = Linked_List()

# Append Class usage
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("C")
linkedlist.append("D")
linkedlist.append("G")
linkedlist.append("H")

# Prepend class usage
linkedlist.prepend("E")
linkedlist.print_list()

####
print("Break between usage of functions")
####

# Insert after a node usage
linkedlist.insert_after_node("A", "F")       # Remove this line's comment to see the usage of insert_after_node function's usage
linkedlist.print_list()

#####
print("Break between usage of functions")
#####

# Delete a node usage
linkedlist.delete_node("B")
linkedlist.print_list()

####
print("Break between usage of functions")
####

# Delete a node at given position usage
linkedlist.delete_node_at_pos(5)


# Print the list
linkedlist.print_list() 


