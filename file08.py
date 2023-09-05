def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data,mode='r+')
    data = f.read()
    for i in data:
        if i.isdigit():
            max = int(i)
    max1 = max
    for n in data:
        if n.isdigit():
            if max1<int(n):
                max1 = int(n)
    return max1
print(main('data/data08.txt'))
# Read data from file