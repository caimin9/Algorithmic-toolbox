import sys

def get_change(m):
    
    list = [1,5,10]
    i = 0
   
    while m > 0:
        a = max(list)
        if a > m:
            list.remove(a)
        else:
            m = m-a
            i +=1
    return i
    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
