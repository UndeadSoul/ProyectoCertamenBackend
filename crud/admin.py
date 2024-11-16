from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Chef
from .models import Contenido
from .models import Pizza

admin.site.register(Post)
admin.site.register(Chef)
admin.site.register(Contenido)
admin.site.register(Pizza)