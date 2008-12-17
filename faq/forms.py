"""
Here we define a form for allowing site users to submit
a potential FAQ that they would like to see added.

From the user's perspective the question is not added automatically,
but actually it is, only it is added as inactive.
"""

import datetime
from django import forms
from faq.models import Question
from faq.enums import STATUS_INACTIVE

class SubmitFAQForm(forms.Form):
    question = forms.CharField(max_length=512,min_length=4,widget=forms.Textarea)
    answer   = forms.CharField(required=False,widget=forms.Textarea)

    def clean_answer(self):
        answer   = self.cleaned_data['answer']
        if not answer or len(answer) < 1:
            self.cleaned_data['answer'] = "No answer for this FAQ is available at this time."
        return self.cleaned_data['answer']

    def save(self, user=None):
        dt = datetime.datetime.now()
        slug_str = "anon-%d-%d-%d-%d-%d-%d" % ( dt.year, dt.month, dt.day,
                                                dt.hour, dt.minute, dt.second )
        question = self.cleaned_data['question']
        answer   = self.cleaned_data['answer']
        new_question = Question( text=question, answer=answer,
                                 slug=slug_str, sort_order = 999,
                                 protected = False, status = STATUS_INACTIVE )
        return new_question

