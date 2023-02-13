import datetime
import sys
from recipe import Recipe

class Book():

    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update = datetime.datetime.now()
        self.creation_date = creation_date = datetime.datetime.now()
        self.recipes_list = recipes_list

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
            print("Error: nombre del BOOK debe ser string y no ser vacío")
            sys.exit()

    @property
    def last_update(self):
        return self._last_update
    @last_update.setter
    def last_update(self, last_update):
        if isinstance(last_update, datetime.datetime) and last_update != "":
            self._last_update = last_update
        else:
            print("Error: last_update del BOOK debe ser datetime y no ser vacío")
            sys.exit()
    
    @property
    def creation_date(self):
        return self._creation_date
    @creation_date.setter
    def creation_date(self, creation_date):
        if isinstance(creation_date, datetime.datetime) and creation_date != "":
            self._creation_date = creation_date
        else:
            print("Error: creation_date del BOOK debe ser datetime y no ser vacío")
            sys.exit()

    @property
    def recipes_list(self):
        return self._recipes_list
    @recipes_list.setter
    def recipes_list(self, recipes_list):
        if isinstance(recipes_list, dict):
            for k, v in recipes_list.items():
                if (k == "starter" or k == "lunch" or k == "dessert"):
                    self._recipes_list = recipes_list
                else:
                    print('Error: Elementos de recipes_list deben ser "starter", "lunch" o "dessert"')
                    sys.exit()
        else:
            print('Error: recipes_list debe ser Dict, y elementos deben ser "starter", "lunch" o "dessert"')
            sys.exit()


    def get_recipe_by_name(self, name):
        for k, v in self.recipes_list.items():
            for i in v:
                if i.name == name:
                    return i
        print("Error: No existe receta con ese nombre")
        sys.exit()
    
    def get_recipes_by_types(self, recipe_type):        
        if recipe_type == 'starter':
            return self.recipes_list['starter']
        elif recipe_type == 'lunch':
            return self.recipes_list['lunch']
        elif recipe_type == 'dessert':
            return self.recipes_list['dessert']
        else:
            print('Error: recipe_type debe ser "starter", "lunch" o "dessert"')
            sys.exit()
            
    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print("Error: recipe debe ser de tipo Recipe")
            sys.exit()
        
'''
entr1 = Recipe('causa', 5, 50, ['patata','aji','aguacate'], "prep1", 'starter')
entr2 = Recipe('ceviche', 3, 15, ['pescado','limon','cebolla'], "prep2", 'starter')
lunch1 = Recipe('Carapulcra', 5, 100, ['patata','pasta','ajiPanca'], "", 'lunch')
lunch2 = Recipe('AjiDeGallina', 5, 80, ['patata','pollo','ajiAmarillo'], "", "lunch")
dess1 = Recipe('Mazamorra', 2, 20, ['MaizMorado','Agua','Canela'], "", "dessert")
dess2 = Recipe('Picarones', 3, 30, ['Harina', 'Miel'], "", "dessert")
lunch3 = Recipe('ChicharronCalamar', 2, 50,['Calamar','Harina', 'Limon'], "", 'lunch')

fechaUltim = datetime.datetime(2023, 1, 25, 12, 30, 45)
fechaCrear = datetime.datetime(2022, 12, 25, 12, 30, 45)
PF = {'starter':[entr1, entr2], 'lunch':[lunch1, lunch2], 'dessert':[dess1, dess2]}


libroFood = Book("PeruvianFood", fechaUltim, fechaCrear, PF)
print(libroFood)

libroFood.add_recipe(lunch3)

for k, v in PF.items():
    for i in v:
        print(i)
'''

