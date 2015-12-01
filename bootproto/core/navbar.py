from django.conf import settings

brand = {
    'render_brand': True,
    'image_link': settings.STATIC_URL + 'ut-brand.png'
}

left_navbar = [
    {
        'dropdown': False,
        'class': 'active',
        'href': '#',
        'content': 'Hello!',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Hello2',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Hello3',
    },
    {
        'dropdown': True,
        'dropdown_main_href': '#',
        'dropdown_main_content': 'Hello4',
        'class': '',
        'href': '#',
        'content': 'HelloDropdown',
        'dropdown_list_items': [
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello5',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello6',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'content': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello7',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello8',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello9',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello10',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'content': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello11',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello12',
            },
        ]
    }
]

right_navbar = [
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Hello!',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Hello2',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Hello3',
    },
    {
        'dropdown': True,
        'dropdown_main_href': '#',
        'dropdown_main_content': 'Hello4',
        'class': '',
        'href': '#',
        'content': 'HelloDropdown',
        'dropdown_list_items': [
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello5',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello6',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'content': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello7',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello8',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello9',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello10',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'content': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello11',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Hello12',
            },
        ]
    }
]

search_bar = {
    'form_method': 'post',
    'form_action': '',
    'placeholder_text': 'Search subsystem...',
    'submit_button_text': 'Search',
}

navbar_items = len(left_navbar) + len(right_navbar) + len(search_bar)

navbar = {
    'render_navbar': True,
    'brand': brand,
    'number_of_navbar_items': navbar_items,
    'left_navbar_items': left_navbar,
    'right_navbar_items': right_navbar,
    'search_bar': search_bar,
}