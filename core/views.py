from django.shortcuts import get_object_or_404, render
from crud.models import Pizza
from crud.models import Chef
from crud.models import Post
from crud.models import Contenido
from crud.models import MasaDisp
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
    containList=Contenido.objects.all()
    doughList=MasaDisp.objects.all()
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    return render(request,"core/menu.html",{'myPizzas':myPizzas,'containList':containList,'doughList':doughList})


def contained(request,contain_id):
    containList=Contenido.objects.all()
    doughList=MasaDisp.objects.all()
    thisContain=get_object_or_404(Contenido,id=contain_id)
    pizzaList=Pizza.objects.filter(Contain=thisContain)
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    return render(request,"core/menufiltered.html",{'myPizzas':myPizzas,'filter':thisContain,'containList':containList,'doughList':doughList})

def doughType(request,dough_id):
    containList=Contenido.objects.all()
    doughList=MasaDisp.objects.all()
    thisDough=get_object_or_404(MasaDisp,id=dough_id)
    pizzaList=Pizza.objects.filter(dough=thisDough)
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    return render(request,"core/menufiltered.html",{'myPizzas':myPizzas,'filter':thisDough,'containList':containList,'doughList':doughList})


"""def services(request):
    pizzaList=Pizza.objects.all()
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    return render(request,"core/services.html",{'myPizzas':myPizzas})"""