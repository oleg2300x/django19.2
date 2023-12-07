from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

class ProdDetailView(DetailView):
    model = Product
    template_name = 'catalog/prod_info.html'
    context_object_name = 'product'


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        print(f"{name}, ({email}) says: {subject}\n{message}")
    return render(requests, 'catalog/contacts.html')
