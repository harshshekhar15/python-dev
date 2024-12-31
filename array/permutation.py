# Check if two given lists are permutations of each other or not

list1 = ['s', 'e', 'r', 'v', 'e']
list2 = ['v', 'e', 'r', 's', 'e']

list3 = ['p', 'e', 'e', 'k']
list4 = ['k', 'e', 'e', 'a']

def is_permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    chars = {}
    for i in list1:
        if i in chars.keys():
            chars[i]+= 1
        else:
            chars[i] = 1
    for i in list2:
        if i in chars.keys():
            chars[i]-= 1
        else:
            chars[i] = 1
    for val in chars.values():
        if val != 0:
            return False
    return True

list5 = [1,2,3]
list6 = [3,2,1]
print(is_permutation(list5, list6))
        