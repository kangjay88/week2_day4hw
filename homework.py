# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    def __init__(self, checkout, items):
        self.checkout = checkout
        self.items = items

    def addToCart(self):
        product = input("What item do you want to add to your cart?").lower()
        self.items.append(product)
        print(f"Successfully added {product} to your cart!")
    
    def showCart(self):
        print(self.items)
    
    def removeFromCart(self):
        product = input("What item do you want to remove from your cart?").lower()
        if product in self.items:
            self.items.remove(product)
            print(f"Successfully removed {product} from your cart")
        else:
            print("You do not have that item in your cart")
    
def goShopping():
    
    while True:
        action = input("What do you want to do? Show/Add/Remove/Quit?").lower()
        if action == 'add':
                costco_cart.addToCart()
        elif action == 'show':
                costco_cart.showCart()
        elif action == 'remove':
                costco_cart.removeFromCart()
        elif action == 'quit':
            print("Thank you for shopping with us! Come again soon.")
            break
        else:
            print("Invalid entry, please choose from show/add/remove/quit.")
                
costco_cart = Cart('express', [])
goShopping()
print(costco_cart.items)


#Exercise 2 - Write a Python class which has two methods get_String and print_String. 
#get_String accept a string from the user and print_String print the string in upper case.

class Getset():
    
    def __init__(self, s1):
        self.s1 = s1
    
    def get_String(self):
        return f'{self.s1}'
    
    def print_String(self):
        self.s1 = (self.s1).upper()
           

phrase = Getset("sunny")
print(phrase.s1)
phrase.print_String()
print(phrase.s1)
