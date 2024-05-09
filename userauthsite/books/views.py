from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import Book


# Create your views here.
@require_GET
def book_search(request):
    try:
        books = Book.objects.filter(genre="Thriller")[:5]
        books_data = []

        # Iterate over each book to extract its details
        for book in books:
            books_data.append({
                'title': book.title,
                'book_description': book.book_description,
                'year': book.year,
                'buy_amount': book.buy_amount,
                'rent_amount': book.rent_amount,
                'stock': book.stock
            })

        # Return the list of book details as JSON response
        return JsonResponse({'books': books_data})

    except:
        return JsonResponse({'error': 'Book genre does not exist'}, status=404)