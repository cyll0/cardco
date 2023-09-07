from django.shortcuts import render

def show_main(request):
    context = {
        'appName': 'cardco',
        'name': 'Clayton Nagle',
        'class': 'PBD KKI'
    }

    return render(request, 'main.html', context)