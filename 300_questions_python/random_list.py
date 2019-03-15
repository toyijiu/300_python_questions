import random

def my_shuffle(sorted_list):
    result = []
    while sorted_list:
        index = random.randrange(0,len(sorted_list))
        result.append(sorted_list[index])
        del(sorted_list[index])

    return result

if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(my_shuffle(a))