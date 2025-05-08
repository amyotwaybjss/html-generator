class Tree:

    # adding instances allows us to track all trees
    tree_list = []
    tree_statuses = {'old', 'growing', 'dormant', 'flowering', 'fruiting'}

    # adding __slots__ prevents new attributes being added
    def __init__(self, species, genus, group, status, location=None):
        # note that in the init statement, adding = 'something' gives a default of 'something'
        # this makes the attribute optional
        self.id = (str(species) + str(genus) + str(group)).lower()
        self.species = species
        self.genus = genus
        self.group = group
        if status.lower() not in self.tree_statuses:
            raise ValueError(f'Unknown status')
        self.status = status
        self.fields = set()
        Tree.tree_list.append(self)

    def __str__(self):
        # This defines how the items in tree_list will be displayed when looped
        return (f'{self.group.upper()}: '
                f'{self.species.title()}'
                f'{'' if self.genus is None else ', ' + str(self.genus).title()}. '
                f'Currently {self.status.lower()}. '
                # f'Currently {self.status.lower()}{'' if self.location is None else ' at ' + str(self.location).upper()}. '
                f'ID: {self.id}')

    def add_field(self, field):
        self.fields.add(field)
        field.trees.add(self)


class Field:
    def __init__(self, name):
        self.name = name
        self.trees = set() # trees in field

    def add_tree(self, tree):
        self.trees.add(tree)
        tree.fields.add(self)

    def __str__(self):
        return f'Field: {self.name}'

