from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': '911 GT3 RS',
        'amount': 1,
        'description' : 'track focused rocketship'
    }

    return render(request, "main.html", context)