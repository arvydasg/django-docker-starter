"""Simple render."""

from django.shortcuts import render


def home(request):
    """Define render template."""
    return render(request, "index.html")
