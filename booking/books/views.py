from django.shortcuts import render

# Create your views here.

def books(request):

    category = {
        'category1': 'romance',
        'category2': 'comedy',
        'category3': 'Mystery',
        'category4': 'Thriller',
        'category5': 'Sci-fi',
        'category6': 'Kids',
        'category7': 'Adventure',
        'category8': 'Comics',
        'category9': 'Fantasy',
        'category10': 'classics',
        'category11': 'Shorts',
        'category12': 'Mystery'
    }

    return render(request,'books.html', category)

