from django.contrib import admin
from hello.models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'sex')
    search_fields = ('name',)
    #fields = ('name', 'age')

#add models to admin site
admin.site.register(UserInfo, UserInfoAdmin)
