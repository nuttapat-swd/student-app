# class Router:
#     app_label = {'schedule'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == self.app_label:
#             return 'mongodb'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == self.app_label:
#             return 'mongodb'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#             obj1._meta.app_label == self.app_label or
#             obj2._meta.app_label == self.app_label
#         ):
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == self.app_label:
#             return db == 'mongodb'
#         return None

class Router:
    mongo_db = "mongodb"
    default_db = "default"
    task_models = ['task',]

    def db_for_read(self, model, **hints):
        model_name = model._meta.model_name
        if model_name in self.task_models:
            return self.mongo_db
        else:
            return None
    
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == self.app_label:
#             return 'mongodb'
#         return None

    def db_for_write(self, model, **hints):
        model_name = model._meta.model_name
        if model_name in self.task_models:
            return self.mongo_db
        else:
            return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == self.app_label:
#             return 'mongodb'
#         return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.task_models:
            return db == self.mongo_db
        else:
            return db == self.default_db
        
    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if app_label == self.app_label:
    #         return db == 'mongodb'
    #     return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == 'schedule' or
            obj2._meta.app_label == 'schedule'
        ):
            return True
        return None

