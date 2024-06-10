from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados  # Certifique-se de que o nome da classe está em CamelCase como é padrão
from .models import Ocorrencia,Dica,Denuncia,Alerta,Avaliacao
from .forms import LoginForm,CadastroForm,OcorrenciaForm,DicaForm,AlertaForm,AvaliacaoForm
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.models import User
from geopy.geocoders import Nominatim

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
    mensagem_sucesso=""
    mensagem_erro=""
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
        mensagem_sucesso="Ocorrencia registrada com sucesso!"
        
        return render(request, 'registrarocorrencia.html', {'mensagem_sucesso': mensagem_sucesso})
    else:
        return render(request, 'registrarocorrencia.html', {'mensagem_erro': mensagem_erro})
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
    mensagem_sucesso=""
    
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES, instance=ocorrencia)
        if form.is_valid():
            form.save()
            mensagem_sucesso="Edição feita com sucesso!"
            return redirect('/vizualizar_ocorrencia/')
            
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    return render(request, 'vizualizar_ocorrencia.html', {'form': form,'mensagem_sucesso':mensagem_sucesso})

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

def adicionar_dica(request):
    mensagem_sucesso=""
    if request.method == 'POST':
        form = DicaForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem_sucesso= "Dica adicionada com sucesso"
    else:
        form = DicaForm()
    return render(request, 'dicas_adm.html', {'form': form, 'mensagem_sucesso':mensagem_sucesso})

def exibir_dica(request):
    tipo_selecionado = request.GET.get('tipo')
    dicas = Dica.objects.filter(tipo=tipo_selecionado) if tipo_selecionado else None
    return render(request, 'dicas.html', {'dicas': dicas})

def dicas(request):

    return render(request, 'dicas.html')

def dicas_adm(request):

    return render(request, 'dicas_adm.html')

def denunciar_ocorrencia(request, ocorrencia_id):
    
    if request.method == 'POST':
        ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
        motivo = request.POST.get('motivo', '')
        Denuncia.objects.create(ocorrencia=ocorrencia, motivo=motivo)
        
        return redirect('/vizualizar_ocorrencia_user/', ocorrencia_id=ocorrencia_id)
        
    else:
        return redirect('/vizualizar_ocorrencia_user/')
        

def denuncia_adm(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'denuncia_adm.html', {'denuncias': denuncias})


def alerta_adm(request):
    usuarios = User.objects.all()
    if request.method == 'POST':
        form = AlertaForm(request.POST)
        if form.is_valid():
            alerta = form.save(commit=False)
            alerta.usuario_id = request.POST['usuario']
            alerta.save()
            return redirect('ver_alertas')
    else:
        form = AlertaForm()
    return render(request, 'alerta_adm.html', {'form': form, 'usuarios': usuarios})

def ver_alertas(request):
    alertas = Alerta.objects.all()  # Buscar todos os alertas, independentemente do usuário
    return render(request, 'ver_alertas.html', {'alertas': alertas})

def avaliar_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.ocorrencia = ocorrencia
            avaliacao.save()
            return redirect('/vizualizar_ocorrencia_user/', ocorrencia_id=ocorrencia_id)
    else:
        form = AvaliacaoForm()
    return render(request, 'vizualizar_ocorrencia.html', {'form': form, 'ocorrencia': ocorrencia})

def ver_feedbacks(request):
     avaliacoes = Avaliacao.objects.all()
     return render(request, 'ver_feedbacks.html', {'avaliacoes': avaliacoes})

def mapa_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()
    geolocator = Nominatim(user_agent="geoapiExercises")
    locations = []
    
    for ocorrencia in ocorrencias:
        location = geolocator.geocode(ocorrencia.endereco)
        if location:
            locations.append({
                'descricao': ocorrencia.descricao,
                'endereco': ocorrencia.endereco,
                'tipo_de_lixo': ocorrencia.tipo_de_lixo,
                'latitude': location.latitude,
                'longitude': location.longitude
            })
    return render(request, 'ver_alertas.html', {'locations': locations})
