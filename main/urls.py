from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('form', views.form),
    path('suggest', views.suggest),
    path('vendor/<id>', views.vendorDetail),
    path('quotes/<id>', views.vendorQuote),
    path('add_review/<id>', views.addReview)
]