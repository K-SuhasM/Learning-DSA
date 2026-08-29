# def one_to_n(i,n):
#     while i>n:
#         return
#     print(i, end=" ")
#     one_to_n(i+1,n)

# one_to_n(1,10)    

def fctorial(n):
    if n==0:
        return 1
    return n*fctorial(n-1)
    
print(fctorial(4))
# n=1
# x=input("Enter a number: ")
# while n<=int(x):
#     print(n)
#     n+=1