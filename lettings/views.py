"""Views for the lettings application.

This module contains the views responsible for displaying
the list of lettings and the detail of a single letting.
"""

import logging
from django.shortcuts import render, get_object_or_404
from lettings.models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of lettings.

    Retrieves all Letting objects and renders the lettings index page.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse: The rendered lettings index page.
    """
    logger.info("Affichage de la liste des lettings")
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Display details for a single letting.

    Retrieves a single Letting by its identifier and renders
    the letting detail page. Raises a 404 error if the letting
    does not exist.

    Args:
        request: HttpRequest object representing the current request.
        letting_id: Primary key of the Letting to display.

    Returns:
        HttpResponse: The rendered letting detail page.
    """
    logger.info("Affichage du letting %s", letting_id)
    letting = get_object_or_404(Letting, id=letting_id)
    context = {"title": letting.title, "address": letting.address}
    return render(request, "lettings/letting.html", context)
