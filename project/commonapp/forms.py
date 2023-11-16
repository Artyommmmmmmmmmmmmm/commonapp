from django import forms
from .models import New, Article
from django.core.exceptions import ValidationError

class NewForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    class Meta:
       model = New
       fields = ['title', 'text', 'category']
    def clean_title(self):
        title = self.cleaned_data["title"]
        if title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return title

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        # print(text)
        # if text is not None and len(text) < 20:
        #     raise ValidationError({
        #         "text": "Описание не может быть менее 20 символов."
        #     })
    
        title = cleaned_data.get("title")
        # print(title)
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data
    
class ArticleForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    class Meta:
       model = Article
       fields = ['title', 'text', 'category']
    def clean_title(self):
        title = self.cleaned_data["title"]
        if title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return title

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        # print(text)
        # if text is not None and len(text) < 20:
        #     raise ValidationError({
        #         "text": "Описание не может быть менее 20 символов."
        #     })
    
        title = cleaned_data.get("title")
        # print(title)
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data