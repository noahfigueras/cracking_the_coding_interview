string = str(input())

def stringCompressor(string):
    result = ''
    current = ''
    i = 0

    for n in range(len(string)+1):
        if n < len(string):
            if i == 0: 
                current = string[n]
                i+=1
            elif current == string[n]:
                i+=1
            else:
                result += current + str(i) 
                i=1
                current = string[n]
        else:
            result += current + str(i)  

    if result > string:
        return string
    return result

print(stringCompressor(string))




