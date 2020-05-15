from django.contrib import admin

from landing.models import Category, Edizm, NalichiTehniki, Kabinet, NamKabinet, Mebel, Engineer


class catigoriAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, catigoriAdmin)


class EdizmAdmin(admin.ModelAdmin):
    pass


admin.site.register(Edizm, EdizmAdmin)


class KabinetAdmin(admin.ModelAdmin):
    list_display = ['id', 'Naimenovanie', 'NamKabinet']


admin.site.register(Kabinet, KabinetAdmin)


class NamKabinetAdmin(admin.ModelAdmin):
    pass


admin.site.register(NamKabinet, NamKabinetAdmin)


class MebelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mebel, MebelAdmin)





class NalichiTehnikiAdmin(admin.ModelAdmin):
    list_display = ['Kabinet', 'NamKabinet', 'category', 'kodTMU', 'Naimenovanie', 'Edizm', 'kolich']
    list_filter = ['category', 'Naimenovanie', 'kodTMU', 'Kabinet', 'NamKabinet']


admin.site.register(NalichiTehniki, NalichiTehnikiAdmin)


class EngineerAdmin(admin.ModelAdmin):
    list_display = ['kabinet', 'aty', 'doljnosti', 'tel', 'start_work', 'end_work']
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