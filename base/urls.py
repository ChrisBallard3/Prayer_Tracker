from django.urls import path
from .views import PrayerDetail, PrayerList, PrayerCreate, PrayerUpdate, PrayerDelete, PriorityPrayer, Register, SignIn
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signin/', SignIn.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(next_page='signin'), name='signout'),
    path('register/', Register.as_view(), name='register'),

    path('', PrayerList.as_view(), name='home'),
    path('prayer/<int:pk>', PrayerDetail.as_view(), name='prayer'),
    path('priority/<int:pk>', PriorityPrayer.as_view(), name='priority'),
    path('create-prayer/', PrayerCreate.as_view(), name='create-prayer'),
    path('update-prayer/<int:pk>', PrayerUpdate.as_view(), name='update-prayer'),
    path('delete-prayer/<int:pk>', PrayerDelete.as_view(), name='delete-prayer'),
]
