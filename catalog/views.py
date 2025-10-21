from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Book

# Create your views here.
def hi(request):
    now = datetime.now()
    return HttpResponse(
        f'''
<html>
<body>
<h1>我將發動一次牛B的攻擊</h1>
<label>齊格飛.卡斯蘭娜</label>
{now}
</body>
</html>
        '''
    )
def index(request):
    return render(request, 'index.html')

def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book_list.html', {'books': books})

def book(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book.html', {'books': book})