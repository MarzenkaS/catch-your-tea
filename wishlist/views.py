from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Wishlist
from products.models import Product
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


@login_required
def wishlist_view(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        products = wishlist.products.all()
    except Wishlist.DoesNotExist:
        products = []

    context = {
        'products': products,
    }
    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, product_id):
    if not request.user.is_authenticated:
        messages.info(request, "You need to log in or register to add products to your wishlist.")
        return redirect('login')  # Redirect to your login page

    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    # Check if the product is already in the wishlist
    if product in wishlist.products.all():
        messages.info(request, f"{product.name} is already in your wishlist.")
    else:
        wishlist.products.add(product)
        messages.success(request, f"{product.name} has been added to your wishlist.")

    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        # Update the redirect to match your actual wishlist view name or URL pattern name
        return redirect('wishlist')  # Update 'wishlist' to the correct name
    else:
        return HttpResponseForbidden("You do not have permission to remove this item from your wishlist.")
