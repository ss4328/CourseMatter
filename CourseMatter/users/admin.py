from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'get_country')
    # list_filter = ('Profile.country',)
    prefetch_related = ('Profile',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def get_country(self, instance):
        return instance.Profile.country

    # get_country.short_description = 'Location'


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
