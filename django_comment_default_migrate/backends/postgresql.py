from psycopg2 import sql

from django_comment_default_migrate.backends.base import BaseCommentDefaultMigration
from django_comment_default_migrate.utils import get_field_comment, get_table_comment


class CommentDefaultMigration(BaseCommentDefaultMigration):
    comment_sql = sql.SQL("COMMENT ON COLUMN {}.{} IS %s")
    table_comment_sql = sql.SQL("COMMENT ON TABLE {} is %s;")

    def comment_default_sqls(self):
        results = []
        comment_default_sqls = self._get_fields_comments_sql()
        if comment_default_sqls:
            results.extend(comment_default_sqls)
        table_comment = get_table_comment(self.model)
        if table_comment:
            results.append(
                (
                    self.table_comment_sql.format(sql.Identifier(self.db_table)),
                    [table_comment],
                )
            )

        return results

    def _get_fields_comments_sql(self):
        comment_default_sqls = []
        for field in self.model._meta.fields:
            comment = get_field_comment(field)
            if comment:
                comment_sql = self.comment_sql.format(
                    sql.Identifier(self.db_table), sql.Identifier(field.column)
                )
                comment_default_sqls.append((comment_sql, [comment]))
        return comment_default_sqls
