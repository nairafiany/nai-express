from django.shortcuts import render

# Create your views here.
def show_main(request):
    products = [
        {
            'name': 'Tumbler',
            'price': '10000',
            'description': 'A cute little tumbler',
            'image': 'images/tumbler.avif',  
            'availability': 'In Stock', 
            'stock': 20, 
            'discount': '10%',  
        },
        {
            'name': 'Notebook',
            'price': '5000',
            'description': 'A small notebook for quick notes',
            'image': 'images/notebook.avif',
            'availability': 'Limited Stock',  
            'stock': 5,  
            'discount': '5%',  
        },
        {
            'name': 'Pen',
            'price': '2000',
            'description': 'A smooth writing pen',
            'image': 'images/pen.avif',
            'availability': 'Out of Stock', 
            'stock': 0,  
            'discount': 'No discount',  
        }
    ]

    context = {
        'website_title': 'Nai Express📦',
        'owner_name': 'Naira Shafiqa Afiany',
        'class_name': 'PBP C',
        'products': products,
    }

    return render(request, "main.html", context)
