import warnings

from django.conf import settings
from django.db import connections
from django.utils.module_loading import import_string

from django_comment_default_migrate.config import dcdm_config


def get_migration_class_from_engine(engine):
    engine_name = engine.split(".")[-1]
    if (
        dcdm_config.DCDM_BACKEND
        and isinstance(dcdm_config.DCDM_BACKEND, dict)
        and dcdm_config.DCDM_BACKEND.get(engine_name)
    ):
        path = dcdm_config.DCDM_BACKEND.get(engine_name)
    else:
        # This backend was renamed in Django 1.9.
        if engine_name == "postgresql_psycopg2":
            engine_name = "postgresql"
        path = f"django_comment_default_migrate.backends.{engine_name}.CommentDefaultMigration"

    return import_string(path)


def migrate_app_models_comment_to_database(app_models, using):
    engine = settings.DATABASES[using]["ENGINE"]
    try:
        migration_class = get_migration_class_from_engine(engine)
    except ImportError:
        warnings.warn(
            f"{engine} is not supported by this comment migration" f" backend."
        )
    else:
        for model in app_models:
            executor = migration_class(connection=connections[using], model=model)
            executor.execute()
