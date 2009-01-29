from setuptools import setup, find_packages

setup(
    name='django-faq',
    version='0.1.0',
    description='This is a simple FAQ application.',
    author='Kevin Fricovsky',
    author_email='kfricovsky@gmail.com',
    url='http://github.com/RockHoward/django-faq/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
