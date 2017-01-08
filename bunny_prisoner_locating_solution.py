__author__ = 'lookmayank'
def answer(x_num, y_num):
    step = x_num 
    ans = 0
    while(x_num > 0):
        ans += x_num
        x_num = x_num -1
    if (y_num > 1):
        for i in range(0,y_num - 1):
            ans = ans + i + step
    return ans
