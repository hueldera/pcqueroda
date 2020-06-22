from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Software, Computer
from django.db.models import Q

def index(request):
    context = {}

    url_parameter = request.GET.get("s")

    if url_parameter:
        software_list = Software.objects.filter(Q(name__icontains=url_parameter) | Q(acronym__icontains=url_parameter))
    else:
        software_list = Software.objects.order_by('-updated_at')[:6]

    context['software_list'] = software_list

    if request.is_ajax():
        html = render_to_string(template_name='searcher/softwares-results-partial.html', context=context)

        data_dict = {"html_from_view": html}

        print(data_dict)

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'searcher/index.html', context)

def discover_computers(request):
    context = {}

    selected_softwares = list(map(int, request.GET.getlist('sw')))

    context['selected_softwares'] = Software.objects.filter(pk__in=selected_softwares)

    if not context['selected_softwares']:
        return redirect('/searcher/')

    context['computer_list'] =  Computer.objects.all()

    return render(request, 'searcher/results.html', context)

