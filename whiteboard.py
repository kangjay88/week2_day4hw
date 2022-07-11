# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome 
# (the same word spelled forward and backwards).
# Example Input: ‘racecar’
# Example Output: True

def palindrome(word):

    reverse = word[::-1]
    if reverse == word:
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome")

palindrome('word')


def palindrome2(word):
    left = 0
    right = len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrome2('racecar'))


#SHOPPING CART PROBLEM:

def addToCart():
    pass
def removeFromCart():
    pass
def showCart():
    pass
def goShopping():
    while True:
        action=input("What do you want to do? add/remove/show/quit").lower()
        if action == 'add':
            addToCart(cart)
        elif action == 'remove':
        elif action == 'show':
        elif action == 'quit':
            break
        else: 
            print("Invalid action, please try again")