from definingTrees import Tree
# import pandas as pd

# Creating trees:
gala = Tree('gala', 'RoYal', 'Apple', 'Fruiting', 'Plot 1')
golden = Tree('delicious', 'golden', 'Apple', 'Fruiting', 'Plot 1')
w_grape = Tree('grape', 'white', 'Grape', 'Fruiting', 'Plot 2')
r_grape = Tree('grape', 'red', 'Grape', 'flowering')
orange = Tree('orange', None, 'orange', 'flowering')

# print(gala)

# this prints all trees

count = 0

for item in Tree.tree_list:
    print(item)
    count += 1

if count < 1:
    print(f'{count} is less than than 1.')
elif count % 3 == 0:
    print(f'{count} is divisible by three.')
elif count % 2 == 0:
    print(f'{count} is divisible by two.')
elif (count+1) % 3 == 0:
    print(f'{count}+1 is divisible by three.')
elif (count+1) % 2 == 0:
    print(f'{count}+1 is divisible by two.')
else:
    print(f'{count} is invalid.')

# print(count)
