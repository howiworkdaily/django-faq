import datetime
from django.views.generic.list_detail import object_detail, object_list
from faq.models import Question

def question_detail(request, slug, template_name='faq/question_detail.html',
                    extra_context=None):
    """
    Displays an invidual question.
    """
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra_context or {},
        slug = slug,
        slug_field = 'slug',
        queryset = Question.objects.active(),
    )

def question_list(request, template_name='faq/question_list.html',
                  extra_context=None):
    """
    Displays a list of all the questions.
    
    """
    # NOTE:
    # this below is NOT NEEDED really so I would remove but I think it's a
    # good example for people to see how they could "extend" their existing
    # extra_context using a parameter value to allow developers to make their
    # app more reusable we set the below dict value and then allow the user
    # to pass along their own if they we then populate the user supplied
    # extra_context using the update method

    if extra_context is None:
        extra_context = {}
    extra = {
        'created_on': datetime.datetime.now()
    }
    extra.update(extra_context)
    return object_list(
        request,
        template_name = template_name,
        extra_context = extra,
        queryset = Question.objects.active(),
    )
