from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse  # type: ignore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def login(request):
        
    return render(request, 'front/login.html')

def home_aluno(request):

    return render(request, 'home_aluno.html')
def home_adm(request):

    return render(request, 'home_adm.html')
@csrf_exempt
def processar_formulario(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if tipo == 'administrador':
            redirect_url = '/home_adm'
        elif tipo == 'aluno':
            redirect_url = '/home_aluno'
        else:
            redirect_url = '/'

        return JsonResponse({'redirect': redirect_url})

    return JsonResponse({'error': 'Método não permitido'}, status=405)