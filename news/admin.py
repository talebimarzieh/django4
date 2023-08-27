from django.contrib import admin
from .models import news
from .models import contact
# Register your models here.
admin.site.register(news)
admin.site.register(contact)