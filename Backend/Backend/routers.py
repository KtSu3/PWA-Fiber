class DatabaseRouter:
    def db_for_read(self, model, **hints):
        return 'postgres'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('default', 'postgres')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'