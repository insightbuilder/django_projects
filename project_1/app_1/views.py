from django.shortcuts import render

# Historical Timelines in Django Land
historical_timelines = [
    "1840 - Founding",
    "1895 - First Rails",
    "1950 - Django Landmark",
    "2005 - Django Framework",
]

# Geographical Anomalies in Django Land
geographical_anomalies = [
    "Rainbow Valley",
    "Misty Peaks",
    "Enchanted Caves",
    "Whispering Woods",
]

# Condiments of Django Land
condiments = [
    "Whisker Sauce",
    "Spicyberry Jam",
    "Meadow Honey",
    "Forest Truffle",
]

# Innovative Products by Django People
innovative_products = [
    "Skyglider Drone",
    "EcoHarvest Machine",
    "DigiGlobe",
    "SwiftCycle",
]

lists = [
    "Condiments",
    "Innovative_products",
    "Historical_timelines",
    "Geographical_anomalies",
    ]
# Create your views here.

def APP_INDEX(request):
    context = {
        "lists":lists,
        "inno_pdts":innovative_products,
        "condiments":condiments,
        "anoms":geographical_anomalies,
        "timelines":historical_timelines
    }
    return render(request, 'single_app.html',context)
