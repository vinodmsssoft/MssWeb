from django.contrib import admin
from webApp.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'subject', 'contact', 'address', 'message')

# Register your models here.
admin.site.register(Contact, ContactAdmin)