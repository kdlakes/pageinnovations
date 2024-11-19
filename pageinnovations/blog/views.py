from django.shortcuts import render
from .models import BlogPost
from .models import Product
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import ContactMessage

from django.shortcuts import get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home(request):
    products = Product.objects.order_by('-created_at')[:3]
    posts = BlogPost.objects.order_by('-created_date')[:3]
    context = {
        'products' : products,
        'posts' : posts
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def blog(request):
    posts_list = BlogPost.objects.all().order_by('-created_date')
    paginator = Paginator(posts_list, 2)  # Show 5 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, 'pages/blog.html', context)


def contact(request):
    return render(request, 'pages/contact.html')

def shop(request):
    products_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator( products_list, 3)  # Show 5 posts per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }
    return render(request, 'pages/shop.html', context)

def cart(request):
    return render(request, 'pages/cart.html')

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    
    context = {
        'post': post
        }
    return render(request, 'pages/blog-details.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    
    context = {
        'product': product
        }
    return render(request, 'pages/shop-detail.html', context)














# Create your views here.
