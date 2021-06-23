
from django.urls import path
from django.urls.conf import include
from.import views
urlpatterns = [
    path("calsi/",views.calsi,name="bmi"),
    path("bmi_calculations/",views.bmi_calculations,name="bmi_calculations")
]