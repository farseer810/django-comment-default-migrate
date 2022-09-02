from abc import ABCMeta
from typing import Type, List, AnyStr, Tuple

from django.db import transaction
from django.db.models import Model


class BaseCommentDefaultMigration(metaclass=ABCMeta):
    atomic = True

    def __init__(self, connection, model: Type[Model], collect_sql=False):
        self.connection = connection
        self.model = model
        self.collect_sql = collect_sql
        if self.collect_sql:
            self.collected_sql = []

    @property
    def db_table(self):
        return self.model._meta.db_table

    def comment_default_sqls(self) -> List[Tuple[AnyStr, List[AnyStr]]]:
        pass

    def migrate_comments_to_database(self):
        pass

    def quote_name(self, name):
        return self.connection.ops.quote_name(name)

    def execute(self):
        if self.atomic:
            with transaction.atomic():
                self.execute_sql()
        else:
            self.connection.needs_rollback = False
            self.execute_sql()

    def execute_sql(self):
        comment_default_sqls = self.comment_default_sqls()
        if comment_default_sqls:
            with self.connection.cursor() as cursor:
                for comment_default_sql, sql_params in comment_default_sqls:
                    cursor.execute(comment_default_sql, sql_params)
