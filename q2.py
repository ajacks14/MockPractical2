def search(str,lst,size):
    for x in range(size):
        if lst[x] == str:
            return x
    return -1

print(search("quallude",["ape","gibbon","cat","dog","quallude"],5))