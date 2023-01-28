from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, ListView
from .forms import OrderItemForm
from accounts.models import Vendee, OrderItems


class CreateDeliveryOrderItem(CreateView):
    form_class = OrderItemForm
    template_name = 'vendee/create_order_item.html'

    def form_valid(self, form):
        form.instance.vendee = self.request.user.user_vendee
        form.save()
        return redirect('create_order_item')


class DeliveryOrderItemListView(ListView):
    model = OrderItems
    queryset = OrderItems.objects.all()
    context_object_name = 'order_items'
    template_name = 'order_items.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('search')
        print(query)
        if query:
            qs = OrderItems.objects.filter(id=query)

            return qs
        return qs
