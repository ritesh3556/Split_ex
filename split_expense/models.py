from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Expense(models.Model):
    EQUAL = 'EQUAL'
    EXACT = 'EXACT'
    PERCENT = 'PERCENT'
    EXPENSE_TYPES = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENT, 'Percentage'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES, default=EQUAL)  # Manually defining the default value
    created_at = models.DateTimeField(default=timezone.now)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.description} - {self.amount} - {self.created_at}"
class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(Expense, related_name='participants', on_delete=models.CASCADE)
    participant = models.ForeignKey(User, related_name='participated_expenses', on_delete=models.CASCADE)
    share = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.participant.username} - {self.share}"

class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balances')
    other_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_balances')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} owes {self.amount} to {self.other_user.username}"
