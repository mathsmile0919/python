'''
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
每一行都是多个字符+空格+换行
'''
# 使用双重循环
row = 1
# 控制行数
while row <= 9:
    col = 1
    while col <= row:
        print("{}*{}={}".format(col, row, col*row), end=' ')
        col += 1
    print()
    row += 1
