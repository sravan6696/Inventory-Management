from django.shortcuts import render
import requests
from .models import Book
# from .forms import NewBookForm
import json

# Create your views here.
from django.http import HttpResponse

def home(request):

    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def search(request):

    if request.method == 'POST':

        searchField = request.POST['search']

        results = requests.get('https://www.googleapis.com/books/v1/volumes?q='+searchField)
        
        results = json.loads(results.content)
        finalResults = list()

        for item in results.items():
            # item.authorString = ','.join(item.volumeInfo.authors)
            if item[0] == 'items':
                for book in item[1]:
                    temp = dict()
                    temp['id'] = book['id']

                    if 'volumeInfo' in book and 'title' in book['volumeInfo']:
                        temp['name'] = book['volumeInfo']['title']

                    if 'volumeInfo' in book and 'authors' in book['volumeInfo']:
                        temp['authorString'] = ', '.join(book['volumeInfo']['authors'])

                    finalResults.append(temp)


        return render(request, 'searchResults.html', {'results': finalResults})

    return render(request, 'search.html')


