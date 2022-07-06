from rest_framework.routers import DefaultRouter

from body.viewset import UserGalleryViews, UserViews

urlpatterns = []


router = DefaultRouter()
router.register(r'site/user', UserViews, basename='user')
router.register(r'site/user_gallery', UserGalleryViews, basename='user_gallery')


urlpatterns += router.urls