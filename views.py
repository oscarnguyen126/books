from django.shortcuts import render
from .models import Book
from django.http import JsonResponse


def list(request):
    books = [b.to_dict() for b in Book.objects.all()]
    return JsonResponse({'books': books})
