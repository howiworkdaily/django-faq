from django import template
from django.template import Library, Node, Variable, TemplateSyntaxError


from faq.models import Question

register = Library()


class FaqListNode(Node):
    def __init__(self, num, topic, varname):
        self.num, self.topic, self.varname = num, topic, varname

    def render(self, context):
        context[self.varname] = Question.objects.active(topic__slug=self.topic)[:self.num]
        return ''


def do_faqs_for_topic(parser, token):
    """
    returns a list of 'count' faq's that belong to the given topic
    the supplied topic argument must be in the slug format 'topic-name'
    
    Example usage:
    {% faqs_for_topic [5] [topicslug] as [faqs] %}
    """

    args = token.contents.split()
    if len(args) != 5:
        raise TemplateSyntaxError, "faqs_for_topic tag takes exactly four arguments"
    if args[3] != 'as':
        raise TemplateSyntaxError, "third argument to the faqs_for_topic tag must be 'as'"

    return FaqListNode(args[1], args[2], args[4])
    
register.tag('faqs_for_topic', do_faqs_for_topic)


class FaqNode(Node):
    def __init__(self, num, varname):
        self.num, self.varname = num, varname

    def render(self, context):
        context[self.varname] = Question.objects.active()[:self.num]
        return ''

def do_faq_list(parser, token):
    """
    returns a generic list of 'count' faq's to display in a list 
    ordered by the faq sort order.

    Example usage:
    {% faq_list [5] as [faqs] %}
    """

    args = token.contents.split()
    if len(args) != 4:
        raise TemplateSyntaxError, "faq_list tag takes exactly four arguments"
    if args[2] != 'as':
        raise TemplateSyntaxError, "second argument to the faq_list tag must be 'as'"

    return FaqNode(args[1], args[3])

register.tag('faq_list', do_faq_list)
