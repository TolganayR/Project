from django.contrib import admin
from .models import Customer,RoomManager,Contact,Booking,Rooms
admin.site.register(Customer)
admin.site.register(RoomManager)
admin.site.register(Rooms)
admin.site.register(Contact)
admin.site.register(Booking)
