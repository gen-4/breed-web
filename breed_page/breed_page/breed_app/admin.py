from django.contrib import admin

from breed_page.breed_app.models import Breed, Coat, Discipline

# Register your models here.
admin.site.register(Breed)
admin.site.register(Coat)
admin.site.register(Discipline)