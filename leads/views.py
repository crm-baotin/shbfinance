from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect
from .models import Lead
import requests

TELEGRAM_TOKEN = "8213846644:AAG_Mom7MRzH97Y_-c7KQocQ0VS9qqf3mIc"
CHAT_ID = "6663298744"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print("Telegram error:", e)


def landing(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        income = request.POST.get("income")
        location = request.POST.get("location")

        time_limit = timezone.now() - timedelta(hours=24)

        if Lead.objects.filter(phone=phone, created_at__gte=time_limit).exists():
            return render(request, "landing.html", {
                "error": "Số điện thoại này đã gửi thông tin trong vòng 24 giờ qua. Vui lòng thử lại sau."
            })

        Lead.objects.create(
            full_name=full_name,
            phone=phone,
            income=income,
            location=location,
        )

        message = (
            "📥 <b>LEAD MỚI</b>\n\n"
            f"👤 <b>Họ tên:</b> {full_name}\n"
            f"📞 <b>SĐT:</b> {phone}\n"
            f"💰 <b>Thu nhập:</b> {income}\n"
            f"📍 <b>Khu vực:</b> {location}"
        )

        # 🔔 Gửi Tele (có lỗi cũng KHÔNG ảnh hưởng redirect)
        send_telegram(message)

        # 🔥 DÒNG QUYẾT ĐỊNH
        return redirect("thank_you")

    return render(request, "landing.html")


def thank_you(request):
    return render(request, "thank_you.html")
