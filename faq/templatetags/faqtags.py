from __future__ import absolute_import

from django import template
from ..enums import STATUS_ACTIVE
from ..models import Question, Topic

register = template.Library()

class FaqsForTopicNode(template.Node):
    def __init__(self, num, topic, varname):
        self.num = template.Variable(num)
        self.topic = template.Variable(topic)
        self.varname = varname

    def render(self, context):
        try:
            num = self.num.resolve(context)
            topic = self.topic.resolve(context)
        except template.VariableDoesNotExist:
            return ''
            
        if isinstance(topic, Topic):
            qs = Question.objects.filter(topic=topic)
        else:
            qs = Question.objects.filter(topic__slug=topic)
        
        context[self.varname] = qs.filter(status=STATUS_ACTIVE)[:num]

        return ''

@register.tag
def faqs_for_topic(parser, token):
    """
    Returns a list of 'count' faq's that belong to the given topic
    the supplied topic argument must be in the slug format 'topic-name'
    
    Example usage::
    
        {% faqs_for_topic 5 "my-slug" as faqs %}
    """

    args = token.split_contents()
    if len(args) != 5:
        raise template.TemplateSyntaxError("%s takes exactly four arguments" % args[0])
    if args[3] != 'as':
        raise template.TemplateSyntaxError("third argument to the %s tag must be 'as'" % args[0])

    return FaqsForTopicNode(args[1], args[2], args[4])

class FaqNode(template.Node):
    def __init__(self, num, varname):
        self.num = template.Variable(num)
        self.varname = varname

    def render(self, context):
        try:
            num = self.num.resolve(context)
        except template.VariableDoesNotExist:
            return ''
            
        context[self.varname] = Question.objects.filter(status=STATUS_ACTIVE)[:num]
        return ''

@register.tag
def faq_list(parser, token):
    """
    returns a generic list of 'count' faq's to display in a list 
    ordered by the faq sort order.

    Example usage::
    
        {% faq_list 15 as faqs %}
    """
    args = token.split_contents()
    if len(args) != 4:
        raise template.TemplateSyntaxError("%s takes exactly three arguments" % args[0])
    if args[2] != 'as':
        raise template.TemplateSyntaxError("second argument to the %s tag must be 'as'" % args[0])

    return FaqNode(args[1], args[3])
