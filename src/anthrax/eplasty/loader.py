from anthrax.field.action import Action
try:
    from lxml.html import HtmlElement, tostring
except ImportError:
    HtmlElement = None

def create_object(Type, form):
    values = dict()
    for k, v in form.items():
        if isinstance(form.__fields__[k]._field, Action):
            continue
        if HtmlElement and isinstance(v, HtmlElement):
            values[k] = str(tostring(v))
        else:
            values[k] = v
    return Type(**values)
