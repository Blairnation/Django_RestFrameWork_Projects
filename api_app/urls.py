from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('car-list',CarViewSet, basename='car')
router.register('posts', PostViewSet, basename='posts')
router.register('post-rates', PostRatesViewSet, basename='post-rates')
router.register('students', StudentsViewSet, basename='students')
router.register('modules', ModulesViewSet, basename='modules')
router.register('forecast', ForecastViewset, basename='forecast')

urlpatterns = [
    path('messager/',messager, name='messager'),
    path('message/',Message.as_view(), name='message' ),
    path('car/', CarApiView.as_view()),
    path('carplan/', CarPlanApiView.as_view()),

    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)