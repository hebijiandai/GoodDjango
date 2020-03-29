# coding:utf-8
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import *
from django.shortcuts import redirect

def main_view(request):
    return redirect('http://zhongmade.com/')

@staff_member_required
def custom_view(request):
    posts = Author.objects.all()
    context = {
        'title': "李金忠's Blog",
        'posts': posts,
    }

    template = 'admin/custom_view.html'
    return render_to_response(template, context,
                              context_instance=RequestContext(request))


@staff_member_required
def nonexist_view(request):
    context = {
        'title': "404 Error Page",
    }
    template = 'admin/404.html'
    return render_to_response(template, context,
                              context_instance=RequestContext(request))
