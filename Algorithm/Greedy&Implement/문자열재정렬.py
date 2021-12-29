
##무작위 문자열을 문자끼리 오름차순 정렬해준 뒤, 문자열에 있는 숫자들은 따로 더해서 뒤에 붙이는 문제
#예시 : K1KA5CB7 = > ABCKK13
A = input()  #받을 문자열
intsum = 0  #숫자들의 합
strlist ="" # 문자열들끼리 모아놓을 문자열
for ch in A:
    if(ord(ch)<=57 and ord(ch)>=49):
        intsum+= int(ch)
    else:
        strlist+=ch
result= ''.join(sorted(strlist)) + str(intsum) # 최종 결과값
print(result)


