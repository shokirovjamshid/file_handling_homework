def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data,'r')
    data = f.read()
    t = 0
    for i in data:
        t+=1
    return t
print(main('data/data02.txt')) 
# Read data from file