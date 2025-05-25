from django.urls import reverse_lazy
from django.views import generic

from .models import PreparedItem
from .forms import PreparedItemForm

class PreparedItemListView(generic.ListView):
    model = PreparedItem
    paginate_by = 20
    template_name = 'memo/prepareditem_list.html'

class PreparedItemDetailView(generic.DetailView):
    model = PreparedItem
    template_name = 'memo/prepareditem_detail.html'

class PreparedItemCreateView(generic.CreateView):
    model = PreparedItem
    form_class = PreparedItemForm
    success_url = reverse_lazy('prepareditem_list')
    template_name = 'memo/prepareditem_form.html'

class PreparedItemUpdateView(generic.UpdateView):
    model = PreparedItem
    form_class = PreparedItemForm
    success_url = reverse_lazy('prepareditem_list')
    template_name = 'memo/prepareditem_form.html'

class PreparedItemDeleteView(generic.DeleteView):
    model = PreparedItem
    success_url = reverse_lazy('prepareditem_list')
    template_name = 'memo/prepareditem_confirm_delete.html'
