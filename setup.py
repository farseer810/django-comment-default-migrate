from setuptools import setup

readme = open('README.md', encoding='utf-8').read()

setup(
    name='django-comment-default-migrate',
    version='0.1.0',
    description="""An app that provides Django model comment/default migration """,
    long_description=readme,
    author='farseer810',
    author_email='farseer810@qq.com',
    url='https://github.com/farseer810/django-comment-default-migrate.git',
    keywords='django-comment-default-migrate',
    packages=['django_comment_default_migrate'],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    install_requires=['django>=2.2'],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
