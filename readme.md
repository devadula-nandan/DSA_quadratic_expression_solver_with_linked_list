<!-- '{"name":"DSA Quadratic Expression Solver","version": 12,"tech": ["Python","DSA","LinkedList"],"tags":["backend"],"snapshots":[]}' -->
# project title - polynmial function solving using linked lists

# brief about the project
in this project we solve polynomial equations using linked lists
we perform operations such as addition, multiplication
we sort the given polynomial equation by implementing bubble sorting algorithm in the linked list class

# function behaviours
the addition() function takes two parameters (linked lists) and performs the polynomial addition on them.
in polynomial addition, the coefficients of nodes with same matching powers are added and the unique (non matching) terms are inserted to the result list. and is printed/returned

the multiplication() function takes two parameters (linked lists) and performs the polynomial multiplication on them.
in polynomial multiplication, the coefficients are multiplied and the powers are added, for each node of list1 with respect to list2, and the result is simplified and stored as a new linked list and is printed/returned

the sorting_function() utilizes the sort_linked_list() method in function_operation.py and prints/returns the result linked list
the sort_linked_list() method uses bubble sorting algorithm and sorts the polynomial to descending order of powers

# Build Status
stable for all test cases with different powers and coefficients
sorting can be improved further in terms complexity

# how to use
create and insert data in the two lists on which the operations need to be performed in main.py and call the appropriate methods

# custom sample test case

    List1 = function_operation.Function_LinkedList()
    print("\n1. First equation is being created: ")
    List1.insert_data(3, 12)
    List1.insert_data(2, 4)
    List1.insert_data(0, 1)
    
    print("\nThe data is : ")
    List1.display()            
    
    print("\n2. Second equation is being created: ")
    List2 = function_operation.Function_LinkedList()
    List2.insert_data(4, 1)
    List2.insert_data(1, 4)
    List2.insert_data(0, 1)
    
    print("\nThe data is : ")
    List2.display()

    addedList = addition(List1, List2)
    multipliedList = multiplication(List1, List2)
    sortedList = sorting_function(multipliedList)

# output

1. First equation is being created:

The data is :
12 * x ^ 3 + 4 * x ^ 2 + 1

2. Second equation is being created:

The data is :
x ^ 4 + 4 * x ^ 1 + 1

Addition_equation: x ^ 4 + 12 * x ^ 3 + 4 * x ^ 2 + 4 * x ^ 1 + 2
Multiplication_equation: 12 * x ^ 7 + 49 * x ^ 4 + 28 * x ^ 3 + 4 * x ^ 6 + 4 * x ^ 2 + 4 * x ^ 1 + 1
Sorted_equation: 12 * x ^ 7 + 4 * x ^ 6 + 49 * x ^ 4 + 28 * x ^ 3 + 4 * x ^ 2 + 4 * x ^ 1 + 1
