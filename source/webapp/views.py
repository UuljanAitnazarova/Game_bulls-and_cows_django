from django.shortcuts import render

from .check import Check, track_errors

history_dict = {}
round = 0


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
            
        except ValueError:
            message += 'The values should be integers'

        global round
        round += 1
        history_dict[round] = message

        return render(request, 'result.html', {'message' : message})



def history_view(request):
    return render(request, 'history.html', {'history_dict': history_dict })



