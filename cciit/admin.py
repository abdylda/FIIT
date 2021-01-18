from django.contrib import admin

from cciit.models import Unit, Engineers, Categories, Cabinet_name, Cabinet, Available_techniques


class UnitAdmin(admin.ModelAdmin):
    pass
admin.site.register(Unit, UnitAdmin)


class EngineersAdmin(admin.ModelAdmin):
    list_display = ['fio', 'Cabinet', 'position', 'phone_number', 'start_work', 'end_work', 'photo']
admin.site.register(Engineers, EngineersAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Categories, CategoriesAdmin)


class Cabinet_nameAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cabinet_name, Cabinet_nameAdmin)


class CabinetAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Cabinet_name']
admin.site.register(Cabinet, CabinetAdmin)


class Available_techniquesAdmin(admin.ModelAdmin):
    list_display = ['Cabinet', 'Cabinet_name', 'Categories', 'Unit', 'KODTMU', 'Names', 'Quantity', 'sostoyani']
    list_filter = ['Cabinet', 'sostoyani', 'Categories', 'Cabinet_name']
    search_fields = ('Cabinet', 'Cabinet_name')
admin.site.register(Available_techniques, Available_techniquesAdmin)