from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com/catalogue/page-{}.html'

pages = []
for x in range(1, 40):
    myurl = url.format(x)
    page = requests.get(myurl)
    print(myurl)
    pages.append(page)


def checker(a):
    if(a == "icon-ok"):
        return "In stock"
    return "Out of stock"


for i in pages:
    soup = BeautifulSoup(i.content, "html.parser")
    products = soup.find_all(attrs={"class": "product_pod"})
    for x in products:
        name = x.h3.a.text
        rating = x.find(attrs={"class": "star-rating"})['class'][1]
        product_attrs = x.find(attrs={"class": "product_price"})
        price = product_attrs.find(attrs={"class": "price_color"}).string
        availability = checker(product_attrs.find(
            attrs={"class": "availability"}).i['class'][0])
        print("Product Name :{} Product rating :{} Product price :{} Product Availability : {}".format(
            name, rating, price, availability))
