# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    w, d, h, m, s = 0, 0, 0, 0 , 0
    st = ""
    cnt = 0
    if X >= 604800:
        w = int(X / 604800)
        X = X % 604800
        st += str(w) + "w"
        cnt += 1
    if X >= 86400:
        d = int(X / 86400)
        X = X % 86400
        st += str(d) + "d"
        cnt += 1
        if  cnt >= 2:
            return st
    if X >= 3600:
        h = int(X / 3600)
        X = X % 3600
        st += str(h) + "h"
        cnt += 1
        if cnt >= 2:
            return st
    if X >= 60:
        m = int( X / 60)
        X = X % 60
        st += str(m) + "m"
        cnt += 1
        if cnt >= 2:
            return st
    if X >= 1:
        s = int(X)
        st += str(s) + "s"
        cnt += 1
    return st

    # w = X // ( 60 * 60 * 24 * 7)
    # d = X % 3600 // 60
    # s = seconds % 3600 % 60
    # return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
print(solution(7263))
