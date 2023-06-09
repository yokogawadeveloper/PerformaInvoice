from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = {
    url(r'^login/', Login.as_view(), name='token_obtain_pair'),
    url(r'^login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
}
urlpatterns = format_suffix_patterns(urlpatterns)
