from django.shortcuts import render
from .forms import CurriculoUploadForm
from .models import  AnaliseCurriculo

def home(request):
    return render(request, 'analisador/home.html')

def nova_analise(request):
    resultado = None

    if request.method == 'POST':
        form = CurriculoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.cleaned_data['curriculo']
            vaga = form.cleaned_data['nome_vaga']
            analise_texto =  'Analise simulada:Curriculo recebido com sucesso.'

            registro = AnaliseCurriculo.objects.create(
                nome_vaga=vaga,
                curriculo=arquivo,
                analise=analise_texto,
            )

            resultado= {
                'arquivo': registro.curriculo.name,
                'vaga': registro.nome_vaga,
                'analise': registro.analise
            }
    else:
        form =CurriculoUploadForm()
    return render(request, 'analisador/nova_analise.html', {
        'form': form,
        'resultado':resultado,
    })
# Create your views here.
