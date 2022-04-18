from django.conf.urls import url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('new_hood/', views.new_hood, name='new_hood'),
    path('hood/', views.hood, name='hood'),
    path('edithood/', views.edit_hood, name='edithood'),
    path('businesses/<id>', views.businesses, name='hoodbusiness'),
    path('singlehood/<id>', views.singlehood, name='singlehood'),
    path('new_business/', views.newbiz, name='newbiz'),
    path('post', views.post, name='post'),
    path('hoodpost/<id>', views.posthood, name='hoodpost'),
    path('joinhood/<id>', views.joinhood, name='joinhood'),
    path('leavehood/<id>', views.leavehood, name='leavehood'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)