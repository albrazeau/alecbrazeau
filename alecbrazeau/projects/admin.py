from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
