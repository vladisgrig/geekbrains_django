from django.contrib import admin
from .models import Me, Education, PlaceOfWork, Hobby

# Register your models here.
admin.site.register(Me)
admin.site.register(Education)
admin.site.register(PlaceOfWork)
admin.site.register(Hobby)
