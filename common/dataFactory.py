#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/9/21 11:32
# @IDE:     PyCharm
# @About:   数据工厂

from faker import Faker


class FakeData:
    """
    封装faker库常用数据类型生成
    :param local: 默认中国地区数据类型，可传入local参数调整
    """
    def __init__(self, local='zh_CN'):
        # 实例化Faker类
        self._faker = Faker(locale=local)

    @property
    def name(self):
        """姓名"""
        return self._faker.name()

    @property
    def country(self):
        """国家"""
        return self._faker.country()

    @property
    def city(self):
        """城市"""
        return self._faker.city()

    @property
    def address(self):
        """地址"""
        return self._faker.address()

    @property
    def street_address(self):
        """街道"""
        return self._faker.street_address()

    @property
    def street_name(self):
        """街道名"""
        return self._faker.street_name()

    @property
    def postcode(self):
        """邮编"""
        return self._faker.postcode()

    @property
    def latitude(self):
        """纬度"""
        return self._faker.latitude()

    @property
    def longitude(self):
        """经度"""
        return self._faker.longitude()

    def barcode(self, length: int = 13):
        """自定义位数条码,只能选8或者13"""
        return self._faker.ean(length)

    @property
    def company(self):
        """公司"""
        return self._faker.company()

    @property
    def credit_card_number(self):
        """信用卡号"""
        return self._faker.credit_card_number()

    @property
    def credit_card_provider(self):
        """信用卡提供者"""
        return self._faker.credit_card_provider()

    @property
    def credit_card_expire(self):
        """信用卡有效期"""
        return self._faker.credit_card_expire()

    @property
    def credit_card_full(self):
        """信用卡完整信息"""
        return self._faker.credit_card_full()

    @property
    def currency_code(self):
        """货币代码"""
        return self._faker.currency_code()

    @property
    def date_time(self):
        """日期时间"""
        return self._faker.date_time()

    @property
    def date(self):
        """日期"""
        return self._faker.date(pattern="%Y-%m-%d")

    @property
    def time(self):
        """时间"""
        return self._faker.time(pattern="%H:%M:%S")

    @property
    def month(self):
        """月份"""
        return self._faker.month()

    @property
    def month_name(self):
        """月份名"""
        return self._faker.month_name()

    @property
    def year(self):
        """年"""
        return self._faker.year()

    @property
    def timezone(self):
        """时区"""
        return self._faker.timezone()

    @property
    def day_of_week(self):
        """随机星期几"""
        return self._faker.day_of_week()

    @property
    def day_of_month(self):
        """随机多少号"""
        return self._faker.day_of_month()

    @property
    def timestamp(self):
        """随机时间戳"""
        return self._faker.unix_time()

    @property
    def file_name(self):
        """随机文件名"""
        return self._faker.file_name()

    @property
    def ipv4(self):
        """ipv4"""
        return self._faker.ipv4()

    @property
    def ipv6(self):
        """ipv6"""
        return self._faker.ipv6()

    @property
    def url(self):
        """url"""
        return self._faker.url()

    @property
    def uri(self):
        """uri"""
        return self._faker.uri()

    @property
    def user_agent(self):
        """请求头"""
        return self._faker.user_agent()

    @property
    def mac_address(self):
        """MAC地址"""
        return self._faker.mac_address()

    @property
    def email(self):
        """email"""
        return self._faker.email()

    @property
    def job(self):
        """工作职位"""
        return self._faker.job()

    def text(self, max_nb_chars=50):
        """文本，可控长度"""
        return self._faker.text(max_nb_chars)

    @property
    def boolean(self):
        """随机布尔值"""
        return self._faker.boolean()

    @property
    def password(self):
        """密码"""
        return self._faker.password()

    @property
    def phone(self):
        """手机号"""
        return self._faker.phone_number()

    @property
    def random_str(self):
        """随机字符串"""
        return self._faker.pystr(min_chars=5, max_chars=10)

    @property
    def random_int(self):
        """随机数"""
        return self._faker.pyint()

    @property
    def identity_card(self):
        """身份证"""
        return self._faker.ssn()


if __name__ == '__main__':
    print(FakeData().email)
