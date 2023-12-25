from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('last_modified_date', 'date_of_creation',)

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Такое описание запрещено')

        return cleaned_data

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Такое название запрещено')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):

        is_active = self.cleaned_data.get('is_active')
        all_active_versions = Version.objects.all().filter(product=self.cleaned_data.get('product')).filter(
            is_active=True)
        if len(all_active_versions) >= 1 and is_active:
            if len(all_active_versions.filter(version_number=self.cleaned_data.get('version_number'))) == 0:
                raise forms.ValidationError('Вы можете выбрать только одну активную версию')
            else:
                return is_active
        return is_active
