from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados  # Certifique-se de que o nome da classe está em CamelCase como é padrão
from .models import Ocorrencia
from .forms import LoginForm,CadastroForm,OcorrenciaForm
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from django.db.models import Count

def login(request):
    # Supondo que 'logo.png' está localizado dentro do diretório de mídia
    imagem_url = '/media/logo.png'  # Atualize o caminho conforme necessário
    return render(request, 'front/login.html', {'imagem_url': imagem_url})

def cadastro(request):

    return render(request, 'front/cadastro.html')

def vizualizar_ocorrencia(request):
    endereco_filtro = request.GET.get('endereco_filtro')
    if endereco_filtro:
        # Filtrar as ocorrências com base no endereço fornecido
        ocorrencias = Ocorrencia.objects.filter(endereco__icontains=endereco_filtro)
        return render(request, 'vizualizar_ocorrencia.html', {'ocorrencias': ocorrencias})
    else:
        ocorrencias = Ocorrencia.objects.all()
    
    data_filtro = request.GET.get('data_filtro')
    if data_filtro:
        data_filtro = datetime.strptime(data_filtro, '%Y-%m-%d').date()
        
        ocorrencias = Ocorrencia.objects.filter(data__date=data_filtro)
    else:
        ocorrencias = Ocorrencia.objects.all()
    return render(request, 'vizualizar_ocorrencia.html', {'ocorrencias': ocorrencias})

def vizualizar_ocorrencia_user(request):
    endereco_filtro = request.GET.get('endereco_filtro')
    if endereco_filtro:
        # Filtrar as ocorrências com base no endereço fornecido
        ocorrencias = Ocorrencia.objects.filter(endereco__icontains=endereco_filtro)
        return render(request, 'vizualizar_ocorrencia_user.html', {'ocorrencias': ocorrencias})
    else:
        ocorrencias = Ocorrencia.objects.all()
    
    data_filtro = request.GET.get('data_filtro')
    if data_filtro:
        data_filtro = datetime.strptime(data_filtro, '%Y-%m-%d').date()
        
        ocorrencias = Ocorrencia.objects.filter(data__date=data_filtro)
    else:
        ocorrencias = Ocorrencia.objects.all()
    return render(request, 'vizualizar_ocorrencia_user.html', {'ocorrencias': ocorrencias})

def home_aluno(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if tipo == 'administrador':
            return redirect('/home_adm')
        elif tipo == 'aluno':
            return redirect('/home_aluno')
        else:
            return HttpResponse("Usuário ou senha inválidos", status=401)
    return render(request, 'home_aluno.html')

def home_adm(request):
    usuarios = Dados.objects.all()  # Obtém todos os usuários do banco de dados
    ocorrencias = Ocorrencia.objects.all()  # Obtém todas as ocorrências do banco de dados
    return render(request, 'home_adm.html', {'usuarios': usuarios, 'ocorrencias': ocorrencias})



def registrar_ocorrencia(request):
    if request.method == 'GET':
        return render(request, 'registrarocorrencia.html')
    elif request.method == 'POST':
        descricao = request.POST.get('descricao')
        endereco = request.POST.get('endereco')
        tipo_de_lixo = request.POST.get('tipo_de_lixo')
        
        # Acessa o arquivo de imagem enviado
        imagem = request.FILES.get('imagem')
        data = timezone.now()
        
        # Cria uma nova instância do modelo Ocorrencia e salva os dados, incluindo a imagem
        ocorrencia = Ocorrencia(descricao=descricao, endereco=endereco, tipo_de_lixo=tipo_de_lixo, imagem=imagem,data=data)
        ocorrencia.save()
        
        return render(request, 'registrarocorrencia.html', {'message': 'Ocorrência registrada com sucesso!'})
    else:
        return render(request, 'registrarocorrencia.html', {'error': 'Método não suportado'})
def home_adm(request):
    usuarios = Dados.objects.all()  # Obtém todos os usuários do banco de dados
    ocorrencias = Ocorrencia.objects.all()  # Obtém todas as ocorrências do banco de dados
    return render(request, 'home_adm.html', {'usuarios': usuarios, 'ocorrencias': ocorrencias})

def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            tipo = form.cleaned_data['tipo']
            
            usuario = Dados.objects.filter(nome=nome, senha=senha, tipo=tipo).first()
            if usuario:
                if tipo == 'usuario':
                    
                    return redirect('/home_aluno/')  
                elif tipo == 'administrador':
                    
                    return redirect('/home_adm/')
            
            erro = 'Usuário não cadastrado ou credenciais incorretas.'
    else:
        form = LoginForm()
        erro = None
    return render(request, 'front/login.html', {'form': form, 'erro': erro})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def listar_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()
    return render(request, 'vizualizar_ocorrencia.html', {'ocorrencias': ocorrencias})

def excluir_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    ocorrencia.delete()
    return redirect('/vizualizar_ocorrencia/') 

def editar_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES, instance=ocorrencia)
        if form.is_valid():
            form.save()
            return redirect('/vizualizar_ocorrencia/')
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    return render(request, 'vizualizar_ocorrencia.html', {'form': form})

def stats(request):

    return render(request,'stats.html')

def estatisticas_ocorrencias(request):
    # Calcular estatísticas
    tipo_lixo_count = Ocorrencia.objects.values('tipo_de_lixo').annotate(count=Count('id'))

    # Formatando os dados para o formato JSON
    estatisticas = {
        'tipos_lixo': [item['tipo_de_lixo'] for item in tipo_lixo_count],
        'count': [item['count'] for item in tipo_lixo_count],
    }

    return JsonResponse(estatisticas)