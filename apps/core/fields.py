# Third
from rest_framework.fields import BooleanField, CharField


class StrictCharField(CharField):
    def to_internal_value(self, data):
        if not isinstance(data, str):
            self.fail('invalid')

        return super().to_internal_value(data)


class StrictBooleanField(BooleanField):
    def to_internal_value(self, data):
        try:
            if data is True:
                return True
            elif data is False:
                return False
            elif data is None and self.allow_null:
                return None
        except TypeError:  # Input is an unhashable type
            pass
        self.fail('invalid', input=data)


