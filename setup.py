from setuptools import setup

setup(
    name='core',
    package=['core'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy'
    ]
)
