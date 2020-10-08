############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, 
                 'Muskmelon')
    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')    
    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw') 
    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')

    musk.add_pairing('mint')
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    cren.add_pairing('proscuitto')
    yw.add_pairing('ice cream')

    all_melon_types.append(musk)
    all_melon_types.append(cas)
    all_melon_types.append(cren)
    all_melon_types.append(yw)
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for i in range(len(melon.pairings)):
            print(f' - {melon.pairings[i]}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melons = {}
    for melon in melon_types:
        melons[melon.code] = melons.get(melon.code, melon)
    
    return melons



############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by


    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False 

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_picked = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melons_picked.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melons_picked.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melons_picked.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melons_picked.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melons_picked.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melons_picked.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melons_picked.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melons_picked.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melons_picked.append(melon_9)    

    return melons_picked


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.is_sellable():
            sellable = "CAN BE SOLD"
        else:
            sellable = "NOT SELLABLE"

        print(f'Harvested by {melon.harvested_by} from Field {melon.field} ({sellable})')



if __name__ == '__main__':

    melon_types = make_melon_types()
    melon_lookup = make_melon_type_lookup
    melons = make_melons(melon_types)