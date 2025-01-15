class Tree:

    tree_statuses = {'dormant', 'flowering', 'fruiting'}

    # adding __slots__ prevents new attributes being added
    def __init__(self, species, genus, group, status):
        self.species = species.title()
        self.genus = genus.title()
        if status.lower() not in self.tree_statuses:
            raise ValueError(f'Invalid status')
        self.status = status.lower()
        self.group = group.upper()
        # note that in the init statement, adding = 'something' gives a default of 'something'

    def __str__(self):
        return f'{self.group}: {self.species}, {self.genus}. Currently {self.status}.'


gala = Tree('Gala', 'RoYal', 'Apple', 'Flowering')

print(gala)
