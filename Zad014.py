import copy

list = [1,2,['t','d','f'],['w','e','r']]
list_shallowcopy = list
list_deepcopy = copy.deepcopy(list)

print(f"List:       {list}")
print(f"Shallowcopy {list_shallowcopy}")
print(f"Deepcopy    {list_deepcopy}")
print()
list_deepcopy[2][1] = 'd'
list_shallowcopy[2][1] = 's'

print(f"List:       {list}")
print(f"Shallowcopy {list_shallowcopy}")
print(f"Deepcopy    {list_deepcopy}")