# i have created this file' - Zobia
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def analyze(request):
   
    text = request.POST.get('text','default'  )
   
    removepunc = request.POST.get('removepunc','off'  )
    fullcaps = request.POST.get('fullcaps','off'  )
    newlineremover = request.POST.get('newlineremover','off'  )
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount','off')
   
    if removepunc == 'on':
   
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        text = analyzed
   
    if fullcaps == 'on':
        analyzed =''
        for char in text:
            analyzed += char.upper()

        params = {'purpose':'Change to Upertext','analyzed_text':analyzed}
        text = analyzed
    
    if newlineremover == 'on':
        analyzed =''
        for char in text:
            if char !="\n" and char !="\r":
                analyzed += char

        params = {'purpose':'Change to Upertext','analyzed_text':analyzed}
        text = analyzed
    
    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(text):
            if index != (len(text)-1):
                if not(text[index] == " " and text[index+1]==" " ):
                    analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        text = analyzed

    if charcount == 'on':
        analyzed = 0

        for char in text:
            analyzed += 1

        params = {'purpose':'Change to Upertext','analyzed_text':(analyzed,text)}
        
    if removepunc != 'on' and fullcaps != 'on' and newlineremover!= 'on' and spaceremover != 'on' and charcount != 'on':
        return HttpResponse("ERROR")
    
    return render(request,'analyze.html', params )
