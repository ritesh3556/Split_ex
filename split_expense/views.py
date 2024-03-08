from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from django.shortcuts import render
from .models import Expense, ExpenseParticipant, Balance


def create_expense(request):
    # Sample create expense view function
    if request.method == 'POST':
        # Assuming form data is submitted with keys: amount, description, expense_type, paid_by_id
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        expense_type = request.POST.get('expense_type')
        paid_by_id = request.POST.get('paid_by_id')

        # Assuming you have proper validation and error handling

        # Create expense
        expense = Expense.objects.create(
            amount=amount,
            description=description,
            expense_type=expense_type,
            paid_by_id=paid_by_id
        )

        # Assuming you have expense participants data in the request as well
        participants_data = request.POST.getlist('participants')
        for participant_data in participants_data:
            # Assuming each participant data contains participant_id and share
            participant_id, share = participant_data.split(':')
            ExpenseParticipant.objects.create(
                expense=expense,
                participant_id=participant_id,
                share=share
            )

        # Assuming you have logic to update balances as well

        return JsonResponse({'message': 'Expense created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def get_expense_details(request, expense_id):
    # Sample view to get expense details

    try:
        expense = Expense.objects.get(id=expense_id)
    except Expense.DoesNotExist:
        return JsonResponse({'error': 'Expense not found'}, status=404)

    # Assuming you need to return expense details along with participants
    participants = ExpenseParticipant.objects.filter(expense=expense)

    # Convert participants queryset to list of dictionaries
    participants_data = [{'participant_id': participant.participant_id, 'share': participant.share} for participant in
                         participants]

    response_data = {
        'expense_id': expense.id,
        'amount': expense.amount,
        'description': expense.description,
        'expense_type': expense.expense_type,
        'paid_by': expense.paid_by_id,
        'participants': participants_data
    }

    return JsonResponse(response_data)


def get_balance(request, user_id):
    # Sample view to get balance for a user
    balances = Balance.objects.filter(user_id=user_id)
    # Assuming you want to return balances data
    balance_data = [{'other_user_id': balance.other_user_id, 'amount': balance.amount} for balance in balances]
    return JsonResponse(balance_data, safe=False)
