from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    context = {}
    return render(request, 'base/calcu.html', context)

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])  # Convert to float for numerical operations
        num2 = float(request.POST['num2'])  # Convert to float for numerical operations
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
            operator = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operator = '-'
        elif operation == 'multiply':
            result = num1 * num2
            operator = '*'
        elif operation == 'divide':
            if num2 == 0:
                return HttpResponse('Error: Division by zero is not allowed.')
            result = num1 / num2
            operator = '/'

        context = {
            'num1': num1,
            'num2': num2,
            'operator': operator,
            'result': result
        }
        return render(request, 'base/calcu.html', context)
    else:
        return HttpResponse('Method not allowed.')
