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
        'content': 'Navbar active link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Navbar link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Navbar link',
    },
    {
        'dropdown': True,
        'dropdown_main_href': '#',
        'dropdown_main_content': 'Dropdown menu',
        'class': '',
        'href': '#',
        'content': 'HelloDropdown',
        'dropdown_list_items': [
            {
                'role': '',
                'class': 'dropdown-header',
                'href': '#',
                'content': 'Dropdown header',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
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
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
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
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
            },
        ]
    }
]

right_navbar = [
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Navbar link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Navbar link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'content': 'Navbar link',
    },
    {
        'dropdown': True,
        'dropdown_main_href': '#',
        'dropdown_main_content': 'Dropdown menu',
        'class': '',
        'href': '#',
        'content': 'HelloDropdown',
        'dropdown_list_items': [
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
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
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
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
                'content': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'content': 'Dropdown item',
            },
        ]
    }
]

number_of_navbar_items = len(left_navbar) + len(right_navbar)

navbar = {
    'render_navbar': True,
    'brand': brand,
    'number_of_navbar_items': number_of_navbar_items,
    'left_navbar_items': left_navbar,
    'right_navbar_items': right_navbar,
}