from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'personal_expense/index.html')
