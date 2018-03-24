from django import template

register = template.Library()

from blog.models import Post, Category

@register.inclusion_tag('blog/nav.html')
def tabs_list():
    tabs = Category.objects.all()
    return {'tabs': tabs}

@register.simple_tag()
def simple():
    test = Post.objects.all()
    return {'test':test}

