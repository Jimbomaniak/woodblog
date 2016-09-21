from django.forms import ModelForm, Textarea, EmailInput, NumberInput
from .models import Comment, Purchase


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['comments_article', 'pub_date']
        widgets = {
            'comments_text': Textarea(attrs={
                'rows': 3,
                'placeholder': 'введите текст',
                'style': 'resize: none; width: 100%',
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
                'rows': 1,
                'style': 'resize: none; width: 100%',
                'placeholder': 'Имя'
            }),
            'phone_num': NumberInput(attrs={
                'placeholder': 'Телефон',
                'style': 'width: 100%',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Email',
                'style': 'width: 100%',
            }),
            'address': Textarea(attrs={
                'rows': 2,
                'style': 'resize: none; width: 100%',
                'placeholder': 'Куда доставить'
            }),
            'comment': Textarea(attrs={
                'rows': 2,
                'style': 'resize: none; width: 100%',
                'placeholder': 'Комментарий',
            })
        }
        labels = {
            'full_name': '',
            'address': '',
            'phone_num': '',
            'email': '',
            'comment': '',
        }
