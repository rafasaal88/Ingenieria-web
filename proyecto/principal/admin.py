from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from .models import Post

admin.site.register(Post)
