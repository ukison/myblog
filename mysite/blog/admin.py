from django.contrib import admin
from models import BlogPost


class Blogpost_Admin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(BlogPost, Blogpost_Admin)
