def create_list(size):
    """
    Creates a deque-like data structure with a fixed-size list.

    Parameters:
    - size: The fixed size of the deque.

    Returns:
    A dictionary representing the deque:
    {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }
    """
    return {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }


def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """
    if listADT['n'] == 0:
        return True
    return False 

def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """
    if listADT['n'] == listADT['size']:
        return True
    return False

def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """
    return listADT['data'][i]

def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """
    listADT['data'][i] = e
    

def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """
    return listADT['n']

def rear_index(listADT):
    size = listADT['size']
    n = listADT['n']
    idx = listADT['i']
    rear = idx - n 
    if rear < 0:
        rear += size
    return rear

def add(i, e, listADT):
    """
    Adds an element at the specified index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.
    """
    size = listADT['size']
    data = listADT['data']
    n = listADT['n']
    idx = listADT['i']

    if i < 0 or i >= size:                      # check if the index is valid
        print("Error: Index out of bounds")
        return
    
    if is_full(listADT):
        print("Error: Deque is full")
        return

    rear_check = rear_index(listADT)-1
    if rear_check < 0: 
        rear_check += size
    
    # print("front check", rear_check)
    # print("idx", idx)
    if i == rear_check and idx != rear_check:                       # adding at front 
        data[i] = e
        # print("Hao hao")

    else:
        if is_empty(listADT) or i == idx:                      # adding in empty deque or adding at storing index (front). 
            data[i] = e
            listADT['i'] = (i+1)%size               # store index 'i' have been modified

        else:
            # print("hao")
            n_of_shifts = idx-i
            if n_of_shifts < 0: 
                n_of_shifts += size 

            j = idx
            # print(n_of_shifts)
            for _ in range(n_of_shifts):           # Shifting elements to the right
                if j < 0:
                    j = j+size
                next_ = j-1 
                if next_ < 0:
                    next_ = next_+size
                data[j] = data[next_]
                j-= 1
                next_ -=1 
            data[i] = e                        # Inserting element at specified index

            listADT['i'] = (idx+1)%size        # store index 'i' have been modified

        # Updating 
    listADT['data'] = data
    listADT['n'] += 1
    

def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """
    size = listADT['size']
    data = listADT['data']
    n = listADT['n']
    idx = listADT['i']

    if i < 0 or i >= size:                      # check if the index is valid
        print("Error: Index out of bounds")
        return
    
    if is_empty(listADT):
        print("Error: Deque is empty")
        return
    
    if data[i] == None:
        print("Error: Nothing to Remove")
        return

    rear_check = rear_index(listADT)

    if i == rear_check and (idx+1)%size != rear_check:                       # removing from rear end 
        # print("hao1")
        data[i] = None
        listADT['i'] = idx
    
    else:
        if i == idx-1:                      # removing from front (storing index - 1). 
            # print("hao2")
            data[i] = None
            if n < size:
                i-=1
            if i < 0: 
                i += size
            listADT['i'] = (i + 1)%size

        else:
            n_of_shifts = idx-i
            if n_of_shifts < 0: 
                n_of_shifts += size 

            j = i
            next_ = (j+1)%size
            # print(n_of_shifts)
            for _ in range(n_of_shifts):           # Shifting elements to the right
                data[j] = data[next_]
                j = (j+1)%size
                next_ = (next_+1)%size                         # Inserting element at specified index

            data[idx] = None
            if n < size:
                idx -= 1 
            if idx < 0:
                idx += size
            listADT['i'] = (idx+1)%size        # store index 'i' have been modified

        # Updating 
    listADT['data'] = data
    listADT['n'] -= 1

def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    size =  listADT['size']
    rear_check = rear_index(listADT)-1
    if is_empty(listADT):
        rear_check += 1
    if rear_check < 0: 
        rear_check += size
    add(rear_check, e, listADT)
    

def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    size =  listADT['size']
    rear_check = rear_index(listADT)
    if rear_check < 0: 
        rear_check += size
    remove(rear_check, listADT)

def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    idx =  listADT['i']
    add(idx, e, listADT)

def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    idx = listADT['i']
    # print("idx:", idx)
    size = listADT['size']
    idx -= 1
    if idx < 0:
        idx += size
    # print("idx:", idx)
    remove(idx, listADT)
    

def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """
    idx = listADT['i']
    size = listADT['size']
    idx -= 1
    if idx < 0:
        idx += size
    return get(idx, listADT)

def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
    size =  listADT['size']
    rear_check = rear_index(listADT)
    if rear_check < 0: 
        rear_check += size
    return get(rear_check, listADT)


# a = create_list(5)
# print(a)
# insert_last(2, a)
# print(a)
# insert_first(3, a)
# print(a)
# insert_last(4, a)
# print(a)
# insert_last(5, a)
# print(a)
# insert_first(6, a)
# print(a)
# remove_last(a)
# print(a)
# remove_first(a)
# print(a)
# remove_last(a)
# print(a)
# print(get_first(a))
# print(get_last(a))



















# add(4, 2, a)
# print(a)
# add(0, 3, a)
# print(a)
# add(0, 4, a)
# print(a)
# add(3, 5, a)
# print(a)
# add(4, 6, a)
# print(a)
# add(4, 6, a)
# remove(0, a)
# print(a)
# remove(4, a)
# print(a)
# remove(1, a)
# print(a)
# remove(0, a)
# print(a)