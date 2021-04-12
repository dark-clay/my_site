from django.shortcuts import render
from django.http import HttpResponse


from .models import News


def index(request):
    news = News.objects.all()
    return render(request, "news/index.html", {'news': news, 'title': 'Список новостей'})


def test(request):
    news = News.objects.all()
    return render(request, 'news/test.html', {'news': news, 'title': 'Список новостей'})








    #news = News.objects.all()
    #res = '<h1>Список новостей</h1>>'
    #for item in news:
    #    res += f'<div>\n<p>{item.title}</p>' \
     #          f'\n<p>{item.content}</p>' \
      #         f'</div>' '<h4>дата создания</h4>' \
       ##       f'\n<hr\n>'
    #return HttpResponse(res)
    #return render(request, 'main/index.html')



