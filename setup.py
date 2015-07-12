from setuptools import setup, find_packages

setup(
    name='foundation-sphinx-theme',
    version='0.0.3',
    packages=find_packages(),
    package_data={'': ['*.txt', '*.rst', '*.html', '*.css', '*.js', '*.conf']},
    author='Peter Hudec',
    author_email='peterhudec@peterhudec.com',
    description='',
    long_description=open('README.rst').read(),
    keywords=['sphinx', 'reStructuredText', 'theme', 'foundation'],
    url='https://github.com/peterhudec/foundation-sphinx-theme',
    license = 'MIT',
    install_requires=['setuptools'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Markup",
    ]
)