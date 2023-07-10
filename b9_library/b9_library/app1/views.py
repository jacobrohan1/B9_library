from django.shortcuts import render, HttpResponse, redirect
from .models import Book
# Create your views here.

def welcome_page(request):
    return render(request, 'views.html')

def show_books(request):
    books = Book.objects.all
    return render(request, 'show_books.html', {'all_books' : books})

def show_single_books(request, id):
    try:
        book_object = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse('Book Does not Exist')
    return render(request, 'bookdetail.html', context = {'book': book_object})

def add_books(request):
    if request.method == 'POST':
        final_dict = request.POST
       
        book_name = final_dict.get('nm')
        book_price = final_dict.get('prc')
        book_qty = final_dict.get('qty')
        book_ispub = final_dict.get('ispub')
        book_isactive = final_dict.get('isact')

        if book_ispub == 'Yes':
            book_ispub = True
        else:
            book_ispub = False  

        if book_isactive == 'Yes':
            book_isactive = True
        else:
            book_isactive = False

        Book.objects.create(name = book_name, price = book_price, qty =book_qty, is_published = book_ispub, is_active= book_isactive )
        return redirect('show_books') 


    elif request.method == 'GET':
        return render(request, 'addbook.html')

        