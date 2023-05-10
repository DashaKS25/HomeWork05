#https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python

def two_highest(arg1):
    sorted_list = sorted(set(arg1), reverse=True)
    if len(sorted_list) < 2:
        return sorted_list
    return [sorted_list[0], sorted_list[1]]
