import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of lettings."""
    logger.info("Affichage de la liste des lettings")
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Display details for a single letting."""
    logger.info("Affichage du letting %s", letting_id)
    letting = get_object_or_404(Letting, id=letting_id)
    context = {"title": letting.title, "address": letting.address}
    return render(request, "lettings/letting.html", context)
