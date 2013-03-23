import unittest

import eplasty as ep

from anthrax.container import Form

class Test(unittest.TestCase):
    
    def setUp(self):
        class Knight(ep.Object):
            name = ep.field.CharacterVarying(40)

        class KnightForm(Form):
            __reflect__ = ('eplasty', Knight)
            name = {'label': 'Imię'}

        self.KnightForm = KnightForm

    def test_edit_form(self):
        form = self.KnightForm(mode='EDIT')
        self.assertTrue('name' in form.__fields__)
        self.assertEqual(form.__fields__['name'].name, 'name')
        self.assertIs(form.__fields__['name'].parent, form)
        self.assertEqual(form.__fields__['name'].label, 'Imię')
        self.assertTrue('id' in form.__fields__)

    def test_new_form(self):
        form = self.KnightForm(mode='NEW')
        self.assertTrue('name' in form.__fields__)
        self.assertFalse('id' in form.__fields__)
