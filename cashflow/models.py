from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "status"


class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        unique_together = ("type", "name")


class Record(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.category.type != self.type:
            raise ValueError("Category type must match record type.")

    def __str__(self):
        return f'{self.amount} - {self.created_at}'

    class Meta:
        db_table = "record"
        ordering = ['-created_at']
