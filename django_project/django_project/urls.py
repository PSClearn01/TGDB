from django.urls import include
from django.conf.urls import re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^admin/', admin.site.urls),
]