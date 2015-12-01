from django.shortcuts import render_to_response, render

from bootproto.core.context import context_dict

def main_view(request):
    if request.method == 'POST':
        print('Method is POST')
    return render_to_response('core/main.html')

def main_view3(request):
    if request.method == 'POST':
        print('Method is POST')
    return render_to_response('core/main3.html')

def main_view4(request):
    if request.method == 'POST':
        print('Method is POST')

    return render(request, template_name='core/main4.html', context=context_dict)