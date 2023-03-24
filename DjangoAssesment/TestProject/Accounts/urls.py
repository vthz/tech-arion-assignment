from django.urls import path
from . import views

# Accounts urls

urlpatterns = [
    path("/test-api", views.testFunction),
    path("/create-new-user", views.createNewUser),  # done
    path("/get-all-users", views.getAllUser),  # done
    path("/send-otp-to-email", views.sendOTPtoEmail),  # done
    path("/login-with-otp-email", views.loginWithOtpAndEmail)  # done
]
