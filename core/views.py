from django.shortcuts import render
from crud.models import Pizza
from crud.models import Chef
from crud.models import Post
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    blogList=Post.objects.all()
    paginator=Paginator(blogList,3)
    pageNumber=request.GET.get("page")
    myBlogPosts=paginator.get_page(pageNumber)
    return render(request,"core/index.html",{'myBlogPosts':myBlogPosts})

def about(request):
    chefList=Chef.objects.all()
    paginator=Paginator(chefList,4)
    pageNumber=request.GET.get("page")
    myChefs=paginator.get_page(pageNumber)
    return render(request,"core/about.html",{'myChefs':myChefs})

def blogsingle(request):
    chefList=Chef.objects.all()
    paginator=Paginator(chefList,3)
    pageNumber=request.GET.get("page")
    mychefs=paginator.get_page(pageNumber)
    return render(request,"core/blog-single.html",{'Chefs':mychefs})

def blog(request):
    blogList=Post.objects.all()
    paginator=Paginator(blogList,6)
    pageNumber=request.GET.get("page")
    myBlogPosts=paginator.get_page(pageNumber)
    return render(request,"core/blog.html",{'myBlogPosts':myBlogPosts})

def contact(request):
    return render(request,"core/contact.html")

def menu(request):
    pizzaList=Pizza.objects.all()
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    return render(request,"core/menu.html",{'myPizzas':myPizzas})

"""def services(request):
    pizzaList=Pizza.objects.all()
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    return render(request,"core/services.html",{'myPizzas':myPizzas})"""