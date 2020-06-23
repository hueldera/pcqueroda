from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Software, Computer
from django.db.models import Q, Model, Max, Min

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

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'searcher/index.html', context)

def discover_computers(request):
    context = {}

    # add selected softwares to context

    selected_softwares = list(map(int, request.GET.getlist('sw')))

    context['selected_softwares'] = Software.objects.filter(pk__in=selected_softwares)

    if not context['selected_softwares']:
        return redirect('/searcher/')

    context['computer_list']: Model =  Computer.objects.all()

    # calculate betters computers

    min_graphics_level = round(context['selected_softwares'].aggregate(Max('min_graphics_level'))['min_graphics_level__max'])
    min_processor_level = round(context['selected_softwares'].aggregate(Max('min_processor_level'))['min_processor_level__max'])
    min_memory_level = round(context['selected_softwares'].aggregate(Max('min_memory_level'))['min_memory_level__max'])

    max_graphics_level = round(context['selected_softwares'].aggregate(Max('max_graphics_level'))['max_graphics_level__max'] + 2)
    max_processor_level = round(context['selected_softwares'].aggregate(Max('max_processor_level'))['max_processor_level__max'] + 2)
    max_memory_level = round(context['selected_softwares'].aggregate(Max('max_memory_level'))['max_memory_level__max'] + 2)

    computers = Computer.objects.filter(Q(graphics_level__lte=max_graphics_level) &
                            Q(processor_level__lte=max_processor_level) &
                            Q(memory_level__lte=max_memory_level) &
                            Q(graphics_level__gte=min_graphics_level) &
                            Q(processor_level__gte=min_processor_level) &
                            Q(memory_level__gte=min_memory_level)).order_by('processor_level', 'graphics_level', 'memory_level', 'price')

    base_computers = {}

    computer_list = []

    # separate categories
    for computer in computers:
        if computer.category not in base_computers:
            base_computers[computer.category] = []
        base_computers[computer.category].append(computer)


    for computer_category in base_computers.values():
        if len(computer_category) > 3:
            computer_list.append(computer_category[0])
            computer_list.append(computer_category[round(len(computer_category)/2)]) 
            computer_list.append(computer_category[len(computer_category)-1])
        else:
            computer_list =  computer_list + computer_category

    context['computer_list'] = computer_list

    return render(request, 'searcher/results.html', context)

