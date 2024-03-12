from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from authentication.models import UserProfile


@login_required(login_url="/auth/sign-in")
def dashboard(request):
    if request.user.user_type == "doctor":
        return render(request, "dashboard/doctor_dashboard.html")
    return render(request, 'dashboard/patient_dashboard.html')
