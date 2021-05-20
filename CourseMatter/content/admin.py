from django.contrib import admin
from .models import Content, Course

#overwrites admin panel display
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Content, ContentAdmin)
admin.site.register(Course, CourseAdmin)