from django import forms
from .models import User_Detail,SubCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = User_Detail
        fields = ('sub_category',)

    sub_category = forms.ModelMultipleChoiceField(queryset=SubCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple)



