from django.shortcuts import render, get_object_or_404
from django.template.backends import django
from .models import LeccionAprendida, Experto
from django.shortcuts import render

def dashboard(request):
    context = {
        'total_lecciones': LeccionAprendida.objects.count(),
        'total_categorias': 6,
        'total_expertos': Experto.objects.count(),
        'lecciones_recientes': LeccionAprendida.objects.all().order_by('-fecha_creacion')[:6],
    }
    return render(request, 'lecciones/dashboard.html', context)

def categoria_view(request, categoria):
    lecciones = LeccionAprendida.objects.filter(categoria=categoria)
    context = {
        'categoria': categoria,
        'lecciones': lecciones,
    }
    return render(request, 'lecciones/categoria.html', context)

def leccion_detalle(request, leccion_id):
    leccion = get_object_or_404(LeccionAprendida, id=leccion_id)
    context = {
        'leccion': leccion,
    }
    return render(request, 'lecciones/leccion_detalle.html', context)

def expertos_view(request):
    expertos = Experto.objects.all()
    context = {
        'expertos': expertos,
    }
    return render(request, 'lecciones/expertos.html', context)


def dashboard_bi(request):
    return render(request, 'lecciones/dashboard_bi.html')