from copy import copy
from functools import reduce
import json
from operator import attrgetter, itemgetter


class Book:
	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)
			
	def __str__(self):
		return self.title
		
	def __repr__(self):
		return str(self)
		
def get_books(filename, raw=False):
	try:
		data = json.load(open(filename))
	except FileNotFoundError:
		return []
	else:
		if raw:
			return data['books']
		return [Book(**book) for book in data['books']]
		
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

###--- Functional programming sort
# Creating a sorted list by publish date
print("Sort output:")
pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])

# Creating a sorted list by 
pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)
def sales_price(book):
	"""Apply a 20@ discount to the price"""
	book = copy(book)
	book.price = round(book.price*0.8, 2)
	return book
print("\n")

###--- Functional programming map
# map is similar to list comprehension - prefer map if list comprehension is too long
sales_books = list(map(sales_price, BOOKS))

#list comprehension
sales_book2 = [sales_price(book) for book in BOOKS]
print("Map output:")
print(BOOKS[0].price)
print(sales_books[0].price)
print(sales_book2[0].price)
print("\n")

###--- Functional programming filter
def is_long_book(book):
	"""Does a book have 600 or more pages"""
	return book.number_of_pages >= 600
	
# filter is also similar to list comprehension - prefer filter if list comprehension is too long
long_books = list(filter(is_long_book, BOOKS))
# List comprehension
long_books2 = [book for book in BOOKS if book.number_of_pages >=600]
print("Filter output:")
print(len(BOOKS))
print(len(long_books))
print(len(long_books2))
print("\n")

###--- Functional programming chaining 
def has_roland(book):
	return any(["Roland" in subject for subject in book.subjects])
	
def titlecase(book):
	book = copy(book)
	book.title = book.title.title()
	return book
# chaining filter and map into same list	
print("Chaining output:")
print(list(map(titlecase, filter(has_roland, BOOKS))))

# printing books cheaper than 5$
def is_good_deal(book):
	return book.price <= 5

cheap_books = sorted(
	filter(is_good_deal, map(sales_price, BOOKS)),
	key=attrgetter('price')
)

for i in cheap_books:
	print(i, i.price)
print("\n")

###--- Functional programming reduce
def product(x, y):
	return x * y
print("Reduce output")
print(reduce(product,[1,2,3,4,5]))

#Don't use in real world
total = 0 
for x in [1,2,3,4,5]:
	total = x * total if total else x * 1
print(total)

def add_book_prices(book1, book2):
	return book1 + book2

total = reduce(add_book_prices, [b.price for b in BOOKS])
print(total)

def long_total(a=None, b=None, books=None):
	if a is None and b is None and books is None:
		return None
	if a is None and b is None and books is not None:
		a = books.pop(0)
		b = books.pop(0)
		return long_total(a, b, books)
	if a is not None and books and books is not None and b is None:
		b = books.pop(0)
		return long_total(a, b, books)
	if a is not None and b is not None and books is not None:
		return long_total(a+b, None, books)
	if a is not None and b is not None and not books:
		return long_total(a+b, None, books)
	if a is not None and b is None and not books or books is None:
		return a
		
print(long_total(None, None, [b.price for b in BOOKS]))
print("\n")

print("Factorial output:")
def factorial(n):
	if n==1:
		return 1
	else:
		return n * factorial(n-1)
print(factorial(5))
print("\n")

###--- Lambda output
#import os
#clear = lambda:os.system('cls')
#clear()
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
print("Lambda output")
print(total)

long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
good_deals = filter(lambda book: book.price <= 6, BOOKS)
print(len(list(good_deals)))

