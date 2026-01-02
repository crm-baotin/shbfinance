from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),   # 👈 THÊM DÒNG NÀY
    path("", include("leads.urls")),
]
