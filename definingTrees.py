class Tree:

    # adding instances allows us to track all trees
    tree_list = []
    tree_statuses = {'dormant', 'flowering', 'fruiting'}

    # adding __slots__ prevents new attributes being added
    def __init__(self, species, genus, group, status):
        # note that in the init statement, adding = 'something' gives a default of 'something'
        # this makes the attribute optional
        self.species = species
        self.genus = genus
        if status.lower() not in self.tree_statuses:
            raise ValueError(f'Invalid status')
        self.status = status
        self.group = group
        # note that in the init statement, adding = 'something' gives a default of 'something'
        # this makes the attribute optional
        Tree.tree_list.append(self)

    def __str__(self):
        if self.genus is None:
            return f'{self.group.upper()}: {self.species.title()}. Currently {self.status.lower()}.'
        else:
            return f'{self.group.upper()}: {self.species.title()}, {self.genus}. Currently {self.status.lower()}.'

