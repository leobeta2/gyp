# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Producto


from io import BytesIO 
from reportlab.pdfgen import canvas


def index(request):
    productos = Producto.objects.order_by('p_neto')
    return render_to_response('productos.html', {'productos': productos})


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle.html', {'producto': producto})
"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

"""

def convertir_pdf(request, pk): 
    # Obtenemos un queryset, para un determinado libro usando pk. 
    try: 
        producto = Producto.objects.get(id=pk) 
    except ValueError: # Si no existe llamamos a "pagina no encontrada". 
        raise Http404() 
    # Creamos un objeto HttpResponse con las cabeceras del PDF correctas. 
    response = HttpResponse(content_type='application/pdf') 
    # Nos aseguramos que el navegador lo abra directamente. 
    response['ContentDisposition'] = 'filename="archivo.pdf"' 
    buffer = BytesIO() 
    # Creamos el objeto PDF, usando el objeto BytesIO como si fuera un "archivo". 
    p = canvas.Canvas(buffer) 
    # Dibujamos cosas en el PDF. Aquí se genera el PDF. 
    # Consulta la documentación para una lista completa de funcionalidades. 
    p.roundRect(0, 750, 694, 120, 20, stroke=0, fill=1) 
    #p.setFont('Times­Bold',32) 
    p.setFillColorRGB(1,1,1) 
    p.drawString(100, 800, str(producto.nombre))#Obtenemos el titulo de un libro y la portada. 
    p.drawImage(str(producto.imagen.url), 100, 100, width=400, height=600) 
    # mostramos y guardamos el objeto PDF. 
    p.showPage() 
    p.save() 
    # Traemos el valor del bufer BytesIO y devolvemos la respuesta. 
    pdf = buffer.getvalue() 
    # Cerramos el bufer 
    buffer.close() 
    response.write(pdf) 
    return response