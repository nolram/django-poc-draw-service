import random
from unicodedata import name

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .forms import DrawForm
from .models import Winner, Draw


class Index(View):
    template_name = 'app_draw/index.html'
    form_class = DrawForm
    template_winner = 'app_draw/winners.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            participants = form.cleaned_data["participants"].splitlines()
            quantity = form.cleaned_data["quantity"]
            winners = random.sample(participants, k=quantity)
            
            draw = Draw.objects.create(draw_name=form.cleaned_data["draw_name"])

            for winner in winners:
                Winner.objects.create(name=winner, fk_draw=draw)

            return render(
                request,
                self.template_winner,
                {"form": form, "winners": winners},
            )
        return render(request, self.template_name, {"form": form})

class GetDraw(DetailView):
    template_name = 'app_draw/winners.html'
    model = Draw
