val = -123
positive_flag = 1
if val < 0:
    positive_flag = -1
    val = -val
result_num = int(str(val)[::-1])*positive_flag
print(result_num)