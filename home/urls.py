from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.index,name="index"),
    path('main',views.index,name="main"),
    path('signup',views.signup,name="signup"),
    path('login',views.Login,name="login"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path("HealthDash",views.farmDash, name="farmDash"),
    path("Patients",views.patDetails,name="Pat"),
    path("medicine",views.medicine,name="medicine"),
    path("apptDoc",views.appointedDoctor,name="appointed"),
    path("patLog",views.patLog,name="patientLog"),
    path('changeLog',views.changeLog,name="change"),
    path("changeDoc",views.changeDoc,name="changeDoc"),
    path("ambulanceSystem",views.ambulance,name="ambulance"),
    path("emergency",views.emergency,name="emergency"),
    path("docVerify",views.docVerify,name="DocVerify"),
    path("verification",views.verification,name="verification")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
