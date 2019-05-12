from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    dic = {}
    for i in words:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    return render(request, 'result.html', {'full': text, 'len': len(words), 'dic': dic.items()})
