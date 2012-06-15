from collections import OrderedDict

from eplasty.object.base import Object
from eplasty.object.meta import ObjectMeta
from eplasty.field.simple import Integer, CharacterVarying, Text, Date
from eplasty.field.helper import SimplePK

from anthrax.util import bind_fields
from anthrax.introspector import Introspector
from anthrax.field import IntegerField, TextField, DateField
from anthrax.widget import Hidden, TextInput, LongTextInput

EDIT = 'EDIT'

class EplastyIntrospector(Introspector):

    def get_fields(self, form):
        if not isinstance(self.source, (Object, ObjectMeta)):
            raise TypeError('The introspection source must be Elephantoplasty'
                'Object or Object class')
        result = OrderedDict()
        for field in self.source.fields:
            anthrax_field = self._handle_field(field)
            if anthrax_field is not None:
                result[field.name] = anthrax_field
        bind_fields(result, form)
        return result

    def _handle_field(self, field):
        return getattr(self, self._map[type(field)])()

    def _simple_pk_handler(self):
        return IntegerField(widgets=[Hidden], mode=EDIT)

    def _integer_handler(self):
        return IntegerField()

    def _varchar_handler(self):
        return TextField()

    def _text_handler(self):
        return TextField(widgets=[LongTextInput, TextInput])

    def _date_handler(self):
        return DateField()

    _map = {
        SimplePK: '_simple_pk_handler',
        Integer: '_integer_handler',
        CharacterVarying: '_varchar_handler',
        Text: '_text_handler',
        Date: '_date_handler',
    }
