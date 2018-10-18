from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse


def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
        # new_item_text = request.POST['item_text']
        # Item.objects.create(text=new_item_text)

    # else:
    #     new_item_text = ''

    items = Item.objects.all()
    return render(request,'home.html', {'items': items})
