from django.contrib import admin


from menu.models import Menu


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title', )}
    list_display = ('title', 'parent')


admin.site.register(Menu, MenuAdmin)

