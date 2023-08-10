from django.shortcuts import render, redirect

# Create your views here.
from .models import Profile, Dweet
from .forms import DweetForm

def dashboard(request):
    
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
        
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    #by default the user data is being sent to the page via request
    return render(request, "dwitter/dashboard.html", {"form":form,
                                                      "dweets":followed_dweets})

def profile_list(request):
    #Using the exclude method looks nw
    profiles = Profile.objects.exclude(user=request.user)

    context = {
        "profiles":profiles
    }

    return render(request, 'dwitter/profile_list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})
