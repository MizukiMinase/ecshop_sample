from django.shortcuts import render
from django.views.generic import TemplateView


class ProductDetailView(TemplateView):
    template_name = 'shop/product_detail.html'