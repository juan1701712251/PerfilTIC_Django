from django.http import HttpResponse
from django.template import loader
from django.template import Template, Context
from django.shortcuts import render

def inicio(request):
    var1 = 'Juan Sebastián'
    #Abrir plantilla
    #doc = loader.get_template('inicio.htm')
    #documento = doc.render({'variable':var1})

    return render(request,'inicio.htm',{'variable':var1})

