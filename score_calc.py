import score_sort
def ones(array):
    count = 0
    for i in array:
        if i == 1:
            count += 1
    return count * 1
def twos(array):
    count = 0
    for i in array:
        if i == 2:
            count += 1
    return count * 2

def threes(array):
    count = 0
    for i in array:
        if i == 3:
            count += 1
    return count * 3

def fours(array):
    count = 0
    for i in array:
        if i == 4:
            count += 1
    return count * 4

def fives(array):
    count = 0
    for i in array:
        if i == 5:
            count += 1
    return count * 5

def sixes(array):
    count = 0
    for i in array:
        if i == 6:
            count += 1
    return count * 6
def choice(array):
    return array[0]+array[1]+array[2]+array[3]+array[4]
def small_straight(array):
    array=score_sort.score_sort(array)
    count=0
    for i in range(len(array) - 1):
        if array[i+1]-array[i]==-1:
            count+=1
    if count>=3:
        return 15
    else:
        return 0

def large_straight(array):
    array = score_sort.score_sort(array)
    count = 0
    for i in range(len(array) - 1):
        if array[i + 1]-array[i] == -1:
            count += 1
    print(array)
    if count >= 4:
        return 30
    else:
        return 0
def full_house(array):
    array = score_sort.score_sort(array)
    if ((array[0]==array[1]==array[2] and array[3]==array[4]) or(array[0]==array[1] and
            array[2]==array[3]==array[4])):
        return array[0]+array[1]+array[2]+array[3]+array[4]
    else:
        return 0
def four_kind(array):
    array = score_sort.score_sort(array)
    if array[0]==array[1]==array[2]==array[3] or array[1]==array[2]==array[3]==array[4]:
        return array[0]+array[1]+array[2]+array[3]+array[4]
    else:
        return 0
def yacht(array):
    if len(set(array))==1:
        print("Yacht!")
        return 50
    else:
        return 0

