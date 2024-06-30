from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Wishlist
from products.models import Product


def wishlist_view(request):
    wishlist = Wishlist.objects.get(user=request.user)
    teas = wishlist.products.all()
    context = {
        'teas': teas,
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    tea = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if tea in wishlist.teas.all():
        wishlist.teas.remove(tea)
        return redirect('wishlist')
    else:
        return HttpResponseForbidden("You do not have permission to remove this item from your wishlist.")
