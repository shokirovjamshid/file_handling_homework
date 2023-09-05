def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data,'r')
    data = f.read()
    t = 0
    digit_soni = 0
    alpha_soni = 0
    while len(data)>t:
        if data[t].isdigit():
            digit_soni+=1
        else:
            alpha_soni+=1
        t+=1
    sonlar = [digit_soni,alpha_soni]
    return sonlar
print(main('data/data05.txt'))
# Read data from file