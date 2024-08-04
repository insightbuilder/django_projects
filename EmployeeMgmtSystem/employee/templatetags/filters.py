# employees/templatetags/filters.py

import base64
from django import template

register = template.Library()


@register.filter
def img_to_base64(image):
    """Convert image bytes to base64 string."""
    return base64.b64encode(image.getvalue()).decode("utf-8")
