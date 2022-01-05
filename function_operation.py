class Node:
    def __init__(self, power = 0, coeff = 0):    
        self.power = power
        self.coeff = coeff
        self.next = None

class Function_LinkedList: 


    def __init__(self):
        self.head = None
        self.power = 0
        self.coeff = 1    

    def insert_data(self, power, coeff):
        # creating new node for data insertion
        self.power = power
        self.coeff = coeff
        new_node = Node(self.power, self.coeff)
        # assigning head to the temp variable
        if self.head == None:
            self.head = new_node

        else:
            tmp = self.head
            while(tmp.next):
                tmp = tmp.next
            tmp.next = new_node

        return self.head

        
    def display(self):
        # print the content of the list
        # Initializing the temp variable for traversal
        temp = self.head
        # checking the condition if there are some elements are there in the linked list
        if self.head is not None:
            # running the loop till temp is traversed once completely
            # To print the equation without any confusion, we are iterating till the second last node of the list
            while(temp.next):
                # printing the data
                if temp.coeff == 0:
                    pass
                elif temp.power != 0:
                    if temp.coeff == 1: 
                        print("x", "^", temp.power, end = " + ")
                    else: 
                        print(temp.coeff, "*", "x", "^", temp.power, end = " + ")
                else:
                    if temp.coeff == 1: 
                        print(1, end = " + ")
                    else: 
                        print(temp.coeff, "*", "x", "^", temp.power, end = " + ")


                # moving to the next node
                temp = temp.next
            if(temp.power != 0):
                if temp.coeff == 1:
                    print("x", "^", temp.power)
                else:
                    print(temp.coeff, "*", "x", "^", temp.power)
            else:
                print(temp.coeff)

    def sort_linked_list(self) :
        # we sort the linked list with bubble sorting algorithm, we maintain two pointers fptr(first pointer) sptr(second pointer) and compare the powers to sort the given polynomial equation
        fptr = self.head
        while fptr : 
            sptr = fptr.next
            while sptr : 
                if fptr.power < sptr.power : 
                    fptr.power, sptr.power = sptr.power, fptr.power 
                    fptr.coeff, sptr.coeff = sptr.coeff, fptr.coeff
                sptr = sptr.next
            fptr = fptr.next 