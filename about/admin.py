from django.contrib import admin
from .models import Post, Comment, About
from django_summernote.admin import SummernoteModelAdmin




@admin.register(About)
class Admin(SummernoteModelAdmin):

    summernote_fields = ('content',)

# Register your models here.
admin.site.register(About)
