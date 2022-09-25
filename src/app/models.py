from typing import Any

from behaviors.behaviors import Timestamped  # type: ignore

from django.db import models

__all__ = [
    'models',
    'DefaultModel',
]


class DefaultModel(models.Model):
    """
    - Default __str__ is for field 'name'.
    - If you need to run services on model save(), override 'def run_services(self)'
    - If you need calculated fields, prefer to use a database field and calculate this field using 'def calculate_...(self)' to avoid issues with filters.
    - You can update model with kwargs using 'def update_from_kwargs(...)'
    - For testing: 'def setattr_and_save(...)'
    - VALIDATE MODEL FIELD ONLY OUT OF 'SAVE()' (possible in 'validators=[...]' in field params)
    """
    class Meta:
        abstract = True

    def __str__(self) -> str:
        """Default name for all models"""
        name = getattr(self, 'name', None)
        if name is not None:
            return str(name)

        return super().__str__()

    def update_from_kwargs(self, **kwargs: dict[str, Any]) -> None:
        """A shortcut method to update model instance from the kwargs.
        """
        for (key, value) in kwargs.items():
            setattr(self, key, value)

    def setattr_and_save(self, key: str, value: Any) -> None:
        """Shortcut for testing -- set attribute of the model and save"""
        setattr(self, key, value)
        self.save()

    def get_field_calculators(self) -> list:
        return [
            getattr(self, attr_name) for attr_name in dir(self) if attr_name.startswith('calculate_')
        ]

    def update_calculated_fields(self) -> None:
        for calculator in self.get_field_calculators():
            calculator()

    def run_services(self) -> None:
        """Run required on 'save()' services here
        """
        pass

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.update_calculated_fields()
        self.run_services()
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
