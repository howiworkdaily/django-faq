
from django import template
from django.template import TemplateSyntaxError

from faq.models import Question

register = template.Library()

class FaqsForObjectNode(template.Node):
    def __init__(self, obj, context_var_name):
        self.obj_var = template.Variable(obj)
        self.context_var_name = context_var_name
    
    def render(self, context):
        obj = self.obj_var.resolve(context)
        context[self.context_var_name] = Question.objects.get_for_object(obj)
        return ""

def do_faqs_for_object(parser, token):
    """
    Retrieves a list of ``Question`` objects associated with an object and
    stores them in a context variable.
    
    Usage::
        
        {% faqs_for_object [object] as [varname] %}
    
    Example::
        
        {% faqs_for_object product as product_questions %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError("%s tag requires exactly three arguments" % bits[0])
    if bits[2] != "as":
        raise TemplateSyntaxError("second argument to %s tag must be 'as'" % bits[0])
    return FaqsForObjectNode(bits[1], bits[3])

register.tag("faqs_for_object", do_faqs_for_object)
