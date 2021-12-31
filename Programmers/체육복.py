def solution(n, lost, reserve):
    newlost = [i for i in lost if i not in reserve] ##리스트 선언 안겹치게끔
    newreserve = [k for k in lost if k not in lost]

    for elements in newreserve:
        plus = elements+1  ##출석번호가 뒤
        minus = elements-1 ## 출석번호가 앞
        if plus in newlost:
            newlost.remove(plus)
        elif minus in newlost:
            newlost.remove(minus)
    return n - len(newlost)
