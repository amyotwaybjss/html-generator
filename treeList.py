from definingTrees import Tree

# Creating trees:
gala = Tree('gala', 'RoYal', 'Apple', 'Fruiting', 'Plot 1')
golden = Tree('delicious', 'golden', 'Apple', 'Fruiting', 'Plot 1')
w_grape = Tree('grape', 'white', 'Grape', 'Fruiting', 'Plot 2')
r_grape = Tree('grape', 'red', 'Grape', 'flowering')
orange = Tree('orange', None, 'orange', 'flowering')

# print(gala)

# this prints all trees

for item in Tree.tree_list:
    print(item)
