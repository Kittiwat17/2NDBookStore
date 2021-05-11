from main.models import user_Owner, Dormitory, Room, Furniture, user_customer, Booking
from django.contrib import admin
from django.contrib.auth.models import Permission, User

# Register your models here.
admin.site.register(user_Owner)
admin.site.register(Dormitory)
admin.site.register(Room)
admin.site.register(Furniture)
admin.site.register(user_customer)
admin.site.register(Booking)
admin.site.register(Permission)