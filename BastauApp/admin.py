from django.contrib import admin

from BastauApp.models import User,Student,Partner,Case,Answer


admin.site.register(Student)
admin.site.register(Partner)
admin.site.register(Case)
admin.site.register(Answer)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'password', 'phone')
    