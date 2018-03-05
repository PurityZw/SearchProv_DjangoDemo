from django.template import Library


register = Library()


@register.filter
def mod(value):
    # if value.id == 990000:
        return value % 2
