from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from bag.models import BagItem


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    if request.user.is_authenticated:
        # Fetch bag items from the database for logged-in users
        bag_items_db = BagItem.objects.filter(user=request.user)
        for item in bag_items_db:
            total += item.quantity * item.product.price
            product_count += item.quantity
            bag_items.append({
                'item_id': item.product.id,
                'quantity': item.quantity,
                'product': item.product,
                'amount': item.amount,
            })
    else:
        # Fall back to session storage for anonymous users
        bag = request.session.get('bag', {})
        for item_id, item_data in bag.items():
            product = get_object_or_404(Product, pk=item_id)
            if isinstance(item_data, int):
                total += item_data * product.price
                product_count += item_data
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                })
            else:
                for amount, quantity in item_data['items_by_amount'].items():
                    total += quantity * product.price
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'amount': amount,
                    })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
