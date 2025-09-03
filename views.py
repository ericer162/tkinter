from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all().order_by('-ano_publicaçao')
    serializer_class = LivroSerializer