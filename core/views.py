# -*-coding: utf-8-*-
from blog.models import Category, BlogPost, TourPost, Post
from mediastorage.models import ImageStorage, FileStorage
from pages.models import Page
from partners.models import Partner
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from endless_pagination.decorators import page_template

def index(request):
    return render_to_response('index.html',{
        'post' : Post.objects.all()[:4],
    })

@page_template("archive_page.html")
def view_category(request, slug, template="cat.html", extra_context=None):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category' : category,
        'post' : Post.objects.filter(category=category),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))


def view_tour(request, slug):
    return render_to_response('post.html',{
        'post' : get_object_or_404(TourPost, slug=slug),
    })

@page_template("archive_page.html")
def view_tours(request, template='all_tours.html', extra_context=None):
    # category = get_object_or_404(Category, slug=slug)
    context = {
        'post' : Post.objects.all(),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

def view_blog(request, slug):
    return render_to_response('post.html',{
        'post' : get_object_or_404(BlogPost, slug=slug),
    })

def view_page(request, slug):
    return render_to_response('page.html',{
        'post' : get_object_or_404(Page, slug=slug),
    })

def view_partners(request):
    return render_to_response('partners.html',{
        'partners' : Partner.objects.all(),
    })