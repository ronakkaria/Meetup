from django.contrib import admin
from .models import User as MeetupUser

# Register your models here.

admin.site.register(MeetupUser)