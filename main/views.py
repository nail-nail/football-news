from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406407796 ',
        'name': 'Naila Khadijah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
