'''5. Insert New Book by Price
A bookstore maintains a sorted list of book prices.
A new book arrives, and its price needs to be placed at the correct
position while keeping the list sorted.
Write a program to perform this task.'''

#Approach:
# Q5. Insert New Book by Price
# The list of prices is already sorted.
# We find the correct spot for the new price by shifting
# bigger elements one step to the right, then placing it in the gap.
# (This is the idea used in Insertion Sort.)

book_prices = [150, 220, 300, 450, 600, 800]

new_price = int(input("Enter the price of the new book: "))

# add one empty spot at the end first
book_prices.append(0)

i = len(book_prices) - 2   # last actual element before the empty spot

# shift elements right while they are bigger than new_price
while i >= 0 and book_prices[i] > new_price:
    book_prices[i + 1] = book_prices[i]
    i = i - 1

book_prices[i + 1] = new_price

print("Updated price list:", book_prices)