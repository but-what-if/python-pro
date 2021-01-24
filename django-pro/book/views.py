from django.shortcuts import render
from django.http import HttpResponse

from book.models import Book
from book.models import Author


def book_list(request):

    response_content = ''

    for book in Book.objects.all():  # Book.objects.all() - SELECT * FROM books_book;
        response_content += f'ID: {book.id}, Author: {book.author} <br/>'

    return HttpResponse(response_content)



def author_list(request):

    response_content = ''

    for author in Author.objects.all():
        response_content += f'ID: {author.id}, Author: {author.first_name} {author.last_name}, Date: {author.date_of_birth} - {author.date_of_death or "n.d."}, Country: {author.country}, Gender: {author.gender}, Language: {author.native_language}  <br/>'

    return HttpResponse(response_content)

