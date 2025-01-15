from definingTrees import Tree

# Creating trees:
gala = Tree('gala', 'RoYal', 'Apple', 'Fruiting')
golden = Tree('delicious', 'golden', 'Apple', 'Fruiting')
w_grape = Tree('grape', 'white', 'Grape', 'Fruiting')
r_grape = Tree('grape', 'red', 'Grape', 'flowering')
orange = Tree('orange', None, 'orange', 'flowering')

# print(gala)

# this prints all trees

for item in Tree.tree_list:
    print(item)
