from django import forms

class BookForm(forms.form):
    title = forms.CharField(label="書名", max_length=200)
    author = forms.CharField(label="作者", max_length=100)
    published_data = forms.DateField(label="出版日期")
    isbn = forms.CharField(label="ISBN", max_length=13)