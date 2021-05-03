def average(elem_list):
    if len(elem_list) == 0:
        return 0
    sum = 0
    for i in elem_list:
        sum += i
    return sum / len(elem_list)