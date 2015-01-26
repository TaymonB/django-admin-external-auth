from setuptools import setup

setup(
    name='django-admin-external-auth',
    version='0.1.0',
    description="Use your Django project's existing authentication views in the admin interface.",
    url='https://github.com/TaymonB/django-admin-external-auth',
    author='Taymon A. Beal',
    author_email='taymonbeal@gmail.com',
    license='MIT',
    platforms=['OS Independent'],
    keywords='admin authentication django',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['daeauth'],
    install_requires=['Django>=1.7'],
)