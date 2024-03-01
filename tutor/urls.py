from django.urls import path, include
from . import views
urlpatterns = [
    path('tutor/<int:id>/', views.TutorDetailView.as_view(), name='tutors'),
    path('tutor_singup/', views.TutorRegistrationView.as_view(), name = 'tutorsignup'),
    # path('tutor_login/', views.TutorLoginView.as_view(), name = 'tutorlogin'),
    # path('tutor_profile/', views.Tutorprofile, name = 'tutorprofile'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
]