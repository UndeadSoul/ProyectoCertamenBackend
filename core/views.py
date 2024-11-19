from django.shortcuts import get_object_or_404, render
from crud.models import Pizza
from crud.models import Chef
from crud.models import Post
from crud.models import Contenido
from crud.models import MasaDisp
from django.core.paginator import Paginator

# Create your views here.
# Primera Evaluación
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

#Segunda evaluación
def menu(request):
    #Se obtienen todos los objetos
    pizzaList=Pizza.objects.all()
    #Se obtienen todos los tipos de contenido
    containList=Contenido.objects.all()
    #Se obtiene una lista de todos los tipos de masa
    doughList=MasaDisp.objects.all()
    #Paginator separa las pizzas en conjuntos de 4
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    #Regresa un render con el archivo html y un diccionario con listas que se utilizarán en la página
    return render(request,"core/menu.html",{'myPizzas':myPizzas,'containList':containList,'doughList':doughList})

def contained(request,contain_id):
    #Se obtiene una lista de los objetos contain
    containList=Contenido.objects.all()
    #Se obtiene una lista de los objetos masa
    doughList=MasaDisp.objects.all()
    #Asegura que haya una pagina a pesar de que no exista
    thisContain=get_object_or_404(Contenido,id=contain_id)
    #Aplica un filtro a las pizzas en base a lo que contiene
    pizzaList=Pizza.objects.filter(Contain=thisContain)
    #Paginator separa las pizzas en conjuntos de 4
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    #Regresa un render con el archivo html y un diccionario con listas que se utilizarán en la página filtradas y con el filtro usado
    return render(request,"core/menufiltered.html",{'myPizzas':myPizzas,'filter':thisContain,'containList':containList,'doughList':doughList})

def doughType(request,dough_id):
    #Lo mismo de arriba pero filtrado por tipo de masa
    containList=Contenido.objects.all()
    doughList=MasaDisp.objects.all()
    thisDough=get_object_or_404(MasaDisp,id=dough_id)
    pizzaList=Pizza.objects.filter(dough=thisDough)
    paginator=Paginator(pizzaList,4)
    pageNumber=request.GET.get("page")
    myPizzas=paginator.get_page(pageNumber)
    return render(request,"core/menufiltered.html",{'myPizzas':myPizzas,'filter':thisDough,'containList':containList,'doughList':doughList})
