Instalación miniconda-------------
1. Desinstalar python
2. descargar miniconda (https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
3. instalar miniconda (just me/checkbox "not recomended" sobre el path)
Crear ambiente--------------------
1. cmd-> conda create <nombreambiente> python
2. cmd-> conda activate <nombreambiente>
3. cmd-> conda install django
Crear un proyecto-----------------
1. crear una carpeta de proyecto
2. copiar la ruta de proyecto
3. cmd-> cd <rutadeproyecto>
4. cmd-> django-admin startproyect <nombreproyecto>
5. cmd-> cd <nombreproyecto>
Ejecutar proyecto-----------------
1. cmd-> python manage.py runserver (copiar el host e ir al navegador)
2. cmd-> python manage.py migrate
Crear aplicacion------------------
1. cmd-> python manage.py startapp <nombredeaplicacion> (la primera app se debe llamar core)
Hacer setup de la pagina----------
1. crear la carpeta templates>core en core para los archivos html
2. crear la carpeta static>core en core para las carpetas assets/css/js
3. crear los metodos del archivo views.py en core para mostrar los archivos html
    def <nombrehtml>(request):
        return render(request,"core/<nombrehtml>.html") 
4. agregar el urlpattern a el archivo urls.py
    path('',views.nombreMetodo, name='nombreMetodo')
5. agregar al listado de aplicaciones 
    'core'
6. añadir base.html para usar como pagina base
7. verificar que el env del editor sea el correcto
----------------------------------
1. python manage.py createsuperuser
2. ingresar credenciales
3. crear models
4. python manage.py makemigrations <nombredeaplicacion>
5. python manage.py migrate <nombredeaplicacion>
---------------------------------
1. conda install pillow
2. en settings agregar
    import os
    MEDIA_URL='/media/'
    MEDIA_ROOT=os.path.join(BASE_DIR,"media")
3. en urls agregar
    from django.conf import settings
    from django.conf.urls.static import static
    if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
4. en models agregar el campo image
    image=models.ImageField(upload_to="<subcarpetademedia>",null=True)
----------------------------------
1. 
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/santiago'
---------------------------------
pip install --user django-crispy-forms
pip install crispy-bootstrap5
agregar a installed apps
crispy-forms
crispy-bootstrap5

para administrar el panel de admin de django debo tener un usuario registrado en auth_user
crear superuser con manage.py o dando poderes en el mismo panel

-Register
crispy busca el modelo de login y lo utiliza en el html
(incluir {% load crispy_forms_tags %}
        {{form | crispy}}) <- inclusion del formulario


from .forms import CustomUserCreationForm
crear usuario configurado por nosotros

En register 
{% csrf_token %}
dice que va a entrar en un nivel de seguridad de comunicación
crea token cookie y sesion
standar de seguridad minima