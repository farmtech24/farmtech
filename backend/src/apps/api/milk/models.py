
from django.db import models
from django.utils.translation import gettext as _

class DailyProduction(models.Model):
    """
    Model to store daily milk production data.
    """
    # Week number and day number to identify the day within a week
    week_number = models.PositiveIntegerField()
    day_number = models.PositiveIntegerField()

    # Date of the production
    date = models.DateField()

    # Milk production in gallons
    milk_production = models.DecimalField(max_digits=10, decimal_places=2)  # Allow decimals

    # Additional fields if needed
    # For example, to store any notes or comments about the production
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Week {self.week_number}, Day {self.day_number} ({self.date}) - {self.milk_production} gallons"

    def get_day_of_week(self):
        """
        Method to get the day of the week in Spanish.
        """
        # Use the strftime() method to format the date and get the day of the week
        day_of_week = self.date.strftime('%A')
        # Map the English day names to Spanish using a dictionary
        spanish_days = {
            'Monday': _('Lunes'),
            'Tuesday': _('Martes'),
            'Wednesday': _('Miércoles'),
            'Thursday': _('Jueves'),
            'Friday': _('Viernes'),
            'Saturday': _('Sábado'),
            'Sunday': _('Domingo'),
        }
        # Return the Spanish day name based on the English day name
        return spanish_days.get(day_of_week, day_of_week)
