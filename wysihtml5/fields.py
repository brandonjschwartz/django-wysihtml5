#-*- coding: utf-8 -*-

from django.db.models import fields

from wysihtml5.utils import keeptags
from wysihtml5.widgets import Wysihtml5AdminTextareaWidget


class Wysihtml5TextField(fields.TextField):
    def __init__(self, *args, **kwargs):
        self.keep_tags = kwargs.pop('keep_tags', 'h1 h2 h3 h4 h5 h6 div p i u'
                                    ' ul ol li span img a blockquote')
        super(Wysihtml5TextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"widget": Wysihtml5AdminTextareaWidget}
        defaults.update(kwargs)
        return super(Wysihtml5TextField, self).formfield(**defaults)

    def pre_save(self, model_instance, add):
        value = super(Wysihtml5TextField, self).pre_save(model_instance, add)
        return keeptags(value, self.keep_tags)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^wysihtml5\.fields\.Wysihtml5TextField"])
except ImportError:
    pass
