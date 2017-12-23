from urllib import request
from bs4 import BeautifulSoup


# open any url

def open_url(url):
    try:
        page = request.urlopen(url)
        return page
    except:
        print("Error to open page")
        return None


# Get list with recipe book title and recipe book link

def get_recipe_books(url):
    books = []
    page = open_url(url)
    soup = BeautifulSoup(page, 'html.parser')
    div_recipe_books = soup.find_all(attrs={'class': 'col-md-3'})

    for book in div_recipe_books:
        recipe_link = book.find('div').find('a').get('href')
        recipe_title = book.find('div').find('a').find(attrs={'class': 'titleLista'}).find('h2').text
        books.append({'recipe_book_title': recipe_title, 'recipe_book_link': recipe_link})

    return books


# Get recipe links in a recipe_book

def get_recipes_link_by_book(book):
    recipes_link = []
    page = open_url(book['recipe_book_link'])
    soup = BeautifulSoup(page, 'html.parser')
    div_recipes = soup.find_all(attrs={'class': 'cajaReceta'})

    for recipe in div_recipes:
        link = recipe.find(attrs={'class': 'staticrcp'}).find('a').get('href')
        recipes_link.append(link)

    return recipes_link



recipe_books = get_recipe_books('http://www.recetags.com/recetarios')

for recipe_book in recipe_books:
    print(get_recipes_link_by_book(recipe_book))
