from django.urls  import  include, path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from app.views import ProfileImageView
admin.autodiscover()

urlpatterns = [
    path('', ProfileImageView.as_view(), name='profile_image_upload'),
    path('admin/', admin.site.urls),

]
