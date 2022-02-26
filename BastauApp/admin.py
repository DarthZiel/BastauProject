from django.contrib import admin

from BastauApp.models import *

admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Partner)
admin.site.register(Case)
admin.site.register(Answer)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


