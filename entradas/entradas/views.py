from django.shortcuts import render

def menu_inicial(requests):

    return render(requests, template_name='casa.html')


def entradas(requests):
    if requests.method=='POST':
        return render(requests, 'gracias_entradas.html')
        
    return render(requests, template_name='entradas.html')
    

def contacto(request):

    if request.method=='POST':
        return render(request, 'gracias.html')

    return render(request, template_name='contacto.html')