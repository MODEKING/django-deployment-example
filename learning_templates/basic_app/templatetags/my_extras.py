from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This is a custom template filter that i make that cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut) this is replaced by line 5
