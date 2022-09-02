Django Comment Default Migrate
======================

![Build](https://travis-ci.org/farseer810/django-comment-default-migrate.svg?branch=master)
![<https://pypi.org/project/django-comment-default-migrate/>](https://img.shields.io/pypi/v/django-comment-default-migrate)

An app that provides Django model comment/default migration

English \| [简体中文](./README-zh_CN.rst)

Feature
-------

-   Automatic migration model help\_text to comment \[Support
    customization\]
-   Automatic migration model default to default value(if it makes sense)
-   Automatically migrate the verbose\_name of the model to the table
    comment \[Support customization\]
-   Provide a command to migrate the comment/default of the specified app

Examples
--------

1.  download python package:

        pip install django-comment-default-migrate

2.  add django\_comment\_default\_migrate app

    project/project/settings.py

    ``` {.sourceCode .python}
    INSTALLED_APPS =[
        "django_comment_default_migrate",
        ...
    ]
    ```

3.  add model

    project/app/model.py

    ``` {.sourceCode .python}
    from django.db import models

    class CommentDefaultModel(models.Model):
        no_comment = models.TextField()
        aaa = models.IntegerField(default=0, help_text="test default")
        help_text = models.CharField(max_length=40,
                                     help_text="this is help text")

        class Meta:
            app_label = 'tests'
            db_table = 'comment_default_model'
            verbose_name = 'It is Comment Default Table'
    ```

4.  add app

    > project/app/settings.py

    ``` {.sourceCode .python}
    DCDM_COMMENT_APP=["app"]
    ```

5.  execute database migrate:

        python manage.py makemigrations
        python manage.py migrate

Now check the database table, comments/defaults have been generated.

Custom config
-------------

In settings.py:

    DCDM_COMMENT_KEY='verbose_name'
    DCDM_TABLE_COMMENT_KEY='verbose_name'
    DCDM_BACKEND={
            "new-engine": "engine.path"
    }
    DCDM_COMMENT_APP=["app"]

Command
-------

Provides a comment migration command, which allows the database to
regenerate comments:

    python manage.py migratecommentdefault  [app_label]

The command needs to be executed after all migrations are executed

Running the tests
-----------------

1.  Install Tox:

        pip install tox

2.  Run:

        tox

Supported Database
------------------

-   MySQL
-   PostgreSQL
