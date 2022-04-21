from django.db import models
from django.utils.timezone import now


class Specs(models.Model):
    color = models.CharField(max_length=10)
    fuel_type = models.CharField(max_length=10)
    max_speed = models.IntegerField()

    def __str__(self):
        return (
            f"(color: {self.color},fuel_type: {self.fuel_type}, "
            + f"max_speed: {self.max_speed})"
        )


class Car(models.Model):
    model = models.CharField(max_length=30)
    price = models.IntegerField()
    previous_owner = models.CharField(null=True, max_length=30)
    date_imported = models.DateTimeField(default=now)
    specs = models.ForeignKey(Specs, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"model: {self.model}, price: {self.price}, "
            + f"previous_owner: {self.previous_owner}, date_imported: "
            + f"{self.date_imported},\nspecs= {self.specs}"
        )
