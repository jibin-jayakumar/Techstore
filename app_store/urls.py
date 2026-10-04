from django.urls import path
from . import views

app_name = 'app_store'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
]