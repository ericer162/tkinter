from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .views import UsuarioAutorizado, RegistroAcesso
import json
from datetime import datetime

@csrf_exempt
def verificar_acesso(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            identificacao = dados.get('identificacao', '').strip().lower()
            
            if not identificacao:
                return JsonResponse({'status': 'erro', 'mensagem': 'Identificação não fornecida.'}, status=400)
            
            try:
                usuario = UsuarioAutorizado.objects.get(
                    identificacao__iexact=identificacao,
                    ativo=True
                )
                acesso_permitido = True
                mensagem = f'Acesso liberado! Bem-vindo(a), {usuario.nome}!'
            except UsuarioAutorizado.DoesNotExist:
                acesso_permitido = False
                mensagem = 'Acesso negado: Identificação não autorizada.'
            
            # Registrar tentativa de acesso
            RegistroAcesso.objects.create(
                usuario=usuario if acesso_permitido else None,
                identificacao_tentativa=identificacao,
                acesso_permitido=acesso_permitido
            )
            
            return JsonResponse({
                'status': 'sucesso' if acesso_permitido else 'erro',
                'mensagem': mensagem
            }, status=200 if acesso_permitido else 403)
            
        except json.JSONDecodeError:
            return JsonResponse({'status': 'erro', 'mensagem': 'JSON inválido.'}, status=400)
    
    return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido.'}, status=405)

def listar_usuarios(request):
    if request.method == 'GET':
        usuarios = UsuarioAutorizado.objects.filter(ativo=True).values('id', 'nome', 'identificacao')
        return JsonResponse({
            'status': 'sucesso',
            'usuarios': list(usuarios),
            'total': usuarios.count()
        }, status=200)
    return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido.'}, status=405)