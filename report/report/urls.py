
from django.contrib import admin
from django.urls import path , include
#allow us to return Http response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ReportData.urls')),
]
