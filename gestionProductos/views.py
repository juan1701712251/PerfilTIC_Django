from django.shortcuts import render
from gestionProductos.models import Category

# Create your views here.
def categories(request):
    cat = Category.objects.all()
    context = {'Categories':cat}
    #Abrir plantilla
    #doc = loader.get_template('inicio.htm')
    #documento = doc.render({'variable':var1})

    return render(request,'categories.htm',context)