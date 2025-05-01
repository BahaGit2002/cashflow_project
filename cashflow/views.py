from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from .models import Record, Status, Type, Category
from .forms import RecordForm, StatusForm, TypeForm, CategoryForm
from .services import RecordService, ReferenceService


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = RecordService.filter_records(self.request)
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        return context


class RecordCreateView(View):
    def get(self, request):
        form = RecordForm()
        return render(
            request, 'record_form.html',
            {'form': form, 'title': 'Создать запись'}
        )

    def post(self, request):
        success, form = RecordService.create_record(request)
        if success:
            return redirect('cashflow_app:index')
        return render(
            request, 'record_form.html',
            {'form': form, 'title': 'Создать запись'}
        )


class RecordEditView(View):
    def get(self, request, pk):
        record = get_object_or_404(Record, pk=pk)
        form = RecordForm(instance=record)
        return render(
            request, 'record_form.html', {
                'form': form, 'title': 'Редактировать запись', 'record': record
            }
        )

    def post(self, request, pk):
        record = get_object_or_404(Record, pk=pk)
        success, form = RecordService.update_record(request, record)
        if success:
            return redirect('cashflow_app:index')
        return render(
            request, 'record_form.html', {
                'form': form, 'title': 'Редактировать запись', 'record': record
            }
        )


class RecordDeleteView(View):
    def get(self, request, pk):
        record = get_object_or_404(Record, pk=pk)
        return render(
            request, 'record_form.html',
            {'record': record, 'title': 'Удалить запись'}
        )

    def post(self, request, pk):
        record = get_object_or_404(Record, pk=pk)
        RecordService.delete_record(request, record)
        return redirect('cashflow_app:index')


class ManageReferencesView(TemplateView):
    template_name = 'manage_references.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_form'] = StatusForm(prefix='status')
        context['type_form'] = TypeForm(prefix='type')
        context['category_form'] = CategoryForm(prefix='category')
        context['statuses'] = Status.objects.all()
        context['types'] = Type.objects.all()
        context['categories'] = Category.objects.all()
        return context


class GetCategoriesAPIView(View):
    def get(self, request, type_id):
        return ReferenceService.get_categories(type_id)


class StatusAddAPIView(View):
    def post(self, request):
        return ReferenceService.create_status(request)


class StatusEditAPIView(View):
    def post(self, request):
        return ReferenceService.update_status(request, request.POST.get('id'))


class StatusDeleteAPIView(View):
    def post(self, request):
        return ReferenceService.delete_status(request, request.POST.get('id'))


class TypeAddAPIView(View):
    def post(self, request):
        return ReferenceService.create_type(request)


class TypeEditAPIView(View):
    def post(self, request):
        return ReferenceService.update_type(request, request.POST.get('id'))


class TypeDeleteAPIView(View):
    def post(self, request):
        return ReferenceService.delete_type(request, request.POST.get('id'))


class CategoryAddAPIView(View):
    def post(self, request):
        return ReferenceService.create_category(request)


class CategoryEditAPIView(View):
    def post(self, request):
        return ReferenceService.update_category(
            request, request.POST.get('id')
        )


class CategoryDeleteAPIView(View):
    def post(self, request):
        return ReferenceService.delete_category(
            request, request.POST.get('id')
        )
