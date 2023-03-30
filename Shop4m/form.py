from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=5, max_length=255)
    price = forms.FloatField(required=True)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()


class CommentsCreateForm(forms.Form):
    text = forms.CharField(max_length=355)