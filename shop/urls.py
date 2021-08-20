from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('products', views.ProductListView.as_view(), name='product_list'),
    path('product', views.ProductDetailView.as_view(), name='product_detail')
]