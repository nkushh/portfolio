from django.shortcuts import render

# Create your views here.
def dashboard(request):
	return render(request, "site_engine/dashboard.html", {})
