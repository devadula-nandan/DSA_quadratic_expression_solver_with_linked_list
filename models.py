from function_operation import Function_LinkedList

def addition(equation1, equation2):
    ptr1, ptr2 = equation1.head, equation2.head
    # creating new ll to store result
    equation3 = Function_LinkedList()
    # below loop runs till both ll's last node is null(doesnt have any data)
    while ptr1 or ptr2 :
        # if both pointers have data then we check for same power, if hey have same power, we simply add the coefficients, and we insert the same power and summed up coefficient to the equation3 linked list. and change both pointers to next
        if ptr1 and ptr2 :
            if ptr1.power == ptr2.power : 
                equation3.insert_data(ptr1.power, ptr1.coeff + ptr2.coeff)
                ptr1, ptr2 = ptr1.next, ptr2.next
            # if the powers do not match we will insert the greatest power and the respective coefficient to equation3 and change the greatest power's pointer to next
            elif ptr1.power > ptr2.power : 
                equation3.insert_data(ptr1.power, ptr1.coeff)
                ptr1 = ptr1.next
            else : 
                equation3.insert_data(ptr2.power, ptr2.coeff)
                ptr2 = ptr2.next
        # if either one of the pointer dont have data (or null), we will insert the data (power,coefficient) whichever is available (not null) to equation3 and change the corresponding pointer to next
        else : 
            if not ptr1 : 
                equation3.insert_data(ptr2.power, ptr2.coeff)
                ptr2 = ptr2.next
            else : 
                equation3.insert_data(ptr1.power, ptr1.coeff)
                ptr1 = ptr1.next
    # converting the linked list to easy to read format and printing
    print(f'\nAddition_equation:', end = ' ')
    equation3.display()
    return equation3

def multiplication(equation1, equation2):
    ptr1 = equation1.head
    # we maintain a temporary dict to store powers and coefficients as key value pairs in order to multiply the same power node's coefficients by checking in dictionary
    terms = dict({})
    while ptr1 : 
        ptr2 = equation2.head
        while ptr2 : 
            power = ptr1.power + ptr2.power
            if power not in terms : 
                terms[power] = 0
            terms[power] += ptr1.coeff * ptr2.coeff
            ptr2 = ptr2.next
        ptr1 = ptr1.next
    # creating new ll to store result
    equation3 = Function_LinkedList()
    # inserting each key value pair from temporary dictionary, as node to the linked list equation3
    for power, coeff in terms.items() : 
        equation3.insert_data(power, coeff)
    # converting the linked list to easy to read format and printing
    print('Multiplication_equation:', end = ' ')
    equation3.display()
    return equation3

def sorting_function(equation) :
    # the linked list sorting method is implemented in function_operation.py
    equation.sort_linked_list()
    # converting the linked list to easy to read format and printing
    print('Sorted_equation:', end = ' ')
    equation.display()
    return equation
