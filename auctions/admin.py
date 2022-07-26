from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Listing, Bid

# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'age')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_closed', 'category', 'bid')


class BidAdmin(admin.ModelAdmin):
    list_display = ('bid', 'user')


admin.site.register(User, MyUserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
