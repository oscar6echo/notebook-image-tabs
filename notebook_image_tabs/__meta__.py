
__name__ = 'notebook_image_tabs'
name_url = __name__.replace('_', '-')

__packages__ = [__name__]
__version__ = '0.1.0'
__description__ = 'display several images under tabs'
__long_description__ = 'See repo README'
__author__ = 'oscar6echo'
__author_email__ = 'olivier.borderies@gmail.com'
__url__ = 'https://github.com/{}/{}'.format(__author__,
                                            name_url)
__download_url__ = 'https://github.com/{}/{}/tarball/{}'.format(__author__,
                                                                name_url,
                                                                __version__)
__keywords__ = ['javascript', 'tab', 'image', 'display']
__license__ = 'MIT'
__classifiers__ = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'
                   ]
__include_package_data__ = True
__package_data__ = {
    'templates':
        ['templates/main.tpl.html',
         'templates/script.tpl.js'
        ],
}

__zip_safe__ = False
