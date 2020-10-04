from braces.views import AjaxResponseMixin, JSONResponseMixin
from django.views.generic import ListView, View

from live_search.forms import AirportForm
from live_search.models import Airport


class AirportListView(ListView):
    model = Airport
    template_name = 'live_search/airport_list.html'
    queryset = Airport.objects.none()

    def get_queryset(self):
        queryset = super(AirportListView, self).get_queryset()
        form = AirportForm(self.request.GET)
        if form.is_valid():
            city = form.cleaned_data['city']
            if city:
                queryset = Airport.objects.filter(city__istartswith=city)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AirportListView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = AirportForm(self.request.GET)
        return context


class AirportLiveSearchView(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        queryset = Airport.objects.filter(city__istartswith=self.request.GET.get('q'))[:20]
        return self.render_json_object_response(queryset)
