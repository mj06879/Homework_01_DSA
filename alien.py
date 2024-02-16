import list_adt as listadt
import random 

def create_alien() -> dict:
    """
    Creates an 'alien' dictionary with a list to store messages.
    You can add other attributes if required

    Returns:
    A dictionary representing an 'alien' with a list to store messages:
    {
        'messages': listadt.create_list(100)    # List to store messages with a maximum capacity of 100
    }
    """
    messages = {'messages':listadt.create_list(100),
                'R_num': random.randint(1, 100),
                'min_no': 0,
                'max_no': 0, 
                'count': 0}

    # provide other required implementation here
    return messages

def add(seq: int, msg: str, alienList: dict):
    """
    Parameters:
    - seq: The sequence number of the message.
    - msg: The message to be added.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    # print(alienList)
    if alienList['count'] == 0:
        listadt.insert_first(msg,alienList['messages'])
        alienList['min_no'] = seq
        alienList['max_no']  = seq
        alienList['count'] += 1
    else:
        if seq > alienList['max_no']:
            alienList['max_no'] = seq
            alienList['R_num'] += 1
            listadt.insert_first(msg,alienList['messages'])
        elif seq < alienList['min_no']:
            alienList['min_no'] = seq
            alienList['R_num']  -= 1
            listadt.insert_last(msg,alienList['messages'])

def delete(seq: int, msg: str, alienList: dict):
    """

    Parameters:
    - seq: The sequence number of the message to be deleted.
    - msg: The message to be deleted.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    listadt.remove_first(alienList['messages'])

def get_messages(alienList: dict) -> list[str]:
    """

    Parameters:
    - alienList: The 'alien' dictionary containing the messages list.

    Returns:
    A list of all messages in the conversation.
    """

    # provide implementation here
    
    # we need to use the array implementation here just to return a list of all messages,
    # otherwise we can just return our circular listadt.
    # still using fixed size array

    n = alienList['messages']['n']
    result = [None]*n
    for i in range(n):
        result[i] = listadt.get_last(alienList['messages'])
        listadt.remove_last(alienList['messages'])

    return result


def main(filename) -> list[str]:
    """
    Reads data from a file, processes it, and returns the conversation as a list.

    Data is provided in the following format:
    There can be multiple lines in the file, each line containing an integer and an optional string separated by a space. The integer represents the sequence number of the message, and the string represents the message itself. If the string is not provided, it is assumed to be an empty string. The sequence number 0 indicates the end of the conversation.

    Process the data as follows:
    - If the sequence number is 0, stop processing the file.
    - If the sequence number is positive, add the message to the conversation.
    - If the sequence number is negative, delete the message from the conversation.
    
    Parameters:
    - filename: The name of the file to read data from.

    Returns:
    A list representing the conversation obtained from the file.
    """
    
    messages = create_alien()
    # print(messages['messages'])
    with open (filename) as f :
        lines = f.readlines()

    # R_num = random.random()
    count = 0

    for i in lines:
        line = i.strip().split()
        seq_no = int(line[0])
        if seq_no == 0:
            result = get_messages(messages)
            break
        elif seq_no < 0:
            delete(seq_no,msg,messages)
        else:
            msg  = line[1]
            add(seq_no, msg, messages)
    
    return ' '.join(result)

print(main("Inputs/alien02.txt"))