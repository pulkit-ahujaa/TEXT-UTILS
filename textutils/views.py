from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcounter = request.POST.get('charcounter','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = ""

        for char in djtext:
            analyzed = analyzed + char.upper()

        params = { 'purpose': 'changed to upper case', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""

        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'removed line ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (charcounter=='on'):

        analyzed =""
        count=0

        for char in djtext:
            if char !=" ":
                count=count+1


        params = {'purpose': 'char counter ', 'analyzed_text': count}
        return render(request , 'analyze.html', params)



    else:
        return HttpResponse("Erro")
