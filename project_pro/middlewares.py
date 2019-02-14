# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random, json
from project_pro.spiders.utils import error_back
from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy import signals
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.http.response.html import HtmlResponse


class ProjectProDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 自定义捕获错误URL
class ProcessAllExceptionMiddleware(RetryMiddleware):
    ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError)

    def process_response(self, request, response, spider):
        # def process_response(self, request, response, spider):
        #     if request.meta.get('dont_retry', False):
        #         return response
        #     if response.status in self.retry_http_codes:
        #         reason = response_status_message(response.status)
        #         # 删除该代理
        #         self.delete_proxy(request.meta.get('proxy', False))
        #         time.sleep(random.randint(3, 5))
        #         self.logger.warning('返回值异常, 进行重试...')
        #         return self._retry(request, reason, spider) or response
        #     return response
        # 捕获状态码为40x/50x的response
        if response.status != 200:
            # 随意封装，直接返回response，spider代码中根据url==''来处理response
            error_back(response)
            return response

        # 其他状态码不处理
        return response

    # def process_exception(self, request, exception, spider):
    #     # 捕获几乎所有的异常
    #     if isinstance(exception, self.ALL_EXCEPTIONS):
    #         # 在日志中打印异常类型
    #         print('Got exception: %s' % (exception))
    #         # 随意封装一个response，返回给spider
    #         error_back(exception)
    #         response = HtmlResponse(url='exception')
    #         return response
    #     error_back(exception)



# 自定义一个ip更换下载中间件的类，实现process_request（处理中间件拦截的请求(ip代理吃)）
# 对请求进行ip更换
class Proxy(object):
    def process_request(self, request, spider):
#         # 判断请求的url是http还是https
#         h = request.url.split(':')[0]
#         # if h == 'https':
#         #     ip = random.choice(proxy_https_list)
#         #     # 请求ip的更换(proxy的值就是对应的ip)
#         #     request.meta['proxy'] = 'https://'+ip
#         # else:
        ip = random.choice(proxy_http_list)
        # 请求ip的更换(proxy的值就是对应的ip)
        request.meta['proxy'] = 'http://' + ip

# 自定义请求UA动态池的下载中间件类
# 1.导入包操作
class RandomUserAgetn(UserAgentMiddleware):

    def process_request(self, request, spider):
        # 从列表中随机抽选出一个UA值，并赋值给当前请求的request的header
        UA = random.choice(user_agent_list)
        request.headers.setdefault('User-Agent', UA)



# 这里可针对基于http和https分别存放在两个列表中
# proxy_https_list = [
#     '173.82.219.113:3128',
#     '92.243.6.37:80',
#     '117.102.96.59:8080',
#     '213.234.28.94:8080'
# ]

proxy_http_list = [
    "119.57.108.53:53281",
    "58.249.55.222:9797",
    "61.145.182.27:53281",
    "125.46.0.62:53281",
    "101.89.132.131:80"
]

user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]