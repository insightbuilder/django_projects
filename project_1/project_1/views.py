from django.shortcuts import render, redirect

# Places to Visit in Django Land
places_to_visit = [
    "Django Park",
    "View Point",
    "ORM Lake",
    "Admin Gardens",
]

# Things to Do in Django Land
things_to_do = [
    "Hiking Trails",
    "Django Falls",
    "Sunset Ridge",
    "DjangoCon",
]

# Famous People of Django Land
famous_people = [
    "John Doe - Dev",
    "Jane Smith - Adv",
    "Michael Johnson",
    "Sarah Williams",
]

# Tales of Django Land
tales_of_django = [
    "Django's Legacy",
    "Django's Forest",
    "Django's Journey",
    "Django's River",
]
lists = [
    "places_to_visit",
    "things_to_do",
    "famous_people",
    "tales_of_django",
]

def INDEX(request):
    print('this is request pack',request.GET)
    context = {
        "lists":lists,
        "visit_places":places_to_visit,
        "do_things":things_to_do,
        "famous_people":famous_people,
        "tales":tales_of_django
    }
    
    return render(request, 'single_pjt.html',context)

def SINGLE(request):
    return render(request, 'single_page.html')

def ASSEMBLED(request):
    return render(request, 'assembled_page.html')

def PAGE_NOT_FOUND(request):
    return render(request, '404.html')
