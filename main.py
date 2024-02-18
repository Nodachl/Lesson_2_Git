a=int(input('enter 1 digit '))
b=int(input('enter 1 second digit '))
c=int(input('enter third digit '))
num=input('enter 1-3. 1-max,2-min,3-mean ')
if num=='1':
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)
if num=='2':
    if a<b and a<c:
        print(a)
    elif b<a and b<c:
        print (b)
    elif c<a and c<b:
        print(c)
if num=='3':
    print((a+b+c)/3)

