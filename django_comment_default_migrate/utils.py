from django.db import router, DEFAULT_DB_ALIAS
from django.db.migrations import Migration
from django.db.models import Field

from django_comment_default_migrate.config import dcdm_config


def get_field_comment(field: Field):

    value = getattr(field, dcdm_config.DCDM_COMMENT_KEY)
    if value is not None:
        return str(value)


def get_table_comment(model):
    value = getattr(model._meta, dcdm_config.DCDM_TABLE_COMMENT_KEY)
    if value is not None:
        return str(value)


def get_migrations_app_models(
    migrations: [Migration], apps, using=DEFAULT_DB_ALIAS
) -> set:
    models = set()
    from django_comment_default_migrate.config import dcdm_config  # noqa
    dcdm_comment_app = dcdm_config.DCDM_COMMENT_APP
    for migration in migrations:
        if not isinstance(migration, Migration):
            continue
        app_label = migration.app_label
        if not router.allow_migrate(using, app_label) or app_label not in dcdm_comment_app:
            continue
        operations = getattr(migration, "operations", [])
        for operation in operations:
            model_name = getattr(operation, "model_name", None) or getattr(
                operation, "name", None
            )
            if model_name is None:
                continue
            try:
                model = apps.get_model(app_label, model_name=model_name)
            except LookupError:
                continue
            models.add(model)
    return models
