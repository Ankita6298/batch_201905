i=0
a=4
j=0
while True:
    i = i + 1
    if (a%i)==0 or a==1 or a==2:
        j = j + 1
        if j<=2:
            continue
        else:
            print("not prime")
            break
    elif i>a:
        print("Prime")
        break

