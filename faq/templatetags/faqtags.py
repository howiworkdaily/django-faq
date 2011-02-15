from django import template
from django.template import Library, Node, Variable, TemplateSyntaxError


from faq.models import Question

register = Library()

class FaqListNode(Node):
    def __init__(self, num, topic, varname):
        self.num, self.topic, self.varname = num, topic, varname

    def render(self, context):
        context[self.varname] = Question.objects.filter(topic__slug=self.topic)[:self.num]
        return ''

def do_faqs_for_topic(parser, token):
    """
    returns a list of 'count' faq's that belong to the given topic 
    the supplied topic argument must be in the slug format 'topic-name'
    
    Example usage:
    {% faqs_for_topic 5 topicslug as faqs %}
    """

    args = token.contents.split()
    if len(args) != 5:
        raise TemplateSyntaxError, "faqs_for_topic tag takes exactly four arguments"
    if args[3] != 'as':
        raise TemplateSyntaxError, "third argument to the faqs_for_topic tag must be 'as'"

    return FaqListNode(args[1], args[2], args[4])
    
register.tag('faqs_for_topic', do_faqs_for_topic)
