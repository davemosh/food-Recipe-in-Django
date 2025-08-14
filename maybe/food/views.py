from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your list function based views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)

class IndexClassView(ListView):
    model = Item
    template_name ='food/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse('this is just a response')

#Here is the detials of each food link page, if its coming from the database you should use the context theory
def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/details.html', context)


class FoodDetails(DetailView):
    model = Item
    template_name = 'food/details.html'



#This is form special for submitting to the database
def create_item(request):
    form = ItemForm(request.POST or None)
#checking if the form is valid answers
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})
 

#this is a class based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'


    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


#This is for updating the item in the database
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
#checking if the form is valid answers and passing its id to make change
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html',{'form':form,'item':item})

#deleting the item by getting their id
def delete_item(request,id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',{'item':item})


