import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, MProductForm
from catalog.models import Product, Version


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ProdDetailView(DetailView):
    model = Product
    template_name = 'catalog/prod_info.html'
    context_object_name = 'product'


class ProdCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProdUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    permission_required = 'catalog.change_product'

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

        if (self.request.user != self.object.owner
                and not self.request.user.is_superuser
                and self.request.user.has_perm('catalog.product_published')):
            raise Http404
        return self.object

    def get_form_class(self):
        if self.request.user.has_perm('catalog.product_published'):
            return MProductForm
        return Http404


class ProdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

    def test_func(self):
        return self.request.user.is_superuser


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        print(f"{name}, ({email}) says: {subject}\n{message}")
    return render(requests, 'catalog/contacts.html')
