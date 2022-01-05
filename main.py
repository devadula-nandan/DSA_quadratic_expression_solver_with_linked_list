import function_operation
from models import addition, multiplication, sorting_function

if __name__ == "__main__":
    
    List1 = function_operation.Function_LinkedList()
    print("\n1. First equation is being created: ")
    # Insert operation in the linked list
    # The first parameter represents the power of x
    # the secodn parameter represents the coefficient fo x in the equation
    List1.insert_data(2, 1)
    List1.insert_data(1, 1)
    List1.insert_data(0, 1)
    
    print("\nThe data is : ")
    List1.display()            
    
    print("\n2. Second equation is being created: ")
    List2 = function_operation.Function_LinkedList()
    # Insert operation in the linked list
    # The first parameter represents the power of x
    # the secodn parameter represents the coefficient fo x in the equation
    List2.insert_data(2, 1)
    List2.insert_data(1, 1)
    List2.insert_data(0, 1)

    # printing the content of list
    print("\nThe data is : ")
    List2.display()

    addedList = addition(List1, List2)
    multipliedList = multiplication(List1, List2)
    sortedList = sorting_function(multipliedList)    
    
    

    List3 = function_operation.Function_LinkedList()
    print("\n3. Third equation is being created: ")
    # insert operation in the linked list
    List3.insert_data(2, 3)
    List3.insert_data(1, 4)
    
    print("\nThe data is : ")
    List3.display()            
    
    print("\n4. fourth equation is being created: ")
    List4 = function_operation.Function_LinkedList()
    List4.insert_data(2, 1)
    List4.insert_data(0, 1)
    
    # printing the content of list
    print("\nThe data is : ")
    List4.display()

    addedList = addition(List3, List4)
    multipliedList = multiplication(List3, List4)
    sortedList = sorting_function(multipliedList)