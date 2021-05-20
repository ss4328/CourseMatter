from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin import SimpleListFilter

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CountryListFilter(admin.SimpleListFilter):
    title = 'Country'
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        countries = set()
        for t in model_admin.model.objects.filter():
            try:
                if t.Profile:
                    print(t.Profile.country)
                    countries.add(t.Profile.country)
            except:
                print('no country of {}'.format(t))

        return [(country, country)for country in countries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(country=self.value())
        else:
            return queryset

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'get_country')
    list_filter = (CountryListFilter,)
    prefetch_related = ('Profile',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def get_country(self, instance):
        return instance.Profile.country

    get_country.short_description = 'Location'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
