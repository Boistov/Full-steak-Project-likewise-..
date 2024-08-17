from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from .forms import MenuItemForm
from .models import MenuItem, Category, OrderModel


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class Aboute(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/aboute.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order.html')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()
        context = {'menu_items': menu_items}
        return render(request, 'customer/menu.html', context)

class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )
        context = {'menu_items': menu_items}
        return render(request, 'customer/menu.html', context)

class MenuCreate(View):
    def get(self, request, *args, **kwargs):
        form = MenuItemForm()
        return render(request, 'customer/menu_item_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
        return render(request, 'customer/menu_item_form.html', {'form': form})

class MenuUpdate(View):
    def get(self, request, pk, *args, **kwargs):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        form = MenuItemForm(instance=menu_item)
        return render(request, 'customer/menu_item_form.html', {'form': form})

    def post(self, request, pk, *args, **kwargs):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('menu')
        return render(request, 'customer/menu_item_form.html', {'form': form})

class MenuDelete(View):
    def post(self, request, pk, *args, **kwargs):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        menu_item.delete()
        return redirect('menu')


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/dashboard.html') 