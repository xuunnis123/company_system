from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.views.generic.edit import FormView
from item_app.models import Item
#from item_app.models import Item
#from . import forms


'''
def index(request):
    code_list=Code.objects.order_by('user')
    date_dict={'access_records':code_list} #mapping to templates/index.html <div>
    
    return render(request,'manage_app/index.html',context=date_dict)

def generate(request,mac_address,datetime):
    datetime=request.POST.get('validate')
    mac_address=request.POST.get('mac_address')
    print("Generate")
    date=datetime.split("-")
    datetime=date[0]+date[1]+date[2]
    content=datetime+mac_address
    encode={"code",encode_rsa(content,mac_address)}

def CodeGen(request):
    if request.method == "POST":
        datetime=request.POST.get('validate')
        mac_address=request.POST.get('mac_address')
        date=datetime.split("-")
        datetime=date[0]+date[1]+date[2]
        content=datetime+mac_address
        print(request.POST.objects.get(pk=pk))
        encode={"code",encode_rsa(content,mac_address)}
        print(encode)
        return render(request,"",encode)

class CodeGenView(CreateView):
    print("CodeGenView")
    fields=('user','validate','mac_address')
    model=models.Code
    template_name='manage_app/code_gen.html'
    #success_url= reverse_lazy("manage_app:create")
    
    def get_success_url(self):
   
        print("test=",self.get_object().id)
        return reverse_lazy('update',kwargs={'pk': self.get_object().id})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def generate(self,request):
        datetime=request.POST.get('validate')
        mac_address=equest.POST.get('mac_address')
        print("datetrime:",datetrime)
        date=datetime.split("-")
        datetime=date[0]+date[1]+date[2]
        content=datetime+mac_address
        encode={"code",encode_rsa(content,mac_address)}
        print(encode)
'''
class ItemListView(ListView):
    print("ItemListView")
    context_object_name='item'
    model= models.Item
    template_name='item_app/item_list.html'

class ItemDetailView(DetailView):
    
    context_object_name='item_detail'
    model=models.Item
    template_name='item_app/item_detail.html'

class ItemCreateView(CreateView):
    fields=('item_name','quantity','unit','price','note')
    model=models.Item
    success_url= reverse_lazy("item_app:list")
class ItemUpdateView(UpdateView):
    fields=('item_name','quantity','unit','price','note')
    model=models.Item
    template_name="item_app/item_form.html"
    success_url= reverse_lazy("item_app:list")
class ItemDeleteView(DeleteView):
    model=models.Item
    success_url= reverse_lazy("item_app:list")

class IndexView(TemplateView):
    template_name='item_app/index.html'
    model=models.Item
    
