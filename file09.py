def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data,mode='r+')
    data = f.read()
    for i in data:
        if i.isdigit():
            min = int(i)
    min1 = min
    for n in data:
        if n.isdigit():
            if min1>int(n):
                min1 = int(n)
    return min1
print(main('data/data08.txt'))
# Read data from file