from django.contrib import admin
from . models import Contactform


@admin.register(Contactform)
class Contact(admin.ModelAdmin):
    list_display = ['id','name','email','phone','message',]
# Register your models here.
