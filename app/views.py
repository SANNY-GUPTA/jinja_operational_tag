from django.shortcuts import render

def apple(request):
    d={'a':10,'name':'start','b':500,'c':2000}
    return render(request,'sa.html',d)
