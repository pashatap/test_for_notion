from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from apps.system_for_study.models import Product, Group, AccessRequest


class ProductView(ListView):
    model = Product
    template_name = 'system_for_study/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_groups = Group.objects.filter(students=user)
        products = Product.objects.filter(group__in=user_groups)

        context['products'] = products
        return context


class AllProductsView(ListView):
    model = Product
    template_name = 'system_for_study/all_product.html'
    context_object_name = 'all_products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'system_for_study/product_detail.html'
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lesson_set.all()
        return context


class CreateOrderView(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        product = Product.objects.get(pk=pk)
        user = self.request.user
        status = 'pending'
        AccessRequest.objects.create(status=status, product=product, user=user)
        return redirect('system:all_product')
