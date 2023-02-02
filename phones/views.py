from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {"phones": Phone.objects.all().order_by
               ({'name': 'name', 'min_price': 'price', 'max_price': '-price', None: 'id'}[request.GET.get('sort')])}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {"phone": Phone.objects.get(slug=request.get_full_path().split('/')[-2])}
    return render(request, template, context)
