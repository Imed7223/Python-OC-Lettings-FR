from django.shortcuts import render


def index(request):
    """Display the home page."""
    return render(request, "index.html")


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, "404.html", status=404)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, "500.html", status=500)
