from django.contrib import admin
from .models import EditablePage

# Register your models here.


@admin.register(EditablePage)
class EditablePage_admin(admin.ModelAdmin):
    list_display = ('id', 'name_heading', 'name_content', 'occupation_heading', 'occupation_content',
                    'country_heading', 'country_content', 'image_img', 'txt_over_img')
