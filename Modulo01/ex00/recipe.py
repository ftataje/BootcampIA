import sys

class Recipe():
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    def __str__(self):
        txt = self.name
        return txt

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != "":
            self._name = name
        else:
            print("Error: nombre debe ser string y no ser vacío")
            sys.exit()
    
    @property
    def cooking_lvl(self):
        return self._cooking_lvl
    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        if isinstance(cooking_lvl, int) and 1 <= cooking_lvl <= 5:
            self._cooking_lvl = cooking_lvl
        else:
            print("Error: cooking_lvl no esta en el parametro")
            sys.exit()
    
    @property
    def cooking_time(self):
        return self._cooking_time
    @cooking_time.setter
    def cooking_time(self, cooking_time):
        if isinstance(cooking_time, int) and 0 <= cooking_time:
            self._cooking_time = cooking_time
        else:
            print("Error: cooking_time no esta en el parametro")
            sys.exit()
    
    @property
    def ingredients(self):
        return self._ingredients
    @ingredients.setter
    def ingredients(self, ingredients):
        for i in ingredients:
            if isinstance(i, str) and i != "":
                pass
            else:
                print("Error: ingredientes deben ser string y no ser vacío")
                sys.exit()
        self._ingredients = ingredients

    @property
    def recipe_type(self):
        return self._recipe_type
    @recipe_type.setter
    def recipe_type(self, recipe_type):
        if isinstance(recipe_type, str) and (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
            self._recipe_type = recipe_type
        else:
            print('Error: recipe_type debe ser string y ser "starter", "lunch" or "dessert"')
            sys.exit()



'''

Carapulcra = Recipe("Carapulcra chinchana", 4, 80, ["patata","pasta","ajiPanca"],"","lunch")

print(Carapulcra)
print(Carapulcra.cooking_lvl)
'''



