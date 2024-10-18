from django import template
register = template.Library()


@register.inclusion_tag('base/templatetags/site_header.html')
def site_header(*args,**kwargs):
    return {}

@register.inclusion_tag('base/templatetags/site_footer.html')

def site_footer(*args,**kwargs):
    return {}