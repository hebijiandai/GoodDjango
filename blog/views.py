#coding:utf-8
# from django.shortcuts import render
#
# from django.template import loader, Context
# from django.http import HttpResponse
# from blog.models import *
# from django.contrib.admin.views.decorators import staff_member_required
#
#
# @staff_member_required
# def custom_view(request):
#     posts = Author.objects.all()
#     t = loader.get_template('admin/custom_view.html')
#     c = Context({'posts': posts})
#     return HttpResponse(t.render(c))


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import *


@staff_member_required
def custom_view(request):
    posts = Author.objects.all()
    context = {
        'title': "AllenLee's Blog",
        'posts': posts,
    }

    template = 'admin/custom_view.html'
    return render_to_response(template, context,
                              context_instance=RequestContext(request))


@staff_member_required
def nonexist_view(request):
    return render_to_response('admin/404.html', {'title': '404 ERROR TIPS'},
                              context_instance=RequestContext(request))