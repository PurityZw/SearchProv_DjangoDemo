from django.shortcuts import render
from area_demand.models import AreaInfo
from django.http import JsonResponse,HttpResponse
# Create your views here.
# /index
def index(request):
    return render(request, 'area_demand/index.html')

# /areas
def areas(request):
    areas_addr = AreaInfo.areas.my_all()
    return render(request, 'area_demand/areas.html', {'areas_addr': areas_addr})

# /prov     获取所有省份信息
def prov(request):
    provinces = AreaInfo.areas.filter(aParent__isnull=True)
    prov_arr = []
    for province in provinces:
        prov_arr.append((province.id, province.atitle))
    return JsonResponse({'data': prov_arr})


# /city
def city(request, id):
    city_arr = []
    cities = AreaInfo.areas.filter(aParent_id=id)
    for city_area in cities:
        city_arr.append((city_area.id, city_area.atitle))
    return JsonResponse({'data': city_arr})


