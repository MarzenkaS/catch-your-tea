from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tea, Wishlist


@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    teas_in_wishlist = wishlist.teas.all()
    return render(request, 'wishlist.html', {'teas': teas_in_wishlist})


@login_required
def add_to_wishlist(request, tea_id):
    tea = get_object_or_404(Tea, id=tea_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.teas.add(tea)
    return redirect('wishlist')
