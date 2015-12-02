from django.shortcuts import render_to_response, render
from django.views.generic import (
    TemplateView,
)

from bootproto.core.context import context_dict
from bootproto.core.navbar import navbar

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


class NavHeaderMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(NavHeaderMixin, self).get_context_data(**kwargs)
        ctx['navbar'] = navbar
        return ctx


class BootprotoTemplateView(NavHeaderMixin, TemplateView):
    pass


class Main5View(BootprotoTemplateView):
    template_name = 'core/main4.html'