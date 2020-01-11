from setuptools import setup, find_packages


setup(
    name='mkdocs-toc-sidebar-plugin',
    version='0.1.0',
    description='An MkDocs plugin',
    long_description='An MkDocs plugin that allows users to add additional content to the ToC sidebar using the Material theme',
    keywords='mkdocs',
    url='https://github.com/midnightprioriem/mkdocs-toc-sidebar-plugin',
    download_url='https://github.com/midnightprioriem/mkdocs-toc-sidebar-plugin/archive/v_010.tar.gz',
    author='Zach Hannum',
    author_email='zacharyhannum@gmail.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4',
        'mkdocs-material>=4.5.0',
        'beautifulsoup4>=4.8.2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'toc-sidebar = mkdocs_toc_sidebar_plugin.plugin:TocSidebar'
        ]
    }
)
