from django.contrib import admin

from .models import Review, DiscountCoupon, RoomPromotion, Booking

admin.site.register(Review)
admin.site.register(DiscountCoupon)
admin.site.register(RoomPromotion)
admin.site.register(Booking)