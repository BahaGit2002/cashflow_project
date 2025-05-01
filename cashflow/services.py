from django.db import IntegrityError
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Record, Status, Type, Category
from .forms import RecordForm, StatusForm, TypeForm, CategoryForm


class RecordService:
    @staticmethod
    def filter_records(request):
        records = Record.objects.all()
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        status_id = request.GET.get('status')
        type_id = request.GET.get('type')
        category_id = request.GET.get('category')

        if date_from:
            records = records.filter(created_at__gte=date_from)
        if date_to:
            records = records.filter(created_at__lte=date_to)
        if status_id:
            records = records.filter(status_id=status_id)
        if type_id:
            records = records.filter(type_id=type_id)
        if category_id:
            records = records.filter(category_id=category_id)

        return records

    @staticmethod
    def create_record(request):
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно создана.')
            return True, None
        return False, form

    @staticmethod
    def update_record(request, record):
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно обновлена.')
            return True, None
        return False, form

    @staticmethod
    def delete_record(request, record):
        record.delete()
        messages.success(request, 'Запись успешно удалена.')
        return True


class ReferenceService:
    @staticmethod
    def create_status(request):
        form = StatusForm(request.POST, prefix='status')
        if form.is_valid():
            try:
                status = form.save()
                return JsonResponse(
                    {
                        'success': True,
                        'id': status.id,
                        'name': status.name
                    }
                )
            except IntegrityError:
                return JsonResponse(
                    {
                        'success': False,
                        'error': 'Статус с таким названием уже существует.'
                    }
                )
        return JsonResponse(
            {
                'success': False,
                'error': 'Неверные данные формы.'
            }
        )

    @staticmethod
    def update_status(request, status_id):
        status = get_object_or_404(Status, id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            try:
                status = form.save()
                return JsonResponse(
                    {
                        'success': True,
                        'id': status.id,
                        'name': status.name
                    }
                )
            except IntegrityError:
                return JsonResponse(
                    {
                        'success': False,
                        'error': 'Статус с таким названием уже существует.'
                    }
                )
        return JsonResponse(
            {
                'success': False,
                'error': 'Неверные данные формы.'
            }
        )

    @staticmethod
    def delete_status(request, status_id):
        status = get_object_or_404(Status, id=status_id)
        if Record.objects.filter(status=status).exists():
            return JsonResponse(
                {
                    'success': False,
                    'error': 'Нельзя удалить статус, используемый в записях.'
                }
            )
        status.delete()
        return JsonResponse({'success': True})

    @staticmethod
    def create_type(request):
        form = TypeForm(request.POST, prefix='type')
        if form.is_valid():
            try:
                type_obj = form.save()
                return JsonResponse(
                    {
                        'success': True,
                        'id': type_obj.id,
                        'name': type_obj.name
                    }
                )
            except IntegrityError:
                return JsonResponse(
                    {
                        'success': False,
                        'error': 'Тип с таким названием уже существует.'
                    }
                )
        return JsonResponse(
            {
                'success': False,
                'error': 'Неверные данные формы.'
            }
        )

    @staticmethod
    def update_type(request, type_id):
        type_obj = get_object_or_404(Type, id=type_id)
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            try:
                type_obj = form.save()
                return JsonResponse(
                    {
                        'success': True,
                        'id': type_obj.id,
                        'name': type_obj.name
                    }
                )
            except IntegrityError:
                return JsonResponse(
                    {
                        'success': False,
                        'error': 'Тип с таким названием уже существует.'
                    }
                )
        return JsonResponse(
            {
                'success': False,
                'error': 'Неверные данные формы.'
            }
        )

    @staticmethod
    def delete_type(request, type_id):
        type_obj = get_object_or_404(Type, id=type_id)
        if Record.objects.filter(type=type_obj).exists():
            return JsonResponse(
                {
                    'success': False,
                    'error': 'Нельзя удалить тип, используемый в записях.'
                }
            )
        type_obj.delete()
        return JsonResponse({'success': True})

    @staticmethod
    def create_category(request):
        form = CategoryForm(request.POST, prefix='category')
        if form.is_valid():
            try:
                category = form.save()
                return JsonResponse(
                    {
                        'success': True,
                        'id': category.id,
                        'name': category.name,
                        'full_name': str(category),
                        'type': category.type.id,
                        'type_name': category.type.name,
                        'parent': category.parent.id if category.parent else None,
                        'parent_name': str(
                            category.parent
                        ) if category.parent else None
                    }
                )
            except IntegrityError:
                return JsonResponse(
                    {
                        'success': False,
                        'error': 'Категория с таким названием и типом уже существует.'
                    }
                )
        return JsonResponse(
            {
                'success': False,
                'error': 'Неверные данные формы.'
            }
        )

    @staticmethod
    def update_category(request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            try:
                category = form.save()
                return JsonResponse(
                    {
                        'success': True,
                        'id': category.id,
                        'name': category.name,
                        'full_name': str(category),
                        'type': category.type.id,
                        'type_name': category.type.name,
                        'parent': category.parent.id if category.parent else None,
                        'parent_name': str(
                            category.parent
                        ) if category.parent else None
                    }
                )
            except IntegrityError:
                return JsonResponse(
                    {
                        'success': False,
                        'error': 'Категория с таким названием и типом уже существует.'
                    }
                )
        return JsonResponse(
            {
                'success': False,
                'error': 'Неверные данные формы.'
            }
        )

    @staticmethod
    def delete_category(request, category_id):
        category = get_object_or_404(Category, id=category_id)
        if Record.objects.filter(
                category=category
        ).exists() or Category.objects.filter(
            parent=category
        ).exists():
            return JsonResponse(
                {
                    'success': False,
                    'error': 'Нельзя удалить категорию, используемую в записях или имеющую подкатегории.'
                }
            )
        category.delete()
        return JsonResponse({'success': True})

    @staticmethod
    def get_categories(type_id):
        categories = Category.objects.filter(type_id=type_id).values(
            'id', 'name', 'parent_id'
        )
        return JsonResponse({'categories': list(categories)})
