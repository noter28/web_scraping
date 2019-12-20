import requests
from bs4 import BeautifulSoup

link = 'https://stores.martinsfoods.com/'
output_doc_name = 'output_doc_name.csv'

def write_result(output_doc_name, text):
    with open(output_doc_name, "a") as file:
        file.write(text)


def get_states(link):
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    list_of_states = []

    for article in soup.find_all('a', class_='DirectoryList-itemLink Link--secondary'):
        z = link + article['href']
        list_of_states.append(z)
    #print(list_of_states)
    return list_of_states



def get_cities(states):
    list_of_cities = []
    for i in states:
        source = requests.get(i).text
        soup = BeautifulSoup(source, 'lxml')
        for city in soup.find_all('a', class_='DirectoryList-itemLink Link--secondary'):
            city = link + city['href']
            list_of_cities.append(city)
    print(list_of_cities)
    return list_of_cities



def get_adres(cities):
    for i in cities:
        try:
            source = requests.get(i).text
            soup = BeautifulSoup(source, 'lxml')
            for adr in soup.find_all('div', class_="c-AddressRow"):
                write_result(output_doc_name, adr.text)
                print(adr.text)
        except Exception:
            print('0')


get_adres(get_cities(get_states(link)))
#get_states(link)





#get_states('https://local.safeway.com/safeway.html')

#class="c-directory-list-content-item-link"