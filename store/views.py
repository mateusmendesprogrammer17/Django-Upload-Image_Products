from django.shortcuts import render,redirect


from .forms import ProdutoForm
from .models import Produto
# Create your views here.
def home(request):
    produto = Produto.objects.all()
    #exibe produtos na página inicial
    return render(request,"store/index.html",{'produtos':produto})

def cadastrar_produtos(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProdutoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            # Aqui você deve retornar o formulário com os erros
            context = {'form': form}
            print(form.errors) 
            return render(request, "store/cadastro_produtos.html", context)
    else:
        form = ProdutoForm()
        context = {'form': form}
        return render(request, "store/cadastro_produtos.html", context)
