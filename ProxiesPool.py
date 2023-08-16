# 作者：aoyijiaozhu
# 创建时间：2023/1/14 16:09
# 修改时间：2023/8/16
# 爬取代理池
import requests
from lxml import etree
import time
import random
headers={
    'user-agent':random.choice([
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14"
])
}
proxies=random.choice([
    {'HTTP':'117.94.120.236:9000'},
    {'HTTP':'121.13.252.62:41564'},
    {'HTTP':'112.14.47.6:52024'},
    {'HTTP':'121.13.252.58:41564'},
    {'HTTP':'222.74.73.202:42055'},
    {'HTTP':'117.114.149.66:55443'}
])



#urls=[f'https://www.kuaidaili.com/free/inha/{page}/' for page in range(1,100)]

def get_html(url):  #获取网页html内容
    response = requests.get(url, headers=headers,proxies=proxies)
    content=response.text
    return content

def get_html_tree(html):  #获取html_tree
    html_tree = etree.HTML(html)
    return html_tree

def get_ip_lst(html_tree): #获取ip列表
    ip_lst = html_tree.xpath('//body//table/tbody/tr/td[@data-title="IP"]/text()')
    return ip_lst

def get_port_lst(html_tree):   #获取端口列表
    port_lst = html_tree.xpath('//body//table/tbody/tr/td[@data-title="PORT"]/text()')
    return port_lst

def get_type_lst(html_tree):   #获取代理类型列表
    type_lst = html_tree.xpath('//body//table/tbody/tr/td[@data-title="类型"]/text()')
    return type_lst

def file_write(ip_lst,port_lst,type_lst):   #拼接和写入文件
    with open('C:\\Users\Administrator\\Downloads\\HTTP_ProxiesPool.txt','a') as http_file,open('C:\\Users\\Administrator\\Downloads\\HTTPS_ProxiesPool.txt','a') as https_file:
        for (ip,port,type_) in zip(ip_lst,port_lst,type_lst):
            proxy = '{\'' + type_ + '\'' + ':' + '\'' + str(ip) + ':' + str(port) + '\'}'
            #print(proxy)
            if type_=='HTTP':
                http_file.write(proxy+'\n')
            elif type_=='HTTPS':
                https_file.write(proxy+'\n')
    print('-------------------爬取成功---------------------')

if __name__ == '__main__':
    max_page=int(input("请输入要获取的最大页数："))
    urls = [f'https://www.kuaidaili.com/free/inha/{page}/' for page in range(1, max_page+1)]
    for page,url in enumerate(urls):
        print(f'-------------------正在爬取第{page+1}页ip---------------------')
        time.sleep(random.randint(2,7))
        html=get_html(url)
        html_tree=get_html_tree(html)

        ip_lst=get_ip_lst(html_tree)
        port_lst=get_port_lst(html_tree)
        type_lst=get_type_lst(html_tree)

        file_write(ip_lst=ip_lst, port_lst=port_lst, type_lst=type_lst)

