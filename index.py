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


# Get recipe by link

def get_recipe_by_link(link):
    recipe = {}
    page = open_url(link)
    soup = BeautifulSoup(page, 'html.parser')
    div_recipe = soup.find(attrs={'class': 'inforecetacont'})

    recipe_title = div_recipe.find(attrs={'class': 'tituloreceta'}).find('h1').text
    image_url = div_recipe.find(attrs={'class': 'carousel'}).find('div').find('div').find('img').get('src')
    cook_url = div_recipe.find(attrs={'class': 'tituloing'}).find('a').get('href')
    div_ingredients = div_recipe.find(attrs={'class': 'boxinfoing'}).find('div').find('ul').find_all('li')
    div_tags = div_recipe.find(attrs={'class': 'tagsReceta'}).find('ul').find_all('li')

    tags = []
    ingredients = []

    for tag in div_tags:
        tags.append(tag.find('a').text)

    for ingredient in div_ingredients:
        ingredients.append(ingredient.text)

    recipe['title'] = recipe_title
    recipe['image'] = image_url
    recipe['ingredients'] = ingredients
    recipe['tags'] = tags
    recipe['cook_url'] = cook_url

    return recipe

