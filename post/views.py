from django.shortcuts import render, HttpResponse
from .models import  Post

# Create your views here.
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'pirt': posts})


def post_detail(request):
    posts = Post.object.get(id=1);
    return HttpResponse('<b>Bura Post post_detail page</b>')


def post_create(request):
    return HttpResponse('<b>Bura Post post_create page</b>')


def post_update(request):
    return HttpResponse('<b>Bura Post post_update page</b>')


def post_delete(request):
    return HttpResponse('<b>Bura Post post_delete page</b>')