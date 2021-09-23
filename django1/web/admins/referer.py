from django.contrib import admin


# Register your models here.
class RefererAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'middlename', 'lastname', 'cnic', 'address', 'designation', 'snap')

