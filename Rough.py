n = "446895"

sum = 0
mul = 1
while True:
    for i in str(n):
        s = int(n)%10
        sum += s

        n= int(n)//10


