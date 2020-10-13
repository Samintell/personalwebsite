from django.contrib import admin
from kbdyndemo.models import UserInput
# Register your models here.
class UserInputAdmin(admin.ModelAdmin):
    fields = ['userID', 'text', 'typingData', 'dateOfData']
admin.site.register(UserInput, UserInputAdmin)