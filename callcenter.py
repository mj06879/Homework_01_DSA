# DO NOT CHANGE THIS FUNCTION
# Create a basic queue
def create_queue(size: int) -> dict:
    """
    Description: Creates and initializes a basic queue with a specified size.
    Parameters: size - an integer representing the size of the queue.
    Return: A dictionary representing the initialized queue.
    """
    return {
        'data': [None] * size,  # list of elements
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# DO NOT CHANGE THIS FUNCTION
# Create a priority queue
def create_priority_queue(size: int) -> dict:
    """
    Description: Creates and initializes a priority queue with a specified size.
                 Each element in the queue is a tuple consisting of data and priority.
    Parameters: size - an integer representing the size of the priority queue.
    Return: A dictionary representing the initialized priority queue.
    """
    return {
        'data': [(None, float('inf'))] * size,  # list of elements with default priority set to infinity
        'front': -1,  # index of the first element in the queue
        'rear': -1,  # index of the last element in the queue
        'n': 0,  # number of elements in the queue
        'size': size  # size of the queue
    }

# Check if the queue is full
def is_full(queue: dict) -> bool:
    """
    Description: Checks if the given queue is full (reached its maximum capacity).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is full, False otherwise.
    """
    if queue['n'] == queue['size']:
        return True
    return False

# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    """
    Description: Checks if the given queue is empty (contains no elements).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is empty, False otherwise.
    """
    if queue['n'] == 0:
        return True
    return False 

# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    """
    Description: Adds an element with the value 'val' to the rear of the queue.
    Parameters: queue - a dictionary representing the queue, val - the value to be added to the queue.
    """
    data = queue['data']
    n = queue['n']
    size = queue['size']
    front = queue['front']
    rear = queue['rear']

    if is_full(queue):
        print("Error: Queue is full")
        return
    
    elif is_empty(queue):
        front = 0
        rear = 0
        data[front] = item

    else:
        rear = (rear+1)%size
        data[rear] = item

    # Updating: 
    queue['data'] = data
    queue['front'] = front
    queue['rear'] = rear
    queue['n'] += 1

    
# Remove and return the element from the front of the queue
def dequeue(queue: dict) :
    """
    Description: Removes and returns the element from the front of the queue.
    Parameters: queue - a dictionary representing the queue.
    Return: The element from the front of the queue.
    """
    data = queue['data']
    n = queue['n']
    size = queue['size']
    front = queue['front']
    rear = queue['rear']

    if is_empty(queue):
        print("Error: Queue is empty")

    elif n == 1:
        value = data[front]
        data[front] = None
        front = 0
        rear = 0
    else:
        value = data[front]
        data[front] = None
        front = (front+1)%size
    
    # Updating: 
    queue['data'] = data
    queue['front'] = front
    queue['rear'] = rear
    queue['n'] -= 1
    return value

# Return the element at the front of the queue without removing it
def peek(queue: dict):
    """
    Description: Returns the element at the front of the queue without removing it.
    Parameters: queue - a dictionary representing the queue.
    Return: The element at the front of the queue.
    """
    front = queue['front']
    data = queue['data']
    return data[front]

# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    """
    Description: Adds an element with the value 'val' and the specified priority to the priority queue.
    Parameters: queue - a dictionary representing the priority queue, val - the value to be added to the queue,
                priority - the priority of the element.
    """
    data = priority_queue['data']
    n = priority_queue['n']
    size = priority_queue['size']
    front = priority_queue['front']
    rear = priority_queue['rear']

    if is_full(priority_queue):
        print("Error: Priority Queue is full")
        return
    elif is_empty(priority_queue):
        front = 0
        rear = 0
        data[front] = (item, priority)

    else:
        idx = rear           # index to insert
        while(idx > front and data[idx][1] > priority):
            data[(idx+1)%size] = data[idx]
            idx -= 1

        if idx < 0:
            idx += size
        # print(idx)
        idx = (idx + 1)%size
        data[idx] = (item, priority)
        rear = (rear+1)%size

    priority_queue['data'] = data
    priority_queue['front'] = front
    priority_queue['rear'] = rear
    priority_queue['n'] += 1
    



# Remove and return the element with the minimum priority from the priority queue
def dequeue_min_priority(priority_queue: dict):
    """
    Description: Removes and returns the element with the minimum priority from the priority queue.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    data = priority_queue['data']
    n = priority_queue['n']
    size = priority_queue['size']
    front = priority_queue['front']
    rear = priority_queue['rear']

    if is_empty(priority_queue):
        print("Error: Priority_queue is empty")
        return

    if n == 1:
        value = data[front]
        data[front] = None
        front = 0
        rear = 0
        n -= 1
    else:
        value = data[front]
        data[front] = None
        front = (front+1)%size
        n-=1
    
    # Updating
    priority_queue['data'] = data
    priority_queue['n'] = n
    priority_queue['front'] = front
    priority_queue['rear'] = rear
    return value

# Return the element with the minimum priority from the priority queue without removing it
def peek_min_priority(priority_queue: dict):
    """
    Description: Returns the element with the minimum priority from the priority queue without removing it.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """

    if is_empty(priority_queue):
        print("Error: Priority_queue is empty")
        return

    return priority_queue['data'][priority_queue['front']]


def CallSimulator(callQueue, agentQueue) -> dict:
    """
    Description: Simulates a call center scenario where calls are processed by agents based on their availability.
    Type: Function
    Parameters: callQueue - a dictionary representing the call queue,
                AgentQueue - a dictionary representing the agent queue.
    Return: A queue containing information about each processed call (callerName, call_start, call_end, wait_time).
    """
    # Simulation parameters
    Simulation = True
    currentTime = 0
    
    # Create a queue to store the call log
    callLog = create_queue(callQueue['size'])
    reserve = create_priority_queue(agentQueue['size'])
    Wait = False
    while not is_empty(callQueue):
        # provide your implementation here

        while not is_empty(callQueue) and not is_empty(agentQueue):

            call = peek(callQueue)
            start_time = int(call[0])
            duration = int(call[2])
            if start_time <= currentTime:
                call = dequeue(callQueue)
                agent = dequeue_min_priority(agentQueue)
                waiting_time = max(0, currentTime - start_time)
                end_time = currentTime + duration
                agent = (agent[0], end_time)            # priority update
                enqueue_priority(reserve, agent[0], end_time)
                enqueue(callLog,(call[1], currentTime, end_time, waiting_time))

                # print("Call_Log: ", callLog)
                # print()
            else:
                currentTime += 1        # for waiting for call coming in future, in callqueue.

            
        # chekcing if agent is available if agent is available:
        while is_empty(agentQueue):

            agent_add = False
            next_agent = peek_min_priority(reserve)

            while next_agent[1] <= currentTime:         # Agents can be free at same so while loop. 
                next_agent = dequeue_min_priority(reserve)
                enqueue_priority(agentQueue, next_agent[0], 0)
                next_agent = peek_min_priority(reserve)
                agent_add = True
            else:
                break 

        # Increment the current time for the next iteration
        if not agent_add:
            currentTime += 1

    # Returning the queue containing the call log
    # print("callLog: ", callLog)
    return callLog


def main(filename) -> list:
    """
    Description: Main function to read input data from a file, initialize agent and call queues, simulate call processing using CallSimulator, and return the call log data.
    Parameters: filename - the name of the file containing input data.
    Return: A list representing the call log data.
    """
    
    # Read input data from the file
    # First line contains the list of agents separated by spaces 
    # Second line contains the number of calls to be processed
    # Populate the call queue with call details from the remaining lines contain the call details (start time, caller name, call duration) separated by spaces

    # provide your implementation here 
    with open (filename) as f :
        lines = f.readlines()
    # print()
    agents = lines[0].split()
    no_of_agents = len(agents)
    agentQueue = create_priority_queue(no_of_agents)

    for i in range(no_of_agents):
        enqueue_priority(agentQueue, agents[i], 0)

    no_of_calls = int(lines[1].split()[0])
    call_queue = create_queue(no_of_calls)

    for i in lines[2:]: 
        line = i.strip().split()
        enqueue(call_queue, line)


    # Simulate call processing using CallSimulator
    call_log = CallSimulator(call_queue, agentQueue)

    # Return the call log data as a list
    return call_log['data']

# print(main('Inputs/callcenter01.txt'))



# a = create_queue(5)
# print(a)
# enqueue(a, 1)
# print(a)
# enqueue(a, 3)
# print(a)
# # dequeue(a)
# # print(a)
# print(peek(a))
# dequeue(a)
# print(a)


# a = create_priority_queue(5)
# print(a)
# enqueue_priority(a, 14, 1)
# print(a)
# enqueue_priority(a, 2, 3)
# print(a)
# enqueue_priority(a, 13, 5)
# print(a)
# enqueue_priority(a, 6, 4)
# print(a)
# print(dequeue_min_priority(a))
# print(a)
# # enqueue_priority(a, 7, 3)
# print(peek(a))
# enqueue_priority(a, 8, 2)
# print(a)

# print(dequeue_min_priority(a))
# print(a)
# print(dequeue_min_priority(a))
# print(a)
# print(dequeue_min_priority(a))
# print(a)
# print(dequeue_min_priority(a))
# print(a)