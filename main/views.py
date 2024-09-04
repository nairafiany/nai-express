from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Tumbler',
        'price': '10000',
        'description': 'Lorem ipsum'
    }

    return render(request, "main.html", context)