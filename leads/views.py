from django.shortcuts import render, redirect
from .models import Lead

def landing(request):
    if request.method == "POST":
        Lead.objects.create(
            full_name=request.POST.get("full_name"),
            phone=request.POST.get("phone"),
            income=request.POST.get("income"),
            location=request.POST.get("location"),
        )
        return redirect("/?ok=1")

    return render(request, "landing.html")
