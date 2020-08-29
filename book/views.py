from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from book.models import Publisher
from book.models import Author


class PublisherList(ListView):
    model = Publisher
    template_name = 'book/publisher_list_page.html'
    context_object_name = 'publisher_list'


class AuthorList(ListView):
    model = Author
    template_name = 'book/author_list_page.html'
    context_object_name = 'author_list'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'book/author_details.html'
    context_object_name = 'author'
