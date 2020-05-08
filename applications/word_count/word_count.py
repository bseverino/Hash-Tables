cache = {}

def word_count(s):
    if s == '':
        return {}

    elif s not in cache:
        counts = {}
        s_list = s.translate(s.maketrans('', '', '":;,.-+=/\|[]{}()*^&')).lower().split(' ')
        for i in s_list:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        cache[s] = counts

    return cache[s]



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))