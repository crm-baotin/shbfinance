from django.contrib.admin import SimpleListFilter
from django.utils.timezone import make_aware
from datetime import datetime


class DateRangeFilter(SimpleListFilter):
    title = "Khoảng ngày"
    parameter_name = "created_range"

    template = "admin/date_range_filter.html"

    def lookups(self, request, model_admin):
        return ()

    def queryset(self, request, queryset):
        start = request.GET.get("start_date")
        end = request.GET.get("end_date")

        if start:
            start_date = make_aware(datetime.strptime(start, "%Y-%m-%d"))
            queryset = queryset.filter(created_at__gte=start_date)

        if end:
            end_date = make_aware(datetime.strptime(end, "%Y-%m-%d"))
            queryset = queryset.filter(created_at__lte=end_date)

        return queryset
