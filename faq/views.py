from __future__ import absolute_import
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic.list_detail import object_detail, object_list
from .models import Question
from .forms import SubmitFAQForm

def question_detail(request, slug, template_name='faq/question_detail.html', extra_context={}):
    """
    Displays an individual question.
    """
    return object_detail(
        request,
        template_name = template_name,
        extra_context = extra_context,
        slug = slug,
        slug_field = 'slug',
        queryset = Question.objects.active(user=request.user),
    )    
        
def question_list(request, template_name='faq/question_list.html',
                  extra_context={}, group=False):
    '''
    Displays a list of all the questions.
    '''
    query_set = Question.objects.active(group=group,user=request.user)
    
    if len(query_set) == 0:
	raise Http404()

    last_update = query_set.values('updated_on').order_by('-updated_on',)[0]    
    extra = { 'updated_on': last_update['updated_on'] }
 
    extra.update( extra_context )
    
    return object_list(
        request,
        template_name = template_name,
        extra_context = extra,
        queryset = query_set
    )

def submit_faq(request, form_class=SubmitFAQForm,
               template_name="faq/submit_question.html",
               success_url=None, extra_context={}):
    
    if request.user.is_authenticated():
        instance = Question(created_by=request.user)
    else:
        instance = Question()
        
    form = form_class(request.POST or None, instance=instance)
    if form.is_valid():
        question = form.save()
        # Set up a confirmation message for the user
        messages.success(request, 
            _("Your question was submitted and will be reviewed by for inclusion in the FAQ."),
            fail_silently=True,
        )
        return redirect(success_url if success_url else "faq_question_list")

    context = {'form': form}
    context.update(extra_context)
    return render(request, template_name, context)
