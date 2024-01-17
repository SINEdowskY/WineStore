from .models import Cart

def cart_context(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(account_id=request.user)
        cart_count = sum(item.amount for item in cart_items)

    return {'cart_count': cart_count}