from rest_framework.routers import DefaultRouter
from .views import LivroViewSet

router = DefaultRouter()
router.register(r'livros',LivroViewSet, basename='livro')

urlpatterns = router.urls