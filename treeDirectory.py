from definingClasses import Tree, Field
from images import fruit_image

# Creating trees:
gala = Tree('gala', 'RoYal', 'Apple', 'Fruiting', 'hi_im_gala')
golden = Tree('delicious', 'golden', 'Apple', 'Fruiting', 'hi_im_golden')
lemon = Tree('lemon', None, 'Citrus', 'Fruiting', 'hi_im_lemon')
lime = Tree('lime', None, 'Citrus', 'flowering', ['hi_im_lime','surprise_lime'])
orange = Tree('orange', None, 'orange', 'flowering', 'hi_im_orange')
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

print(f"{gala.species} {fruit_image["gala"]} is in fields: {[f.name for f in gala.fields]}")
