
from sys import exit
#USAGE: python3 menu.py
#USAGE: ./dist/menu

class OrderList:
    def __init__(self):
        self.mealType = None # string --> breakfast / lunch / dinner
        self.mealOrder = None # list --> ['1','2,'3','4']
        self.mealOrderDict = None # dict --> {'1': 1, '2': 2, '3': 1 }

    def validateBreakfast(self): # utility function to help validate and return the breakfast query
        for i in self.mealOrder:
            if(i not in ['1','2','3']): # if the order contains number other than 1,2,3 throw error
                return "Unable to process: Meal item not on menu / Please type order correctly"
        if (len(self.mealOrderDict.keys()) > 4): # if dict has more than 4 items throw error as we only have 1,2,3 items
            return "Unable to process: Menu item not on menu"

        if (self.mealOrderDict['1'] > 1): # If count of 1 for breakfast is more than 1 throw error
            return "Unable to process: Eggs cannot be ordered more than once"

        if (self.mealOrderDict['2'] > 1): # If count of 2 for breakfast is more than 1 throw error
            return "Unable to process: Toast cannot be ordered more than once"

        if ('3' not in self.mealOrderDict): # add water if no drink ordered
            return "Eggs, Toast, Water"

        if (self.mealOrderDict['3'] > 1): # return count of coffee if count of 3 is more than 1
            return "Eggs, Toast, Coffee({})".format(self.mealOrderDict['3'])

        return "Eggs, Toast, Coffee"

    def validateLunch(self): # utility function to help validate and return the lunch query
        for i in self.mealOrder:
            if(i not in ['1','2','3']): # if the order contains number other than 1,2,3 throw error
                return "Unable to process: Meal item not on menu / Please type order correctly"

        if(len(self.mealOrderDict.keys()) > 4): # if dict has more than 4 items throw error as we only have 1,2,3 items
            return "Unable to process: Menu item not on menu"

        if(self.mealOrderDict['1'] > 1): # If count of 1 for lunch is more than 1 throw error
            return "Unable to process: Sandwich cannot be ordered more than once"

        if ('3' not in self.mealOrderDict): # if 3 is not ordered 
            if(self.mealOrderDict['2'] > 1): # If count of 2 for lunch is more than 1 and no 3 is ordered 
                return "Sandwich, Chips({}), Water".format(self.mealOrderDict['2'])
            return "Sandwich, Chips, Water" # If count of 2 for lunch is 1 and no 3 is ordered 

        if(self.mealOrderDict['3'] > 1):# If count of 3 for lunch is more than 1 throw error
            return "Unable to process: Soda cannot be ordered more than once"
        
        if(self.mealOrderDict['2'] > 1):# If count of 2 for lunch is more than 1 return count of items in bracket
            return "Sandwich, Chips({}), Soda".format(self.mealOrderDict['2'])
        return "Sandwich, Chips, Soda"


    def validateDinner(self): # utility function to help validate and return the dinner query
        # for the dinner part I have made my own rules 
        #    1. You cannot order more than 1 side or 1 main or 1 dessert or 1 drink
        for i in self.mealOrder:
            if(i not in ['1','2','3','4']): # if the order contains number other than 1,2,3 throw error
                return "Unable to process: Meal item not on menu / Please type order correctly"

        if(len(self.mealOrderDict.keys()) > 5): # if dict has more than 5 items throw error as we only have 1,2,3,4 items
            return "Unable to process: Menu item not on menu"

        if ('4' not in self.mealOrderDict): # throw error if dessert is not ordered
            return "Unable to process: Dessert is missing"
        
        if(self.mealOrderDict['1'] > 1): # If count of 1 for dinner is more than 1 throw error
            return "Unable to process: Steak cannot be ordered more than once"

        if(self.mealOrderDict['2'] > 1): # If count of 2 for dinner is more than 1 throw error
            return "Unable to process: Potatoes cannot be ordered more than once"

        if('3' not in self.mealOrderDict): # If drink is not ordered return menu with water
            return "Steak, Potatoes, Cake, Water"

        if(self.mealOrderDict['3'] > 1): # If count of 3 for dinner is more than 1 throw error
            return "Unable to process: Wine cannot be ordered more than once"

        if(self.mealOrderDict['4'] > 1): # If count of 4 for dinner is more than 1 throw error
            return "Unable to process: Cake cannot be ordered more than once"

        return "Steak, Potatoes, Wine, Cake, Water" # default return 
    
    def orderList(self,inputString):
        # parsing input string 
        inputList = inputString.split(' ') # list will contain ' ' (space) seperated value
        if(len(inputList) != 2): # if there are more than 2 spaces in input throw error
            return "Unable to process: Please type order correctly"

        self.mealType = inputList[0].lower() #parse self.mealType from input (breakfast,lunch,dinner)
        self.mealOrder = inputList[1].split(',') # parse meal order from input [1, 2, 3, 4]
        self.mealOrderDict = {} # create a dictionary to store number of items Ex. {'1': 1, '2': 2, '3':1 }

        for i in self.mealOrder:
            if(i in self.mealOrderDict.keys()): # update dict if item already exists in dict
                self.mealOrderDict[i] += 1
            else:
                self.mealOrderDict[i] = 1 # make new entry of item if item does not exist in dict

        if(self.mealType not in ['breakfast','lunch','dinner']): #if input is something other than breakfast,lunch,dinner throw error
            return "Unable to process: Meal type not on menu"
        
        if ('1' not in self.mealOrderDict.keys()): # if dict does not have '1' throw error 
            return "Unable to process: Main is missing"

        if ('2' not in self.mealOrderDict.keys()): # if dict does not have '2' throw error 
            return "Unable to process: Side is missing"
        
        
        if (self.mealType == 'breakfast'):
            return self.validateBreakfast()
            
        elif(self.mealType == 'lunch'):
            return self.validateLunch()
            
        elif(self.mealType == 'dinner'):
            return self.validateDinner()

def main():
    print("\n----------------SAUMYA's MENU----------------")
    print("Please enter what you would like to order")
    print("Our menu items are:\n")
    print("Breakfast: 1 - Eggs, 2 - Toast, 3 - Coffee")
    print("Lunch: 1 - Sandwich, 2 - Chips, 3 - Soda")
    print("Dinner: 1 - Steak, 2 - Potatoes, 3 - Wine, 4 - Cake\n")
    print("Note: You can order something like 'Breakfast 1,2,3' and for exiting you can write 'exit'")

    # making an object to call our function
    orderClass=OrderList()

    while(1):
        print("\nOrder: ",end='')
        order = input()
        if(order.lower() == "exit"):
            exit()
        print(orderClass.orderList(order))


if __name__ == "__main__":
    main()
    