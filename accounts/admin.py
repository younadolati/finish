from django.contrib import admin
from .models import Follows,Room,Message
# Register your models here.
admin.site.register(Follows)
admin.site.register(Room)
admin.site.register(Message)
