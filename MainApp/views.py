from django.shortcuts import render
import pandas as pd
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Candle
# Create your views here.


def home(request):
    return render(request,'index.html')


@csrf_exempt
def UploadCsv(request):
    context = {}
    file = request.FILES['csv_file'].temporary_file_path()
    df = pd.read_csv(file)
    for ind in df.index:
        model = Candle()
        model.open,model.close = df['OPEN'][ind],df['CLOSE'][ind]
        model.low,model.high = df['LOW'][ind],df['HIGH'][ind]
        model.date = df['DATE'][ind]
        model.volume = df['VOLUME'][ind]
        model.save()
    
    objs = Candle.objects.all()
    for index,obj in enumerate(objs):
        context[index]={
            "open": model.open,
            "close": model.close,
            "low":model.low,
            "high":model.high,
            "date":model.date,
            "volume":model.volume
        }
    return JsonResponse(data=context)