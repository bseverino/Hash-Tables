cache = {}

def no_dups(s):
    if s == '':
        return ''
    
    elif s not in cache:
        s_list = s.split(' ')
        s_filtered = []
        for i in s_list:
            if i not in s_filtered:
                s_filtered.append(i)
        cache[s] = ' '.join(s_filtered)
    
    return cache[s]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))