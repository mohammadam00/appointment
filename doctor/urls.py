from django.urls import path
from doctor.views import DoctorDetailView, DoctorListView , DoctorAddView

app_name = 'doctor'
urlpatterns = [
    path('list', DoctorListView.as_view(), name='list'),
    path('detail/<int:pk>', DoctorDetailView.as_view(), name='detail'),
    path('add', DoctorAddView.as_view(), name='add'),
]
