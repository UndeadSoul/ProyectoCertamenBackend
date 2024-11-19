from django.contrib import admin

# Register your models here.
# Se registran los modelos para ser visibles en el panel de django
from .models import Post
from .models import Chef
from .models import MasaDisp
from .models import Contenido
from .models import Pizza

admin.site.register(Post)
admin.site.register(Chef)
admin.site.register(MasaDisp)
admin.site.register(Contenido)
admin.site.register(Pizza)
