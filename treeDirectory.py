from definingClasses import Tree, Field

# Creating trees:
gala = Tree('gala', 'RoYal', 'Apple', 'Fruiting', 'Plot 1')
golden = Tree('delicious', 'golden', 'Apple', 'Fruiting', 'Plot 1')
w_grape = Tree('gr1', 'white', 'Grape', 'Fruiting', 'Plot 2')
r_grape = Tree('gr2', 'red', 'Grape', 'flowering')
orange = Tree('orange', None, 'orange', 'flowering')
# cherry = Tree('cherry', None, 'cherry', 'dormant')

# Creating list containing all trees:
all_trees = []
for item in Tree.tree_list:
    all_trees.append(item)

# Creating fields:
field_a = Field("Field A")
field_b = Field("Field B")
field_c = Field("Field C")

# Add trees to fields
field_a.add_tree(gala)
field_b.add_tree(gala)
field_b.add_tree(golden)

print(f"{golden.species} is in fields: {[f.name for f in golden.fields]}")

