from django.conf import settings


class DCDMConfig:
    defaults = {
        "DCDM_COMMENT_KEY": "help_text",
        "DCDM_TABLE_COMMENT_KEY": "verbose_name",
        "DCDM_BACKEND": None,
        "DCDM_COMMENT_APP": []
    }

    def __getattr__(self, name):
        if name in self.defaults:
            return getattr(settings, name, self.defaults[name])


dcdm_config = DCDMConfig()
