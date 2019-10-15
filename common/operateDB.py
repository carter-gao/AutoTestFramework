#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/19 20:56
# @IDE:     PyCharm
# @About:   封装数据库操作

import redis
import pymysql
import cx_Oracle

from common.logger import Logger
from common.constant import config_common_path
from common.operateConfig import OperateConfig


class DBOracle:
    """
    操作ORACLE
    """

    def __init__(self):
        # 引用日志类
        self._log = Logger("ORACLE").get_logger()

        # 获取数据库配置
        self._db_config = OperateConfig(config_common_path)

        self._conn_str = '{}/{}@{}:{}/{}'.format(
            self._db_config.get_str('oracle', 'username'),
            self._db_config.get_str('oracle', 'password'),
            self._db_config.get_str('oracle', 'host'),
            self._db_config.get_str('oracle', 'port'),
            self._db_config.get_str('oracle', 'database')
        )
        try:
            self._conn = cx_Oracle.connect(self._conn_str)
            self._log.info('成功连接数据库')
        except cx_Oracle.Error as e:
            self._log.error('数据库连接失败：{}'.format(e))

    @property
    def conn(self):
        """
        返回数据库连接实例，可单独cx_Oracle库其他方法
        :return: 数据库连接实例
        """
        return self._conn

    def disconnect(self):
        """
        断开连接
        :return: None
        """
        self._conn.close()
        self._log.info('成功断开数据库')

    def select_all(self, sql_string: str):
        """
        执行查询sql
        :param sql_string: sql语句
        :return: 元组列表
        """
        c = self._conn.cursor()
        self._log.info('执行查询语句：%s' % sql_string)
        x = c.execute(sql_string)
        # 获取全部结果集（元组列表）,可使用下标访问结果集，如datalist[0][1]
        datalist = x.fetchall()
        self._log.info('查询结果如下：')
        for data in datalist:
            self._log.debug('第 {} 条数据：{}'.format(datalist.index(data) + 1, data))
        c.close()
        return datalist

    def select_one(self, sql_string: str):
        """
        执行查询sql
        :param sql_string: sql语句
        :return: 单个查询字段值或单条记录
        """
        c = self._conn.cursor()
        self._log.info('执行查询语句：%s' % sql_string)
        x = c.execute(sql_string)
        # 获取查询的单个字段的值或单条记录
        data = x.fetchone()
        self._log.debug('查询结果如下：{}'.format(data))
        c.close()
        if len(data[0]) == 1:
            return data[0][0]
        else:
            return data

    def execute_sql(self, sql_string: str):
        """
        执行插入、更新、删除操作
        :param sql_string: sql语句
        :return: None
        """
        try:
            c = self._conn.cursor()
            self._log.info('执行%s语句：%s' % (sql_string.split()[0], sql_string))
            c.execute(sql_string)
            self._conn.commit()
            c.close()
        except cx_Oracle.Error as e:
            self._log.error('执行失败：%s' % str(e))
            self._conn.rollback()
            self._log.error('成功回滚操作')

    def exec_function(self, function_name: str, *parameters, **keyword_parameters):
        """
        执行指定函数，可指定参数
        :param function_name: 函数名
        :param parameters: 元组可变参数
        :param keyword_parameters: 字典可变参数
        :return: None
        """
        try:
            c = self._conn.cursor()
            self._log.info('执行函数：{}'.format(function_name))
            c.callfunc(function_name, *parameters, **keyword_parameters)
            c.close()
        except cx_Oracle.Error as e:
            self._log.error('执行失败：%s' % str(e))
            self._conn.rollback()
            self._log.error('成功回滚操作')

    def exec_process(self, process_name, *parameters, **keyword_parameters):
        """
        执行指定存储过程，可指定参数
        :param process_name: 过程名
        :param parameters: 元组可变参数
        :param keyword_parameters: 字典可变参数
        :return: None
        """
        try:
            c = self._conn.cursor()
            self._log.info('执行过程：{}'.format(process_name))
            c.callproc(process_name, *parameters, **keyword_parameters)
            c.close()
        except cx_Oracle.Error as e:
            self._log.error('执行失败：%s' % str(e))
            self._conn.rollback()
            self._log.error('成功回滚操作')


