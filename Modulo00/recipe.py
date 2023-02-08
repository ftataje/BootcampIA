dic = {'Sandwich':{'ingredients':['ham', 'bread', 'cheese', 'tomatoes'], 'meal':'lunch', 'prep_time':15}, 'Cake':{'ingredients':['flour', 'sugar', 'eggs'], 'meal':'dessert', 'prep_time':60}, 'Salad':{'ingredients':['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal':'lunch', 'prep_time':15}}

import sys

def printCookbook():
    for key, value in dic.items():
        if isinstance(value, dict): # check if value is a dictionary    
            print(key)

def printRecipe(name):
    if name in dic:
        print("Recipe for " + name + ":")
        print("Ingredients list: " + str(dic[name]['ingredients'])) #str() to convert list to string
        print("To be eaten for " + dic[name]['meal'] + ".")
        print("Takes " + str(dic[name]['prep_time']) + " minutes of cooking.")
    else:
        print("This recipe does not exist")

def deleteRecipe(name):
    if name in dic:
        del dic[name]
    else:
        print("This recipe does not exist")

def addRecipe(name, ingredients, meal, prep_time):
    if name in dic:
        print("This recipe already exists")
    else:
        dic[name] = {'ingredients':ingredients, 'meal':meal, 'prep_time':prep_time}


def main():
    if len(sys.argv) == 1: # no arguments
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        while True:
            try:
                choice = int(input(">> "))
                if choice == 1:
                    name = input("Please enter the recipe's name: ")
                    ingredients = input("Please enter the recipe's ingredients: ")
                    meal = input("Please enter the recipe's meal type: ")
                    prep_time = input("Please enter the recipe's preparation time: ")
                    addRecipe(name, ingredients, meal, prep_time)
                    print("Please select an option: 1, 2, 3, 4 or 5:")
                elif choice == 2:
                    name = input("Please enter the recipe's name to delete it: ")
                    deleteRecipe(name)
                    print("Please select an option: 1, 2, 3, 4 or 5:")
                elif choice == 3:
                    name = input("Please enter the recipe's name to get its details: ")
                    printRecipe(name)
                    print("Please select an option: 1, 2, 3, 4 or 5:")
                elif choice == 4:
                    printCookbook()
                    print("Please select an option: 1, 2, 3, 4 or 5:")
                elif choice == 5:
                    print("Cookbook closed.")
                    break
                else:
                    print("This option does not exist, List of available options: 1, 2, 3, 4, 5")
                    print("To exit, enter 5.")
            except ValueError:
                print("This option does not exist, please select an option: 1, 2, 3, 4 or 5:")
                print("To exit, enter 5.")
    