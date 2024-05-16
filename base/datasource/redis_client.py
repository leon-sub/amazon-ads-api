#!/usr/bin/python3
# coding:utf-8
"""
redis
"""
import redis
import json

class Redis:
    def __init__(self, host=None, password=None, port=None, db=None):
        """
        创建redis实例
        :param host:链接ip
        :param port:端口
        :param password:密码
        """
        self._CData_ = {
            "Host": "127.0.0.1",
            "PassWord": "",
            "Port": 6379,
            "db": 0
            }
        self.redis_data = redis.Redis(host=self._CData_['Host'], port=self._CData_['Port'], password=self._CData_['PassWord'], db=self._CData_['db'], decode_responses=True)

    def put_all_key(self, dict_data):
        """
        增加string类型key
        :param dict_data:需添加对key-value对（dict）
        :return: none
        """
        self.redis_data.mset(dict_data)

    def put_key(self, key, value, ex=None):
        """
        增加string类型key
        :param key: key string
        :param value: value
        :param ex: 过期时间
        :return: none
        """
        if isinstance(value,dict):
            value = json.dumps(value)
        self.redis_data.set(key, value, ex)

    def put_tuple(self, key, value):
        """
        往集合添加数据
        :param key: 集合名
        :param value: 添加数据
        :return: none
        """
        self.redis_data.srem(key, value)
        self.redis_data.sadd(key, value)

    def is_tuple_key(self, key, value):
        """
        判断数据是否在集合中
        :param key: 集合名 string
        :param value: value
        :return:bool
        """
        return self.redis_data.sismember(key, value)

    def get_key(self, key):
        """
        获取value（根据key）
        :param key: key（list）
        :return: str/list
        """
        data = self.redis_data.get(key)
        try:
            data = json.loads(data)
        except:
            pass
        return data

    def del_key(self, key):
        """
        删除key
        :param key:key name
        :return: none
        """
        self.redis_data.delete(key)

    def put_queue_cache(self, key, value):
        """
        添加缓存队列
        :param key:
        :param value:
        :return:
        """
        self.redis_data.sadd(key, value)

    def del_queue_cache(self, key, value):
        """
        删除缓存队列
        :param key:
        :param value:
        :return:
        """
        self.redis_data.srem(key, value)

    def get_queue_cache(self, key):
        """
        获取缓存队列
        :param key:
        :return:
        """
        return self.redis_data.smembers(key)

    def get_queue_size(self, key):
        """
        获取队列长度

        :param key: 队列名称
        :return:
        """
        return self.redis_data.llen(key)

    def get_queue_value_timeout(self, key, timeout):
        """
        获取队列第一个非空的值

        :param key: 队列名称
        :param timeout: 超时时间
        :return:
        """
        return self.redis_data.blpop(key, timeout=timeout)

    def put_queue_value(self, key, value):
        """
        往队列的末尾添加值

        :param key: 队列名称
        :param value: 值
        :return:
        """
        return self.redis_data.rpush(key, value)

    def get_queue_value(self, key):
        """
        获取队列第一个元素，没有就为空

        :param key:
        :return:
        """
        return self.redis_data.lpop(key)
