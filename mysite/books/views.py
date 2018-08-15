from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

app_name = 'book'

class IndexView(generic.ListView):
    template_name = 'books/index.html'
 
 
    def get_queryset(self):
        return Book.objects.all()
 
class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type']

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'author', 'price', 'type']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:index')


class DetailView(generic.DetailView):
    model = Book

    template_name = 'books/detail.html'