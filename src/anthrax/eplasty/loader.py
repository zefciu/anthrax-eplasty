from anthrax.field.action import Action

def create_object(Type, form):
    values = dict()
    for k, v in form.items():
        if isinstance(form.__fields__[k]._field, Action):
            continue
        else:
            values[k] = v
    return Type(**values)
