import sys

class Const(object):
    # 自定义异常处理
    class ConstError(PermissionError):
        pass
    class ConstCaseError(ConstError):
        pass
    # 重写 __setattr__() 方法
    def __setattr__(self, name, value):
        if name in self.__dict__:  # 已包含该常量，不能二次赋值
            raise self.ConstError("Can't change const {0}".format(name))
        if not name.isupper():  # 所有的字母需要大写
            raise self.ConstCaseError("const name {0} is not all uppercase".format(name))
        self.__dict__[name] = value
const = Const()
# 将系统加载的模块列表中的 constant 替换为 _const() 实例
# sys.modules[__name__] = _const()
const.SENDOR = 'trackson512@126.com' # 发件人邮箱账号
const.RECEIVE = '245848461@qq.com'  # 收件人邮箱账号
const.PASSWD = 'asd123456789' # smtp账号，不是登录密码账号
const.MAILSERVER = 'smtp.126.com'
const.PORT = '25'
const.SUB = 'Python3 test'
