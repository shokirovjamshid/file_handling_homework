def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data,'r')
    data = f.read()
    data_elimint_list = []
    t = 0
    while len(data)>t:
        data_elimint_list.append(data[t])
        t+=1
    return data_elimint_list
print(main('data/data04.txt'))
# Read data from file