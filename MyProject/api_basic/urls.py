from django.urls import path
from .views import user_list, login_list, UserAPIView, GenericAPIView, LoginAPIView, Genericlogin

urlpatterns = [
    #path('user/', user_list),
    # path('login/', login_list),
    path('user/', UserAPIView.as_view()),
    path('user/', LoginAPIView.as_view()),
    path('generic/user/<int:id>/', GenericAPIView.as_view()),
    path('user/login/', Genericlogin.as_view()),
]
