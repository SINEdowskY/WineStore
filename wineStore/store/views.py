from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import RegistrationForm, LoginForm, ClientForm, OrderForm
from .models import Client, Order, Wine, Cart, WineOrder

# WINES

def mainPage(request):
    context = {}
    return render(request, "mainPage.html", context)


def winePage(request, wine_type):
    context = {}
    wines = get_list_or_404(Wine, type=wine_type)
    context['wine_type'] = wine_type
    context['wines'] = wines
    return render(request, "winePage.html", context)

def detailWinePage(request, wine_id):
    wine_details = get_object_or_404(Wine, id=wine_id)
    context = {}
    context["wine_details"] = wine_details
    return render(request, "detailWinePage.html", context=context)

# ACCOUNT
def registerPage(request):
    context = {}
    context["form"] = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "registerPage.html", context)

def loginPage(request):
    alert = ""
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"Użytkownik {username} zalogował się")
                return redirect('main')
            else:
                messages.error(request, "Błędne dane logowania !")
                return redirect('login')
        else:
            messages.error(request, "Błędne dane logowania !")
            return redirect('login')
    else:
        context = {}
        context["form"] = LoginForm()
        context["alert"] = alert
        return render(request, "loginPage.html", context)

@login_required
def accountPage(request):
    context = {}
    clients = Client.objects.filter(account_id = request.user.id)
    orders = Order.objects.filter(account_id = request.user.id).order_by("-id")
    context["username"] = request.user.username
    context["clients"] = clients
    context["orders"] = orders
    return render(request, "accountPage.html", context)

@login_required
def addClientPage(request):
    if request.method == "POST":
        model = Client()
        form = ClientForm(request.POST)
        if form.is_valid():
            model.account_id = request.user
            model.first_name = form.cleaned_data["first_name"]
            model.last_name = form.cleaned_data["last_name"]
            model.date_of_birth = form.cleaned_data["date_of_birth"]
            model.address_street = form.cleaned_data["address_street"]
            model.address_number = form.cleaned_data["address_number"]
            model.address_apartament_number = form.cleaned_data["address_apartament_number"]
            model.zip_code = form.cleaned_data["zip_code"]
            model.phone_number = form.cleaned_data["phone_number"]
            
            model.save()
        
            return redirect("account")
        else:
            print(form.errors)
            return redirect("add_client")

    else:
        context = {}
        context["form"] = ClientForm()
        context["is_to_add"] = True
        return render(request, "addClientPage.html", context)

def editClientPage(request, client_id):
    context = {}
    client = get_object_or_404(Client, id=client_id, account_id=request.user)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("account")
    else:
        form = ClientForm(instance=client)
        context["form"] = form
        context["client_id"] = client.id
        context["is_to_add"] = False
    
    return render(request, "addClientPage.html", context)

@login_required
def logoutView(request):
    print(f"Użytkownik {request.user.username} wylogował się")
    logout(request)
    return redirect("main")


# ORDERING
def CartView(request):
    context = {}
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(account_id = request.user)
        context["cart_items"] = cart_items
        context["cart_value"] = sum([item.wine_id.price*item.amount for item in cart_items])
        return render(request, 'cartPage.html', context)
    else:
        return redirect("login")

def addToCartView(request, wine_id):
    context = {}
    if request.user.is_authenticated:
        cart_item, created = Cart.objects.get_or_create(
            account_id = request.user,
            wine_id = Wine.objects.get(id=wine_id)
        )
        if not created:
            cart_item.amount += 1
            cart_item.save()
        else:
            print(f"Użytkownik {request.user.username} dodal do koszyka")

        return redirect("main")
    else:
        return redirect("login")

@login_required
def decrementCartItem(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, id=cart_item_id)
        if cart_item.amount == 1:
            cart_item.delete()
        else:
            cart_item.amount -= 1
            cart_item.save()
        return redirect('cart_view')
    else:
        return redirect("login")

@login_required
def incrementCartItem(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, id=cart_item_id)
        if cart_item.amount < cart_item.wine_id.storage_amount:
            cart_item.amount += 1
            cart_item.save()
        return redirect('cart_view')
    else:
        return redirect("login")

@login_required
def removeCartItem(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, id=cart_item_id)
        cart_item.delete()
        return redirect('cart_view')
    else:
        return redirect("login")

@login_required
def CheckoutPage(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            cart_wines = Cart.objects.filter(account_id = request.user)
            cart_value = sum([item.wine_id.price*item.amount for item in cart_wines])
            
            order_model = Order()
            order_model.client_id = form.cleaned_data["client_id"]
            order_model.account_id = request.user
            order_model.order_value = cart_value
            order_model.shipment = form.cleaned_data["shipment"]
            order_model.save()

            for cart_wine in cart_wines:
                cart_wine.wine_id.storage_amount -= 1
                wine_order_model = WineOrder()
                wine_order_model.wine = cart_wine.wine_id
                wine_order_model.order = order_model
                cart_wine.wine_id.save()
                wine_order_model.save()
            
            cart_wines.delete()
            return redirect("main")
    else:
        context = {}
        context["form"] = OrderForm()
        context["cart_items"] = Cart.objects.filter(account_id = request.user)
        context["cart_value"] = sum([item.wine_id.price*item.amount for item in context["cart_items"]])
        return render(request, "checkoutPage.html", context)

@login_required
def detailOrderPage(request, order_id):
    context = {}
    context["order"] = get_object_or_404(Order, id=order_id)
    context["order_item"] = get_list_or_404(WineOrder, order=order_id)
    return render(request, "detailOrderPage.html", context)