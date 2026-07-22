import random

from django.shortcuts import render
from django.views.generic.edit import FormView

from . import forms


class IndexView(FormView):
    template_name = 'solver/index.html'
    form_class = forms.QuadraticForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = forms.QuadraticForm()
        form.initial = {'a': random.randint(1, 10), 'b': random.randint(1, 10), 'c': random.randint(1, 10)}
        context['form'] = form
        return context

    @staticmethod
    def solve(a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return None, None
        elif discriminant == 0:
            return -b / (2 * a), -b / (2 * a)
        else:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            return x1, x2

    def form_valid(self, form):
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        x1, x2 = self.solve(a, b, c)
        print(x1, x2)
        form = forms.QuadraticForm()
        form.initial = {'a': random.randint(1, 10), 'b': random.randint(1, 10), 'c': random.randint(1, 10)}
        return render(self.request, 'solver/index.html', {'x1': x1, 'x2': x2, 'form': form})

