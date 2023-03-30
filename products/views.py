import products

from django.shortcuts import render, redirect

import products
from Shop4m.form import ProductCreateForm, CommentsCreateForm
from products.models import Products ,Comment


# Create your views here.
def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Products.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)

        context = {
            "product":product,
            "comments" :product.comment_set.all()
        }

        return render(request , 'products/detail.html' ,context=context)



def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm,
        }

        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form= ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Products.objects.create(
                title=form.cleaned_data.get('title'),
                rate=form.cleaned_data.get('rate'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                image=form.cleaned_data.get('image')
            )
            return redirect("/products/")
        return render(request, 'products/create.html', context={'form':form})


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'comments': product.comment_set.all(),
            'form': CommentsCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Products.objects.get(id=id)
        data = request.POST
        form = CommentsCreateForm(data=data)


        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                product=product

            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)




