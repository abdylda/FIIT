from django.contrib import admin

from landing.models import Category, Edizm, NalichiTehniki, NamKabinet, Mebel, Engineer, Kabinet,  Ingener


class catigoriAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, catigoriAdmin)


class EdizmAdmin(admin.ModelAdmin):
    pass
admin.site.register(Edizm, EdizmAdmin)


class NamKabinetAdmin(admin.ModelAdmin):
    pass
admin.site.register(NamKabinet, NamKabinetAdmin)


class KabinetAdmin(admin.ModelAdmin):
    list_display = ['Naimenovanie', 'NamKabinet']
admin.site.register(Kabinet, KabinetAdmin)


class MebelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Mebel, MebelAdmin)


class NalichiTehnikiAdmin(admin.ModelAdmin):
    list_display = ['Kabinet', 'NamKabinet', 'category', 'Edizm', 'kodTMU', 'Naimenovanie', 'Kolich', 'sostoyanie']
    list_filter = ['Kabinet', 'sostoyanie', 'category', 'NamKabinet']
    search_fields = ('Kabinet', 'NamKabinet')
admin.site.register(NalichiTehniki, NalichiTehnikiAdmin)



class EngineerAdmin(admin.ModelAdmin):
    list_display = ['kabinet', 'aty', 'doljnosti', 'tel', 'start_work', 'end_work', 'photo']
    list_filter = ['kabinet', 'doljnosti']
admin.site.register(Engineer, EngineerAdmin)






# class KlassMebelAdmin(admin.ModelAdmin):
#     list_display = ['Kabinet', 'NamKabinet', 'FIO', 'Doljnosti', 'Mebel', 'Edizm', 'kodTMU', 'kolich']
#     list_filter = ['Kabinet', 'NamKabinet', 'Doljnosti', 'Mebel']
#
#
# admin.site.register(Mebel, KlassMebelAdmin)

admin.site.site_title = "Администратор сайт Абдулла"
admin.site.site_header = "Администратор сайт Абдулла"