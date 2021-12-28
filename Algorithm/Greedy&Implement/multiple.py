
input_loaction = input()
row = int(input_loaction[1])
column = int(ord(input_loaction[0])) - int(ord('a'))+1

steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
cnt =0
for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    if(next_row>=1 and next_row<=8 and next_column >=1 and next_column <=8):
        cnt+=1

print(cnt)