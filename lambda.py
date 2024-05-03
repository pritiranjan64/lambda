#lambda with one arguement.
multiply=lambda n:n*100
print(multiply(2))     #200   


#lambda with two arguement.
add=lambda a,b:a+b
print(add(2,3))      #5   


#lambda with three arguement.
mul=lambda a,b,c:a*b*c
print(mul(2,5,2))        #20     


#lambda with variable length arguement.
add=lambda *a:sum(a)
print(add(2,3))     #5    


#checking given number is even or not by using lambda function.
isEven=lambda n:n%2==0
print(isEven(12))  #True    


#print the key from a given dictionary whice is having maximum value.
d={'a':10,'b':45,'c':13}
print(max(d,key=lambda k:d[k]))     #b    


#print even number in given range.
isEven=lambda n:n%2==0
for n in range(1,10):
    if isEven(n):
        print(n)    


#using lambda in map function
l=[20,10,30,40,50]
print(list(map(lambda a:a*100,l)))   


print(list(map(lambda s:s.strip(),['hello','hai','bye'])))
print(list(map(lambda s:s.split(),'hello hai bye')))