from bs4 import BeautifulSoup
import requests
import csv

def start_scraping(url,site):
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    description = []
    keyword = "🧐 How-To"
    desc = soup.select_one(".description")
    for d in desc:
        description.append(d.text)
    description = [description[1]]


    title = soup.select_one('.product-title h1').text
    current_price = soup.select_one('#ProductPrice-product-template').text
    actual_price = soup.select_one('#ComparePrice-product-template .money').text
    images = []
    product_links = soup.select('a.product-single__thumbnail--product-template')

    for link in product_links:
        images.append(link.get('href'))

    # print(description)
    try:
        index = description[0].index(keyword) + len(keyword)
        how_to_ = description[0][index:]
        index = description[0].index(keyword)
        des_to_be_used = description[0][:index]
    except ValueError:
        how_to_ = "Just eat it"
        des_to_be_used = description[0]
    # print(how_to_)

    # add everything to the csv file
    f = open(f'{site}.csv', 'a')
    writer = csv.writer(f)
    row = [title,current_price,actual_price,des_to_be_used,how_to_,images]
    writer.writerow(row)

    # close the file
    f.close()


# start_scraping("https://foodkoreadubai.com/products/copy-of-cheese-rice-tteokbokki-270g-1pc-only-available-for-dubai-areas-deira-till-dubai-marina-excluding-far-areas#how-to","beverages")