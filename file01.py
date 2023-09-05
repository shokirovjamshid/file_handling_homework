def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data,'r')
    data = f.read()
    data_list = list(map(int,data.split(',')))  
    return data_list
print(main('data/data01.txt'))
# Read data from file