import datetime
import sys
from book import Book
from recipe import Recipe


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

















