from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Items
from django.urls import reverse

def index(request):
    my_items = Items.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'my_items': my_items,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add_item.html')
    return HttpResponse(template.render({},request))

def add_item(request):
    x = request.POST['name']
    y = request.POST['description']
    z = request.POST['vendor']
    q = request.POST['stock']
    item = Items(item_name=x,item_desc=y,vendor_name=z,item_stock=q )
    item.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    item = Items.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    my_items = Items.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'my_items': my_items,
    }
    return HttpResponse(template.render(context, request))

def update_item(request, id):
    name = request.POST['name']
    desc = request.POST['description']
    vendor = request.POST['vendor']
    stock = request.POST['stock']
    item = Items.objects.get(id=id)
    item.item_name = name
    item.item_desc = desc
    item.vendor_name = vendor
    item.item_stock = stock
    item.save()
    return HttpResponseRedirect(reverse('index'))

def sell(request):
    my_items = Items.objects.all().values()
    template = loader.get_template('sale.html')
    context = {
        'my_items': my_items,
    }
    return HttpResponse(template.render(context, request))

def sell_item(request):
    quantity = request.POST['quantity']
    item = request.POST['item']
    item =Items.objects.get(id=item)
    newStock = int(item.item_stock) - int(quantity)
    item.item_stock = str(newStock)
    item.save()
    return HttpResponseRedirect(reverse('index'))
