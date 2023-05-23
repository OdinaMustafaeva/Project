from django.urls import path
from users.views import ProfileView, RegisterView, CustomTokenObtainPairView, SendEmailVerificationCodeView, \
    CheckEmailVerificationCodeView, CheckEmailVerificationCodeWithParams, FacebookLogin, GoogleLogin, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path('auth/token/', LoginView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login/', TokenRefreshView.as_view(), name='token_refresh'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email/verification/", SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path('auth/google/', GoogleLogin.as_view(), name='google_auth'),
    path('auth/facebook/', FacebookLogin.as_view(), name='facebook_auth'),
    path("email/check-verification/", CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path("email/check-verification-code/", CheckEmailVerificationCodeWithParams.as_view(), name="check-email"),
]
