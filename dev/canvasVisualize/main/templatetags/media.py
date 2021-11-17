from django import template

register = template.Library()

@register.filter
def media(arg1):
    """concatenate arg1 & arg2"""
    return f"https://cvisualize-code.s3.eu-west-2.amazonaws.com/media/code/{arg1}"