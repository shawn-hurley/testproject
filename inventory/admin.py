from django.contrib import admin
from inventory.models import *

admin.site.register(InventoryRecord)
admin.site.register(Category)
admin.site.register(Item)