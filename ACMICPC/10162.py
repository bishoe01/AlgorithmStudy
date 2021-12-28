T = int(input())
five = 0
one = 0
tens = 0
if (T % 10 != 0):
    print(-1)
else:
    if(T >= 300):
        five += T//300
        T = T % 300
    if(T >= 60):
        one += T//60
        T = T % 60
    if(T >= 10):
        tens += T//10
        T = T % 10
    print(five, one, tens)
