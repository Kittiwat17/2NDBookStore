from main.models import user_Owner, Book, Typebook, user_customer
from django.contrib import admin
from django.contrib.auth.models import Permission, User

# Register your models here.
admin.site.register(user_Owner)
admin.site.register(Book)
admin.site.register(Typebook)
# admin.site.register(Furniture)
admin.site.register(user_customer)
# admin.site.register(Booking)
admin.site.register(Permission)