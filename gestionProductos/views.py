from django.shortcuts import render
from gestionProductos.models import Category, Product
import requests

# Create your views here.
def categories(request,idC=None):
    Pro = None
    context = {}
    if idC is not None:
        Pro = Product.objects.filter(category_id = idC)
    cat = Category.objects.all().order_by('parentCategory')
    context["Categories"]=cat
    context["Products"]=Pro

    url= 'http://api.currencylayer.com/live?access_key=405e0a2e943e4174df8bb5881800e101&currencies=USD,AUD,CAD,PLN,MXN&format=1'
    response = requests.get(url)
    if(response.status_code == 200):
        print(response.json()["quotes"])
        quote = response.json()["quotes"]["USDMXN"] #Diccionario
        if Pro:
            for p in Pro:
                p.prize = p.prize*quote

    #Abrir plantilla
    #doc = loader.get_template('inicio.htm')
    #documento = doc.render({'variable':var1})

    return render(request,'categories.htm',context)

def products(request,idC):
    Pro = Product.objects.filter(category_id = idC)
    context = {'Products':Pro}

    
    #Abrir plantilla
    #doc = loader.get_template('inicio.htm')
    #documento = doc.render({'variable':var1})

    return render(request,'products.htm',context)