from django.template import Library
from ..models import Region

register = Library()


@register.simple_tag
def all_region():
    return Region.objects.all()