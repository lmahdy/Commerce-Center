from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from item.models import Item

# Create your views here.
@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)#we are filtering the items based on the user who created them

    return render(request, 'dashboard/index.html', {
        'items': items
    })#we are passing the items to the template so that we can display them in the dashboard