class DBRedis:
    """
    连接redis执行操作
    :param db_: 库，默认第一个（0）
    """

    def __init__(self, db_=0):
        # 引用日志类
        self._log = Logger('REDIS').get_logger()

        # 获取redis配置信息
        self._redis_conf = OperateConfig(config_common_path)

        try:
            pool = redis.ConnectionPool(
                host=self._redis_conf.get_str('redis', 'host'),
                port=self._redis_conf.get_str('redis', 'port'),
                password=self._redis_conf.get_str('redis', 'auth'),
                db=db_,
                decode_responses=True
            )
            self._conn = redis.StrictRedis(connection_pool=pool)
            self._log.info('成功连接REDIS，db({})'.format(db_))
        except redis.exceptions.RedisError as e:
            self._log.error('REDIS连接失败：{}'.format(e))

    def conn(self):
        """
        返回连接实例，可单独调用redis库的其他方法
        :return: 连接实例
        """
        return self._conn

    def set_kv(self, key_, value_, ex_=None, px_=None, nx_=False, xx_=False):
        """
        在Redis中设置值，不存在则创建，存在则修改，并返回值;
        对于有些value有业务需求字符串的，加上双引号，如：'"123456"'
        :param key_: key
        :param value_: value
        :param ex_: 过期时间（秒）
        :param px_: 过期时间（毫秒）
        :param nx_: 如果设置为True，则只有name不存在时，当前set操作才执行
        :param xx_: 如果设置为True，则只有name存在时，当前set操作才执行
        :return: 设定的value值
        """
        self._conn.set(key_, value_, ex=ex_, px=px_, nx=nx_, xx=xx_)
        self._log.info('设置成功：{}={}'.format(key_, value_))
        return value_

    def get_v(self, key_):
        """
        获取指定key的value值
        :param key_: key
        :return: value
        """
        value = self._conn.get(key_)
        if value:
            self._log.info('获取到{}={}'.format(key_, value))
            return value
        else:
            self._log.error('键{}不存在'.format(key_))

    def del_kv(self, key_):
        """
        删除指定的key-value
        :param key_: key
        :return:
        """
        value = self._conn.get(key_)
        if value:
            self._conn.delete(key_)
            self._log.info('已删除{}={}'.format(key_, value))
        else:
            self._log.info('指定删除的键不存在')


class DBMySql:
    """
    操作MYSQL
    """

    def __init__(self):
        # 引用日志类
        self._log = Logger("MYSQL").get_logger()

        # 获取数据库配置
        self._db_config = OperateConfig(config_common_path)

        try:
            self._conn = pymysql.connect(
                user=self._db_config.get_str('mysql', 'username'),
                password=self._db_config.get_str('mysql', 'password'),
                host=self._db_config.get_str('mysql', 'host'),
                port=self._db_config.get_str('mysql', 'port'),
                database=self._db_config.get_str('mysql', 'database')
            )
            self._log.info('成功连接数据库')
        except pymysql.Error as e:
            self._log.error('数据库连接失败：{}'.format(e))

    @property
    def conn(self):
        """
        返回数据库连接实例，可单独PyMySql库其他方法
        :return: 数据库连接实例
        """
        return self._conn

    def disconnect(self):
        """
        断开连接
        :return: None
        """
        self._conn.close()
        self._log.info('成功断开数据库')

    def select_all(self, sql_string: str):
        """
        执行查询sql
        :param sql_string: sql语句
        :return: 元组列表
        """
        c = self._conn.cursor()
        self._log.info('执行查询语句：%s' % sql_string)
        x = c.execute(sql_string)
        datalist = x.fetchall()
        self._log.info('查询结果如下：')
        for data in datalist:
            self._log.debug('第 {} 条数据：{}'.format(datalist.index(data) + 1, data))
        c.close()
        return datalist

    def select_one(self, sql_string: str):
        """
        执行查询sql
        :param sql_string: sql语句
        :return: 单个查询字段值或单条记录
        """
        c = self._conn.cursor()
        self._log.info('执行查询语句：%s' % sql_string)
        x = c.execute(sql_string)
        # 获取查询的单个字段的值或单条记录
        data = x.fetchone()
        self._log.debug('查询结果如下：{}'.format(data))
        c.close()
        if len(data[0]) == 1:
            return data[0][0]
        else:
            return data

    def execute_sql(self, sql_string: str):
        """
        执行插入、更新、删除操作
        :param sql_string: sql语句
        :return: None
        """
        try:
            c = self._conn.cursor()
            self._log.info('执行%s语句：%s' % (sql_string.split()[0], sql_string))
            c.execute(sql_string)
            self._conn.commit()
            c.close()
        except pymysql.Error as e:
            self._log.error('执行失败：%s' % str(e))
            self._conn.rollback()
            self._log.error('成功回滚操作')


if __name__ == '__main__':

    db = DBRedis()
    s = db.get_v('SMSCaptcha:activity:sales:18936048888')
