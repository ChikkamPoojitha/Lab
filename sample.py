s = input("enter string : ")


def fn(s) :
    br1 = s[::2]
    br2 = s[1::2]
    brr = br1 + br2
    print(brr)
    
    l1 = []
    
    for i in brr :
        l1.append(brr.count(i))
        #print(l1)


    for i in l1 :
        if l1[i] == 1 :
            return brr[i]
    return "-1"
    
print(fn(s))