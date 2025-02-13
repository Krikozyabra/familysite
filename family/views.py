from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import render

from family.models import FamilyMember, Relations, Images

def updateData(request):
    context = {}
    if request.method == 'GET':
        keywords = request.GET.get('keywords')
        all_queries = None
        field = 'name'  # change accordingly
        for keyword in keywords.split(' '):  # keywords are splitted into words (eg: john science library)
            all_queries = Q(**{field + '__icontains': keyword})

        members = FamilyMember.objects.filter(all_queries).distinct()
        context['mens'] = getList(members)
        return JsonResponse(context)


def getList(members):
    res = [{'name': mem.name,
            'url': mem.get_absolute_url(),
            } for mem in members]
    return res
    
def getBaS(parentsId, manId):
    rels = Relations.objects.filter(parent__in=parentsId).values_list("child", flat=True).exclude(child=manId).distinct()
    members = []
    for rel in rels:
        members.append(FamilyMember.objects.get(pk=rel))
    return members


# Create your views here.
def index(request):
    keywords = ''
    images = Images.objects.all()
    context = {
        'images': images,
    }
    if request.method == 'POST':  # form was submitted

        keywords = request.POST.get("keywords")  # <input type="text" name="keywords">
        all_queries = None
        field = 'name'  # change accordingly
        for keyword in keywords.split(' '):  # keywords are splitted into words (eg: john science library)
            all_queries = Q(**{field + '__icontains': keyword})

        members = FamilyMember.objects.filter(all_queries).distinct()
        context['men'] = members
        return render(request, 'family/index.html', context)

    else:  # no data submitted
        members = FamilyMember.objects.all()
        context['men'] = members
        return render(request, 'family/index.html', context)


# return render(request, 'family/index.html', context=data)


def card(request, man_id):
    men = FamilyMember.objects.all()

    idLst = [man.id for man in men]

    if man_id not in idLst:
        raise Http404()

    man = FamilyMember.objects.get(id=man_id)
    parents = Relations.objects.filter(child=man_id)
    children = Relations.objects.filter(parent=man_id)
    if parents.exists():
        bAs = getBaS([p.parent for p in parents], man_id)
    else:
        bAs = []
    data = {
        "man": man,
        "parents": parents,
        "children": children,
        "bAs": bAs,
    }
    return render(request, 'family/card.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Данной страницы не существует</h1>")
