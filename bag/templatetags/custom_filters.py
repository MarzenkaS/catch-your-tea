from django import template

register = template.Library()


@register.filter
def conditional_double(price, amount):
    try:
        price = float(price)
        amount = int(amount)
        if amount == 100:  # Check if the amount is 100
            return price * 2
        return price
    except (ValueError, TypeError):
        return price
