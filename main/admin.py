from django.contrib import admin

from . models import Review, Quote, Vendor, Match

admin.site.register(Review)
admin.site.register(Vendor)
admin.site.register(Match)


