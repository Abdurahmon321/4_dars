from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category


# Create your views here.


# def index(request):
#     return render(request, "fath/all_products.html")

class IndexListView(ListView):
    model = Category
    template_name = 'fath/all_products.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(parent=None)


def cart(request):
    return render(request, "cart/cart.html")


def shop_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        "product": product
    }
    return render(request, "shop_detail/shop_detail.html", context)


def shop_1(request):
    return render(request, "shop_1/shop.html")


def handler404(request, exception):
    return render(request, '404.html', status=404)

