from django import template

register = template.Library()


@register.filter
def double(price, product):
    try:
        price = float(price)
        amount_in_gram = product.amount_in_gram

        if amount_in_gram != 50:
            return price * 2
        else:
            return price
    except (ValueError, TypeError):
        return price
