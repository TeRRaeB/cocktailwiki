from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status','image')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
