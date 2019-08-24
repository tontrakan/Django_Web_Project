from django.shortcuts import render
from MainPage.models import Mainpage

def Mainpage_index(request):
    mainpage = Mainpage.objects.all()
    context = {
        'mainpage': mainpage
    }
    return render(request, 'mainpage_index.html', context)

    
def Mainpage_detail(request, pk):
    mainpage = Mainpage.objects.get(pk=pk)
    context={
        'mainpage': mainpage
    }
    return render(request, 'mainpage_detail.html', context)
