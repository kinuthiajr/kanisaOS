from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import User,Invitation

# Register your models here.
class AccountUsers(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff','is_active')
    search_fields = ('email','username')
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
    def mark_inactive(self,queryset):
        for user in queryset:
            user.soft_delete()

    mark_inactive.short_decription = 'Inactive user'

admin.site.register(User,AccountUsers,)
admin.site.register(Invitation)
