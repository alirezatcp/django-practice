from django import forms

from library.models import Book

class BookForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    email = forms.EmailField(required=False)

    # if we want to add filter to one field we should use this structure to function name: clean_<field_name>
    # add a filter to author that it length should be bigger than 3 chars.
    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) < 3:
            message = 'author name should be bigger than 3 characters.'
            raise forms.ValidationError(message)

        return author 


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title',)