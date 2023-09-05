def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, mode='r+')
    data_1 = f.read()
    s = 0
    for i in data_1:
        if i.isdigit():
            s+=int(i)
    return s
print(main('data/data07.txt')) 
# Read data from file