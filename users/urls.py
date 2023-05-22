from django.urls import path
from users.views import ProfileView, RegisterView, CustomTokenObtainPairView, SendEmailVerificationCodeView, \
    CheckEmailVerificationCodeView, CheckEmailVerificationCodeWithParams
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email/verification/", SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path("email/check-verification/", CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path("email/check-verification-code/", CheckEmailVerificationCodeWithParams.as_view(), name="check-email"),
]
