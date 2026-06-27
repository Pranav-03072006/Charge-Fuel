"""
URL configuration for ChargeFuel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from development import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homefun,name="index.html"),
    path("homelink",views.homefun),
    path("aboutlink",views.aboutfun),
    path("serviceslink",views.servicesfun),
    path("contactlink",views.contactfun),
    path("signuplink",views.signupfun),
    path("loginlink",views.loginfun),
    path("settingslink",views.settingsfun),
    path("accountslink",views.accountsfun),
    path("customerdashboardlink",views.customerdashboardfun),
    path("feedbacklink",views.feedbackfun),
    path("complainlink",views.complainfun),
    path("orderlink",views.orderfun),
    path("orderevlink",views.orderevfun),
    path("orderfuellink",views.orderfuelfun),
    path("companylink",views.companyfun),
    path("companydashboardlink",views.companydashboardfun),
    path("companysettingslink",views.companysettingsfun),
    path("loadcomplainlink",views.loadcomplainfun),
    path("loadorderfuellink",views.loadorderfuelfun),
    path("loadorderevlink", views.loadorderevfun),
    path("companyfeedbacklink", views.companyfeedbackfun),
    path("companycustomerslink", views.companycustomersfun),
    path("companycontactlink", views.companycontactfun),
    # database connectivity

    path("signupcodedb",views.signupdbcode),
    path("logincodedb",views.logindbcode),
    path("contactcodedb",views.contactdbcode),
    path("settingscodedb",views.settingsdbcode),
    path("accountscodedb",views.accountsdbcode),
    path("feedbackcodedb",views.feedbackdbcode),
    path("complaincodedb",views.complaindbcode),
    path("orderevcodedb",views.orderevdbcode),
    path("orderfuelcodedb",views.orderfueldbcode),
    path("companylogincodedb",views.companylogindbcode),
    path("companysettingscodedb",views.companysettingsdbcode),
    path("companycomplaincodedb",views.companycomplaindbcode),
    path("companyorderfuelcodedb",views.companyorderfueldbcode),
    path("companyorderevcodedb",views.companyorderevdbcode),
    path("companyfeedbackcodedb", views.companyfeedbackdbcode),
    path("companycustomerscodedb", views.companycustomersdbcode),
    path("companycontactcodedb", views.companycontactdbcode),
]
