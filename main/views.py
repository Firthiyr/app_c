from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def	index(request) -> HttpResponse:
	context: dict[str, str] = {
			'title': 'Home - Головна',
			'content': 'CustomCraze Boutique',
	}
	return render(request, 'main/index.html', context)

def	about(request) -> HttpResponse:
	context: dict[str, str] = {
			'title': 'Home - Про нас',
			'content': 'Про нас',
	}
	return render(request, 'main/about.html', context)