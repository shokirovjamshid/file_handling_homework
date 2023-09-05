def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data,'r')
    data = f.read()
    data_int_list = []
    for i in data:
        if i.isdigit():
            data_int_list.append(int(i))
    return data_int_list
# Read data from file
