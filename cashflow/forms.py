from django import forms
from .models import Record, Status, Type, Category


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['status', 'type', 'category', 'amount', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        type = cleaned_data.get('type')

        if category and type and category.type != type:
            raise forms.ValidationError(
                'Категория не соответствует выбранному типу.'
            )


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type', 'parent']

    def clean(self):
        cleaned_data = super().clean()
        parent = cleaned_data.get('parent')
        type = cleaned_data.get('type')
        if parent and parent.type != type:
            raise forms.ValidationError(
                'Родительская категория должна принадлежать тому же типу.'
            )
