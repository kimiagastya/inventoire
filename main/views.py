from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_identitas' : 'I Putu Gede Kimi Agastya',
        'kelas_identitas' : 'PBP D',
        # 'name': '911 GT3 RS',
        # 'amount': 1,
        # 'description' : 'track focused rocketship'
    }

    return render(request, "main.html", context)