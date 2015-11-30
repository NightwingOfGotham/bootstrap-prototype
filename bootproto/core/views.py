from django.shortcuts import render_to_response

def main_view(request):
    if request.method == 'POST':
        print('Method is POST')
    return render_to_response('core/main.html')