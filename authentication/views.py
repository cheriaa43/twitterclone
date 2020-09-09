from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from authentication import forms
from django.views.generic import TemplateView


# Create your views here.
class LoginView(TemplateView):
    
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "generic_form.html", {"form": form})
        
    def post(self, request):
        form = forms.LoginForm()
        if request.method == "POST":
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(request, username=data.get("username"), password=data.get("password"))
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse("home"))
                return render(request, "generic_form.html", {"form": form})
        

class LogoutView(TemplateView):
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("home"))
