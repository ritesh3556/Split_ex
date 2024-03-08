from django.contrib.auth.models import User
from django.shortcuts import render
import json
from django.http import JsonResponse , HttpResponse
from django.shortcuts import render
from .models import Expense, ExpenseParticipant, Balance

from django.contrib.auth.models import User

# Create a new user instance

def create_expense(request):
    # user = User.objects.create(username='user_1', email='user_1@example.com')
    #
    # # Set the password for the user
    # user.set_password('password')
    #
    # # Save the user instance
    # user.save()
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            amount = body.get("amount")
            description = body.get('description')
            expense_type = body.get('expense_type')
            paid_by_id = body.get('paid_by_id')
            participants_data = body.get('participants_data')

            # Check if the user who paid the expense exists
            print(",y usert "+str(User.objects.all()))
            try:
                paid_by = User.objects.get(id=paid_by_id)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User who paid the expense does not exist'}, status=400)

            # Create an Expense record
            expense = Expense.objects.create(
                amount=amount,
                description=description,
                expense_type=expense_type,
                paid_by=paid_by
            )

            # Iterate over participants data and create ExpenseParticipant records
            for participant_data in participants_data:
                participant_id, share = participant_data.split(':')
                try:
                    participant = User.objects.get(id=participant_id)
                except User.DoesNotExist:
                    return JsonResponse({'error': f'Participant with ID {participant_id} does not exist'}, status=400)
                ExpenseParticipant.objects.create(
                    expense=expense,
                    participant=participant,
                    share=share
                )

            return JsonResponse({'message': 'Expense created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
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
