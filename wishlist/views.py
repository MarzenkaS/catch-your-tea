from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tea, Wishlist


@login_required
def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    teas_in_wishlist = wishlist.teas.all()
    return render(request, 'wishlist.html', {'teas': teas_in_wishlist})
