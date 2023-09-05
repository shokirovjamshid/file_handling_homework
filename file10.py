def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data,mode='r+')
    data = f.read().split('\n')
    len_max = len(data[0])
    for i in data:
        if len_max<len(i):
            len_max = len(i)
    return len_max
print(main('data/data10.txt'))
# Read data from file