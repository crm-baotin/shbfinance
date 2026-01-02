from django.contrib import admin
from django.http import HttpResponse
from .models import Lead
import csv


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "income", "location", "created_at")
    search_fields = ("full_name", "phone")

    # ✅ LỌC NGÀY CHUẨN DJANGO – CÓ CUSTOM RANGE
    list_filter = (
        "income",
        "location",
        ("created_at", admin.DateFieldListFilter),
    )

    ordering = ("-created_at",)
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv; charset=utf-8-sig"
        )
        response["Content-Disposition"] = 'attachment; filename="leads.csv"'
        response.write('\ufeff')

        writer = csv.writer(response)
        writer.writerow(["Họ tên", "SĐT", "Thu nhập", "Nơi sống", "Thời gian"])

        for lead in queryset:
            writer.writerow([
                lead.full_name,
                lead.phone,
                lead.income,
                lead.location,
                lead.created_at.strftime("%d/%m/%Y %H:%M"),
            ])

        return response

    export_as_csv.short_description = "Xuất Excel (theo bộ lọc)"
