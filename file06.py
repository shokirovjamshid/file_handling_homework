def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data,'r')
    data = f.read()
    data_list_split = data.split('\n')
    split_list_pupu = []
    for i in data_list_split:
        split_list_pupu.append(len(i))
    return split_list_pupu
print(main('data/data06.txt'))  
# Read data from file