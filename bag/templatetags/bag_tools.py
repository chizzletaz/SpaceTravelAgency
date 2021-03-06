from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, item_data):
    if isinstance(item_data, int):
        total = price * item_data
    else:
        total = price * item_data['quantity']
    return total
