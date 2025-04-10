from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view (
    openapi.Info(
        title='Movie API',
        default_version='1.0',
        description='API about movies'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger')),
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls'))
]
