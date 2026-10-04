from django.views.generic import ListView, DetailView
from .models import Product, Category, Banner, Promotion


class HomeView(ListView):
    model = Product
    template_name = 'app_store/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.filter(is_active=True)
        context['categories'] = Category.objects.filter(is_active=True)
        context['featured_products'] = Product.objects.filter(is_active=True, is_featured=True)
        context['promotions'] = Promotion.objects.filter(is_active=True)
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'app_store/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'app_store/product_detail.html'
    context_object_name = 'product'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'app_store/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.product_set.filter(is_active=True)
        return context