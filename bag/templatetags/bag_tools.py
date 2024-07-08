from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price_per_item, quantity):
    return quantity * price_per_item
