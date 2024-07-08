from decimal import Decimal
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    amount = None

    # Check if there's a selected amount (e.g., 50g, 100g)
    if 'product_amount' in request.POST:
        amount = int(request.POST['product_amount'])

    bag = request.session.get('bag', {})

    # Calculate the price based on the selected amount or default (50g)
    if amount:
        price_per_item = product.get_price_for_amount(amount)
    else:
        price_per_item = product.price  # Default price for 50g

    # Convert price_per_item to float for JSON serialization
    price_per_item_float = float(price_per_item)

    # Determine which price_per_item to store in the bag
    item_price_per_item = price_per_item_float if amount else float(product.price)

    # If the item already exists in the bag
    if item_id in bag:
        if amount:
            if amount in bag[item_id].get('items_by_amount', {}):
                bag[item_id]['items_by_amount'][amount] += quantity
                messages.success(request, f'Updated amount {amount}g {product.name} quantity to {bag[item_id]["items_by_amount"][amount]}')
            else:
                bag[item_id]['items_by_amount'][amount] = quantity
                messages.success(request, f'Added amount {amount}g {product.name} to your bag')
        else:
            bag[item_id]['quantity'] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]["quantity"]}')
    else:
        if amount:
            bag[item_id] = {'items_by_amount': {amount: quantity}, 'price_per_item': item_price_per_item}
            messages.success(request, f'Added amount {amount}g {product.name} to your bag')
        else:
            bag[item_id] = {'quantity': quantity, 'price_per_item': item_price_per_item}
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    amount = None
    if 'product_amount' in request.POST:
        amount = request.POST['product_amount']
    bag = request.session.get('bag', {})

    if amount:
        if quantity > 0:
            bag[item_id]['items_by_amount'][amount] = quantity
            messages.success(request, f'Updated amount {amount.upper()} {product.name} quantity to {bag[item_id]["items_by_amount"][amount]}')
        else:
            del bag[item_id]['items_by_amount'][amount]
            if not bag[item_id]['items_by_amount']:
                bag.pop(item_id)
            messages.success(request, f'Removed amount {amount.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        amount = None
        if 'product_amount' in request.POST:
            amount = request.POST['product_amount']
        bag = request.session.get('bag', {})

        if amount:
            del bag[item_id]['items_by_amount'][amount]
            if not bag[item_id]['items_by_amount']:
                bag.pop(item_id)
            messages.success(request, f'Removed amount {amount.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
