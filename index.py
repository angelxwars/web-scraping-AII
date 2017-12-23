from urllib import request
from bs4 import BeautifulSoup


def open_url(url):
    try:
        page = request.urlopen(url)
        return page
    except:
        print("Error to open page")
        return None


# Get list with recipe book title and recipe book link

def get_recipe_books(url):
    threads = []
    page = open_url(url)
    soup = BeautifulSoup(page, 'html.parser')

    div_recipe_books = soup.find_all(attrs={'class': 'col-md-3'})

    for recipe_book in div_recipe_books:
        recipe_link = recipe_book.find('div').find('a').get('href')
        recipe_title = recipe_book.find('div').find('a').find(attrs={'class': 'titleLista'}).find('h2').text

        threads.append({'recipe_title': recipe_title, 'recipe_link': recipe_link})

    return threads


print(get_recipe_books('http://www.recetags.com/recetarios'))
