# 作者：aoyijiaozhu
# 创建时间：2023/1/14 18:41
# 修改时间：2023/8/16
# 多线程测试代理池的timeout
# 返回时间dead_time,测试网址目前用的是小红书。
import time
import requests
import txt_to_dict
from concurrent.futures import ThreadPoolExecutor
dead_time=1

def proxies_pool_test(proxy):   #测试ip代理，返回单个ip（字典格式），只保持dead_time响应时间内的
    print('现在测试的是'+str(proxy) )
    #url = 'http://httpbin.org/ip'
    url='https://xiaohongshu.com/discove'   #测试用的网址
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    try:
        response=requests.get(url, headers=headers, proxies=proxy)
    except:
        print(str(proxy) + '超时，不合格')
    else:
        if response.elapsed.total_seconds()<dead_time:    #返回dead_time内响应内的ip
            print(str(proxy) + '-----' + str(response.elapsed.total_seconds()) + '-----' + '合格')
            return proxy

if __name__ == '__main__':
    #打开文件
    file = open('C:\\Users\\Administrator\\Downloads\\HTTP_ProxiesPool.txt', 'r')    #待测试文件
    new_file = open(f'C:\\Users\\Administrator\\Downloads\\New_HTTP_ProxiesPool_{dead_time}s.txt', 'w')  #测试成功的存放在这里

    proxies_lst = txt_to_dict.transform_lines(file) #把txt内容转换为字典列表
    start_time=time.time()
    with ThreadPoolExecutor() as pool:  #创建线程池
        results=pool.map(proxies_pool_test,proxies_lst)
    results=list(results)   #把得到的生成器转换为list

    for result in results:  #将结果数据写入新文件
        if  result!=None:
            new_file.write(str(result)+'\n')

    end_time=time.time()
    print('耗时: '+str(end_time-start_time)+' s')

    #关闭文件
    file.close()
    new_file.close()








