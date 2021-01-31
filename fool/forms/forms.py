
from django import forms
from fool.models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    title = forms.CharField(max_length=60)
    body = forms.CharField(
        max_length=800,
        widget=forms.Textarea(),
        help_text='Submit a Comment'
    )

    class Meta:
        model = Comment
        fields = ('name', 'title', 'body')

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        name = cleaned_data.get('name')
        title = cleaned_data.get('title')
        body = cleaned_data.get('body')
        if not name and not title and not body:
            raise forms.ValidationError('You have to write something!')
