from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]#0:3] means we want to show 3 items from the list of related items that we have filtered

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()#if the request is not a POST request, we will create a new instance of the NewItemForm class and pass it to the template means the user will see a blank form means the user will see a blank form to fill out and submit

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):#one cas submit;two cas get
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)#else if the request is not a POST request, we will create a new instance of the EditItemForm class and pass it to the template means the user will see a form filled with the item's current data if we dont do that when the user clicks on the edit button, they will see a blank form to fill out and submit because we are not passing the instance of the item to the form and we mean by else when the user clicks on the edit button, they will see a form filled with the item's current data the other case is when the user submits the form, we will create a new instance of the EditItemForm class and pass it to the template

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')