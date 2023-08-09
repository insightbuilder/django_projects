from django.shortcuts import render

# Create your views here.

def SUM(request):
    if request.method == 'POST':
        # Get the numbers from the form
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))

        # Calculate the sum
        sum_result = num1 + num2
        
        #initialize / get the existing data in session as a list

        stored_data = request.session.get('stored_data',[])

        # Store the numbers in session
        stored_data.append({'num1':num1,
                           'num2':num2})

        request.session['stored_data'] = stored_data

        context ={
            'sum_result':sum_result,
            'stored_data': stored_data
        }
        return render(request, 'sum_numbers.html', context)

    return render(request, 'sum_numbers.html')

