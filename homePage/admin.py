from django.contrib import admin
from .models import Post, Comment, Meeting
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Meeting)



