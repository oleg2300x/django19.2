import datetime

from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        for object in context['product_list']:
            active_version = Version.objects.filter(product=object, is_active=True).last()
            if active_version:
                object.active_version_number = active_version.version_number
                object.version_name = active_version.version_name
            else:
                object.active_version_number = None
        return context


class ProdDetailView(DetailView):
    model = Product
    template_name = 'catalog/prod_info.html'
    context_object_name = 'product'


class ProdCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProdUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = version_formset(self.request.POST, instance=self.object)
        else:
            formset = version_formset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.last_modified_date = datetime.datetime.now()
        self.object.save()
        return self.object


class ProdDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        print(f"{name}, ({email}) says: {subject}\n{message}")
    return render(requests, 'catalog/contacts.html')
