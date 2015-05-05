from mezzanine.conf import register_setting


DEFAULT_SETTINGS = {
    'pages': (
        'pages.RichTextPage',
        'pages.Link',
    ),
    'blog': (
        'blog.BlogPost',
        'blog.BlogCategory',
    ),
    'forms': (
        'forms.Form',
    ),
    'galleries': (
        'galleries.Gallery',
    ),
}


register_setting(
    name="MEZZANINE_REST_SETTINGS",
    editable=False,
    default=DEFAULT_SETTINGS,
)
