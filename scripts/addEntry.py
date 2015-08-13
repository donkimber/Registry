from zinnia.views.quick_entry import *

content = """
THis is the body
of a multiline
dummy test article.
"""

data = {
            'title': "This is dummy insertion",
            'slug': slugify("This is dummy insertion"),
            'status': PUBLISHED,
            'sites': [Site.objects.get_current().pk],
            'authors': [1],
            'content_template': 'zinnia/_entry_detail.html',
            'detail_template': 'entry_detail.html',
            'creation_date': timezone.now(),
            'last_update': timezone.now(),
            'content': content,
            'tags': "dummy"}
form = QuickEntryForm(data)
if form.is_valid():
    form.instance.content = linebreaks(form.cleaned_data['content'])
    entry = form.save()
    print "Added and saved"

