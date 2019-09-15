from django.contrib import admin
from django.urls import path
import common.views
import account.views
import competition.views
import festival.views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', common.views.home, name='home'),
    path('festival/', include('festival.urls')),
    path('competition/', include('competition.urls')),
    path('account/', include('account.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
