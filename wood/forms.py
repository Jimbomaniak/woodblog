from django.forms import ModelForm, Textarea, NumberInput
from .models import Comment, Purchase


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['comments_article', 'pub_date']
        widgets = {
            'comments_text': Textarea(attrs={
                'cols': '100%',
                'rows': 3,
                'placeholder': 'введите текст'
            })
        }
        labels = {
            'comments_text': '',
        }


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        exclude = ['product', 'buy_date']
        widgets = {
            'full_name': Textarea(attrs={
                'cols': '30%',
                'rows': 1,
                'style': 'resize: none',
                'placeholder': ''
            }),
            'address': Textarea(attrs={
                'cols': '30%',
                'rows': 2,
                'style': 'resize: none',
                'placeholder': 'город, адрес'
            }),
            'phone_num': Textarea(attrs={
                'cols': '30%',
                'rows': 1,
                'type': 'number',
                'style': 'resize: none',
                'placeholder': ''
            }),
            'comment': Textarea(attrs={
                'cols': '30%',
                'rows': 3,
                'style': 'resize: none',
                'placeholder': 'комментарий'
            })
        }
        labels = {
            'full_name': 'Полное имя:',
            'address': 'Адрес доставки:',
            'phone_num': 'Контактный телефон:',
        }