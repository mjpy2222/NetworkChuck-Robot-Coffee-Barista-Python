#Let's start a coffee shop together!! We're going to build a coffee shop using come new Python programming concepts!!

#Let's build robot Barista!!

#Greet customer

print("Hello, Welcome to NetworkChuck Coffee!!!!!")

#Ask your customer what their name is with the input() function and store that in the variable name.
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation.
if name == "Ben":
  evil_status = input("Are you evil?\n")
  if evil_status == "yes":
    print("You're not welcome here Evil Ben!! Get out!!")
    exit()
  else:
    print("Oh, so you're one of those good Bens. Come on in!!")
else:
  print("Hello " + name + ", thank you so much for coming in today.\n")

beard_length =int(input("How long is your beard?\n"))

if beard_length >= 1:
  print("Oh, hello good sir, nice beard. You may go to the front of the line.")

#Coffee menu
menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

#Ask customer what they would like from the menu and store it in the variable order. 
order = input(name + ", what would you like from our menu today? Here is what we are serving:\n" + menu + "\n")

#Ask the customer how many coffees they would like and store it in the variable quantity.
quantity = input("How many " + order + "s would you like?\n")

#set the price for coffee
if order == "Frappuccino":
  price = 13
elif order == "Black coffee":
  price = 3
elif order == "Espresso":
  price = 5
elif order == "Latte":
  Whipped_cream = input("Would you like whipped cream?")
    if whipped_cream = "yes"
      price = 11
    elif whipped_cream = "no"
      price = 9
elif order == "Cappucino":
  price = 10
else:
  print("Sorry, we don't have that here.")
  price = 0

#Calculate the customer's total
total = price * int(quantity)

#Give the customer their total
print("Thank you. Your total is $" + str(total)))

#Final Statement
print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")
