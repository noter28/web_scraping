import requests
from bs4 import BeautifulSoup

link = 'https://locations.timhortons.com/ca/on/east-york.html'
output_doc_name = 'result.csv'

def write_result(output_doc_name, text):
    with open(output_doc_name, "a") as file:
        file.write(text)


def get_addresses(link):
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    for article in soup.find_all('address', class_='c-address'):
        write_result(output_doc_name, article.text + '\n')


get_addresses(link)
