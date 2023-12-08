from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blogs


class BlogListView(ListView):
    model = Blogs
    template_name = 'blog/blog.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'blog/blogview.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blogs
    fields = ('title', 'content', 'date_of_creation', 'publication', 'image')
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slag = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blogs
    fields = ('title', 'slag', 'content', 'date_of_creation', 'publication', 'image')
    template_name = 'blog/blog_form.html'
    # success_url = reverse_lazy('blog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slag = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blogview', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blogs
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog')
