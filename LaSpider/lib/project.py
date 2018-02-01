# project 检测result， 状态有页数和清洗结果
# 主要用来处理统计页面。
# 一个project应该包括爬虫和清洗，目前先考虑所有清洗在爬虫处理的情况

class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 定义清洗程序
class StringField(Field):
    """判断代码"""
    def __init__(self, name):
        if len(name) > 10:
            raise Exception('String length can not over 1')
        super(StringField, self).__init__(name, 'varchar(100)')



# 定义元类, field对象存入mapping, mapping={'name': obj}
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 这个类用来实现数据的操作
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append('"{}"'.format(getattr(self, k, None).replace('"', '').replace("'", '')))
        print(args, fields)
        sql = 'insert into {} ({}) values ({})'.format(self.__table__, ','.join(fields), ','.join(args))
        print(sql)





class ProjectManager:
    @staticmethod
    def build_module(project, env=None):
        pass


    def __init__(self, script, task):
        pass
        self.page = page

    def build_module(self, script, task):
        pass


class User(Model):
    name = StringField('name')


if __name__ == '__main__':
    import importlib

    spec = importlib.machinery.ModuleSpec('spec', None)
    mod = importlib.util.module_from_spec(spec)
    script = "def a():" \
             "  return 'this is a'"
    aa = compile(script, 'script', 'exec')
    print(aa)
    print(exec(aa), )