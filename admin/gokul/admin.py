from django.contrib import admin
from.models import Employee,articles
# Register your models here.
admin.site.register(Employee)

class articlesadmin(admin.ModelAdmin):
    list_display=['content','id','title']

admin.site.register(articles,articlesadmin)   