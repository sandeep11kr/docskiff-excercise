from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from .models import Product


def login_as_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            products = user.product_set.all().values('favorite_fruit')
            return render(request, 'product.html', {'products': products})
        else:
            return render(request, 'error.html', {'message': 'Invalid Credential!'})

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def dashboard(request):
    return render(request, "dashboard.html")


def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            product_objs = [Product(user=user, favorite_fruit=fruit) for fruit in
                            form.cleaned_data.get('favorite_fruit')]
            Product.objects.bulk_create(product_objs)
            login(request, user)
            return redirect("dashboard")
    return render(request, "register.html", {"form": form})


def logout_as_view(request):
    logout(request)
    return redirect("dashboard")
