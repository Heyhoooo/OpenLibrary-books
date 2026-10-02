import requests
import csv

url = "https://openlibrary.org/search.json"
params = {
    'q':'technology',
    'limit': 50
}
response = requests.get(url, params=params)
data = response.json()

# print((data['docs'])[1]['author_name'])

def books_after_2000():
    books_list = []
    for book in data['docs']:
    #     for k,v in book.items():
    #         if k == 'first_publish_year' and v > 2000:
    #             books_list.append({'author_name':book['author_name'],'first_publish_year':book['first_publish_year'],'title':book['title']})
    # return books_list
        year = book.get('first_publish_year')
        author_names = book.get('author_name')
        title = book.get('title')

        if year is None or author_names is None or title is None:
            continue
        
        author = ', '.join(author_names)
        if year > 2000:
            books_list.append({'Author':author,'Year':year,'Title':title})
    
    # num = len(books_list)

    return books_list 


books_in_order = sorted(books_after_2000(), key = lambda book:book['Year'])


with open('books_in_order.csv', 'w', newline='') as final_file:
    writer = csv.DictWriter(final_file, fieldnames = ['Author', 'Year', 'Title'])
    writer.writeheader()
    writer.writerows(books_in_order)


