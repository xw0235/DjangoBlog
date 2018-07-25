from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    #path('admin/', admin.site.urls),
]
