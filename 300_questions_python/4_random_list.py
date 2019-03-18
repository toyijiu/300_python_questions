import random

def fisher_shuffle(sorted_list):
    result = []
    while sorted_list:
        index = random.randrange(0,len(sorted_list))
        result.append(sorted_list[index])
        del(sorted_list[index])

    return result

def knuth_shuffle(sorted_list):
    for i in range(0,len(sorted_list)-1):
        index = random.randrange(i+1,len(sorted_list))
        sorted_list[i],sorted_list[index] = sorted_list[index],sorted_list[i]
    return sorted_list

#Inside-Out Algorithm
def shuffle(lis):
    result = lis[:]
    for i in range(1, len(lis)):
        j = random.randrange(0, i)
        result[i] = result[j]
        result[j] = lis[i]
    return result


if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(knuth_shuffle(a))