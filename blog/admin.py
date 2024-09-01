from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Tag, Post, Comment
from blog.models import Tag, Post, Comment, AuthorProfile

admin.site.register(Tag)
admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at')


admin.site.register(Post, PostAdmin)
admin.site.register(AuthorProfile)