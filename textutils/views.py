# i have created this file......
from django.http import HttpResponse
from django.shortcuts import render     #importing render..
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def analize(request):
    djtext=request.POST.get('text','default')
    print(djtext)
    removepuc=request.POST.get('removepuc','off')
    capatalize=request.POST.get('capatalize','off')
    newlineremove=request.POST.get('newlineremove','off')
    charcount = request.POST.get('charcount', 'off')
    print( removepuc)
    if removepuc=="on":
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analized=""
        for char in djtext:
            if char not in punctuations:
                analized= analized+char
        param = {'purpose': 'remove punctuations', 'analized_text': analized}
        djtext=analized
       # return render(request,'analize.html',param)               #when i was using elif statement my site takes only one input and returns result but now with this djtext gets updataed for every on
    if capatalize=="on":
        analized=""
        for char in djtext:
            analized=analized+char.upper()
        param = {'purpose': 'capatalize', 'analized_text': analized}
        djtext = analized
        #return render(request, 'analize.html', param)
    if newlineremove=="on":
        analized=""
        for char in djtext:
            if(char!='\n' and char!='\r'):
                analized=analized+char
        param = {'purpose': 'newlineremove', 'analized_text': analized}
        djtext = analized
        #return render(request, 'analize.html', param)
    if charcount=="on":
        count = 0

        for i in range(0, len(djtext)):
            if (djtext[i] != ' '):
                count = count + 1;
        param = {'purpose': 'charcount', 'analized_text':count}
    if(removepuc!="on"and capatalize!="on"and charcount!="on"and newlineremove!="on"):
        return HttpResponse('ERROR')
    return render(request, 'analize.html', param)

 #   return HttpResponse("charcount")   this is used to return statements ..