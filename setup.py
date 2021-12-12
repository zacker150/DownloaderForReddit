from setuptools import setup
from DownloaderForReddit.version import __version__

setup(
    # Metadata
    name='DownloaderForReddit',
    version=__version__,
    url='https://github.com/MalloyDelacroix/DownloaderForReddit',
    license='GNU GPLv3',
    author='Kyle Hickey',
    author_email='kyle.hickey222@gmail.com',
    description='A GUI application with some advanced features that downloads user posted content from reddit, '
                'either via a list of users or subreddits.',

    packages=[
        'DownloaderForReddit',
        'DownloaderForReddit.core',
        'DownloaderForReddit.customwidgets',
        'DownloaderForReddit.database',
        'DownloaderForReddit.extractors',
        'DownloaderForReddit.gui',
        'DownloaderForReddit.gui.database_views',
        'DownloaderForReddit.gui.settings',
        'DownloaderForReddit.gui.widgets',
        'DownloaderForReddit.guiresources',
        'DownloaderForReddit.guiresources.database_views',
        'DownloaderForReddit.guiresources.settings',
        'DownloaderForReddit.guiresources.widgets',
        'DownloaderForReddit.local_logging',
        'DownloaderForReddit.messaging',
        'DownloaderForReddit.persistence',
        'DownloaderForReddit.scheduling',
        'DownloaderForReddit.utils',
        'DownloaderForReddit.utils.exporters',
        'DownloaderForReddit.utils.importers',
        'DownloaderForReddit.viewmodels',
    ],

    entry_points={
        'console_scripts': [
            'dfr = main:main',
        ],
    }
)
