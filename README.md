# ProxiesPool
**爬取 [快代理](https://www.kuaidaili.com/free/) 的免费代理池**

文档更新时间（2023/8/17）
>
>很久以前写的一个拙劣的爬虫，最近翻到了就上传了
>
>由于是免费代理，所以不一定都有效，使用前先测试
>

# 使用说明
>
># ProxiesPool.py
>爬取代理，生成.txt文件
>>
>>1.运行程序，输入要获取的最大页数
>>
>>2.等待程序运行，在C:\Users\Administrator\Downloads\目录下会生成HTTP_ProxiesPool.txt和HTTPS_ProxiesPool.txt文件
>>
>
># ProxiesPool_test.py
>测试代理池，生成新的.txt文件
>>
>>1.dead_time:响应时间，根据测试需求修改，默认是1s
>>
>>2.proxies_pool_test()函数里的url为用于测试的网址，默认是小红书，请自行修改
>>
>>3.运行程序，在C:\Users\Administrator\Downloads\目录下会生成通过测试的.txt文件
>


