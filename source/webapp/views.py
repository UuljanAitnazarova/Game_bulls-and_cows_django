from django.shortcuts import render

from .check import Check, track_errors

def game_view(request):
    if request.method == 'GET':
        return render(request, 'game.html')
    elif request.method == 'POST':
        try:
            message = ''
            numbers = list(map(int, request.POST.get('numbers').split(' ')))
            print(numbers)
            error = track_errors(numbers)
            if error:
                message += error
            else:
                check = Check(numbers)
                result = check.check_values()
                message += result
            return render(request, 'history.html', {'message' : message})
        except ValueError:
            message += 'The values should be integers'






