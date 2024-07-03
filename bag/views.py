from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
from bag.models import BagItem


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    amount = request.POST.get('product_amount', None)

    if request.user.is_authenticated:
        # Save item to the database for logged-in users
        bag_item, created = BagItem.objects.get_or_create(
            user=request.user,
            product=product,
            amount=amount,
            defaults={'quantity': quantity}
        )
        if not created:
            bag_item.quantity += quantity
            bag_item.save()
        messages.success(request, f'Added {product.name} to your bag')
    else:
        # Use session storage for anonymous users
        bag = request.session.get('bag', {})
        if amount:
            if item_id in bag:
                if amount in bag[item_id]['items_by_amount']:
                    bag[item_id]['items_by_amount'][amount] += quantity
                else:
                    bag[item_id]['items_by_amount'][amount] = quantity
            else:
                bag[item_id] = {'items_by_amount': {amount: quantity}}
        else:
            if item_id in bag:
                bag[item_id] += quantity
            else:
                bag[item_id] = quantity
        request.session['bag'] = bag
        messages.success(request, f'Added {product.name} to your bag')

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    amount = request.POST.get('product_amount', None)

    if request.user.is_authenticated:
        # Update item in the database for logged-in users
        bag_item = get_object_or_404(BagItem, user=request.user, product=product, amount=amount)
        if quantity > 0:
            bag_item.quantity = quantity
            bag_item.save()
        else:
            bag_item.delete()
        messages.success(request, f'Updated {product.name} quantity to {quantity}')
    else:
        # Use session storage for anonymous users
        bag = request.session.get('bag', {})
        if amount:
            if quantity > 0:
                bag[item_id]['items_by_amount'][amount] = quantity
            else:
                del bag[item_id]['items_by_amount'][amount]
                if not bag[item_id]['items_by_amount']:
                    del bag[item_id]
        else:
            if quantity > 0:
                bag[item_id] = quantity
            else:
                del bag[item_id]
        request.session['bag'] = bag
        messages.success(request, f'Updated {product.name} quantity to {quantity}')

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    amount = request.POST.get('product_amount', None)

    if request.user.is_authenticated:
        # Remove item from the database for logged-in users
        bag_item = get_object_or_404(BagItem, user=request.user, product=product, amount=amount)
        bag_item.delete()
        messages.success(request, f'Removed {product.name} from your bag')
    else:
        # Use session storage for anonymous users
        bag = request.session.get('bag', {})
        if amount:
            del bag[item_id]['items_by_amount'][amount]
            if not bag[item_id]['items_by_amount']:
                del bag[item_id]
        else:
            del bag[item_id]
        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from your bag')

    return HttpResponse(status=200)
