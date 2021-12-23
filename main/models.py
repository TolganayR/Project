from django.db import models
class Customer(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    def __str__(self):
        return "Customer: "+self.username

class RoomManager(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    def __str__(self):
        return "Room Manager: "+self.username

class Contact(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    message=models.TextField()
    def __str__(self):
        if self.name == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.name

class Rooms(models.Model):
    manager=models.ForeignKey(RoomManager, on_delete=models.CASCADE)
    room_no=models.CharField(max_length=5)
    room_description=models.TextField(max_length=500)
    is_available=models.BooleanField(default=True)
    price=models.FloatField(default=100.00)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    room_image = models.ImageField(upload_to="photos/%Y/%m/%d", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return "Room No: "+str(self.id)

class Booking(models.Model):
    room_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    email=models.CharField(max_length=50)
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    end_day=models.DateField(auto_now=False, auto_now_add=False)
    booked_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return "Booking ID: "+str(self.id)