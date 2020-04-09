from django.shortcuts import render, redirect

from .models import *


def landing (request):
    return render(request, "landing.html")

def form (request):

    if "user_id" in request.session:
        user = User.objects.get(id = request.session["user_id"])

    context = {
        "user": user,
        "vendors": Vendor.objects.all()
    }

    return render (request, "form.html", context)

def suggest (request):
    x = {}
    if request.POST["infrastructure"] == "On Premise only":
        x["cloud_only"] = "False"
        x["prem_only"] = "True"
        x["hybrid"] = "False"
    if request.POST["infrastructure"] == "Cloud only":
        x["cloud_only"] = "True"
        x["prem_only"] = "False"
        x["hybrid"] = "False"
    if request.POST["infrastructure"] =="Hybrid":
        x["cloud_only"] = "False"
        x["prem_only"] = "False"
        x["hybrid"] = "True"

    if request.POST["sites"] == "U.S.":
        x["international"] = "False"
    if request.POST["sites"] == "International":
        x["international"] = "True"

    if request.POST["latency"] == "mission critical":
        x["low_latency"] = "True"
    if request.POST["latency"] == "more cloud focused":
        x["low_latency"] = "False"

    if request.POST["sla"] == "I need this":
        x["sla"] = "True"
    if request.POST["sla"] == "no worries":
        x["sla"] = "False"
    
    if request.POST["firewall"] == "I need this":
        x["firewall"] = "True"
    if request.POST["firewall"] == "no worries":
        x["firewall"] = "False"

    context = {
        "matches": Match.objects.filter(cloud_only = x["cloud_only"], prem_only = x["prem_only"], hybrid = x["hybrid"], international = x["international"], low_latency = x["low_latency"], sla = x["sla"], firewall = x["firewall"]),
        "vendors": Vendor.objects.all(),
        "email": request.session["email"]
    }
    
    return render (request, "suggest.html", context)


def vendorDetail (request, id):
    vendor = Vendor.objects.get(id=id)
    all_reviews = vendor.reviews.all()
    review_count = 0
    for review in all_reviews:
        review_count +=1

    context = {
        "vendor": vendor,
        "email": request.session["email"],
        "all_reviews": vendor.reviews.all(),
        "review_count": review_count,
    }

    return render(request, "vendor_detail.html", context)

def vendorQuote (request, id):
    pass

def addReview (request, id):
    pass



