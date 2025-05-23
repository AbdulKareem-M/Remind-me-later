from django.db import models

class Reminder(models.Model):
    CHOICES_TYPES = [
      ('sms', 'SMS'),
      ('email','Email')
    ]
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=CHOICES_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.reminder_type} - {self.date} {self.time}'
      
