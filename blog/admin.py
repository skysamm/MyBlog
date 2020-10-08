from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status","tag")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
