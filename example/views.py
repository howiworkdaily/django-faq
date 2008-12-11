from django.views.generic.list_detail import object_detail, object_list
from faq.views import question_list

def faq_list( request ):
    '''
    Display a typical FAQ view but more importantly an example of a basic way to "extend" or 
    "override" an existing view from a "reusable apps".
    
    '''
    
    #NOTE:
    #Again just for example - we pass along a custom extra_context dict so even if the view we're reusing sets it's own
    #we are still allowed to provide further details we may need by passing along this argument.
    extra = { 'page_title': 'FAQ Details' }
    
    #NOTE:
    #we also pass along our own custom template_name to override the existing one that's set.
    return question_list(request, template_name='faq/faq_list.html', extra_context=extra)
