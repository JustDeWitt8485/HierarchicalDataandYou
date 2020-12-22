from django.contrib import admin
from folder_file.models import File
from mptt.admin import DraggableMPTTAdmin
# Register your models here.
admin.site.register(File, DraggableMPTTAdmin)
