'''@contextmanager'''


'''urllib   
http://c.biancheng.net/view/2640.html
urllib 模块则包含了多个用于处理 URL 的子模块：
urllib.request：这是最核心的子模块，它包含了打开和读取 URL 的各种函数。
urllib.error：主要包含由 urllib.request 子模块所引发的各种异常。
urllib.parse：用于解析 URL。
urllib.robotparser：主要用于解析 robots.txt 文件。'''

from urllib import request,parse


#简单发送1个get请求到指定页面，获取http响应
with request.urlopen('https://www.baidu.com/') as f:
    data=f.read()
    print('status: {} {}'.format(f.status,f.reason))
    for k,v in f.getheaders():
        print('%s %s' %(k,v))
    print('data: %s' % data.decode('utf-8'))

#使用request对象，添加header,模拟浏览器发送请求
req=request.Request('https://www.baidu.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('status: {} {}'.format(f.status,f.reason))
    for k,v in f.getheaders():
        print('{} {}'.format(k,v))
    print(f.getheaders())
    print('data: %s',f.read().decode('utf-8'))

#使用request对象，添加请求参数，模拟发送get请求
from urllib import parse,request
para=parse.urlencode({'name':'fkit','password':'123888'})
url='http://localhost:8888/test/get.jsp?%s' %para
print(url)
req=request.Request(url)
with request.urlopen(req) as f:
    print(f.read().decode('utf-8'))


#将参数data以bytes方式传入，模拟发送post求情
from urllib import request,parse
import  json

print('Visit to www.weibo.com 。。。')
email=input('请输入账户名称：')
passwd=input('请输入密码：')
data=parse.urlencode([('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req=request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data=data.encode('utf-8')) as f:
    print('status: {} {}'.format(f.status,f.reason))
    for k,v in f.getheaders():
        print('{} {}'.format(k,v))
    print('data: %s' % f.read().decode('utf-8'))


'''
运行结果：
Visit to www.weibo.com 。。。
请输入账户名称：wjing18@126.com
请输入密码：18WODESHIBASUI
status: 200 OK
Server nginx/1.6.1
Date Thu, 24 Oct 2019 07:27:23 GMT
Content-Type text/html
Transfer-Encoding chunked
Connection close
Vary Accept-Encoding
Cache-Control no-cache, must-revalidate
Expires Sat, 26 Jul 1997 05:00:00 GMT
Pragma no-cache
Access-Control-Allow-Origin https://passport.weibo.cn
Access-Control-Allow-Credentials true
DPOOL_HEADER lich243
Set-Cookie login=609423641c81693ee710ee69b0d0e34c; Path=/
data: {"retcode":50011002,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"wjing18@126.com","errline":661}}
'''

#coding:utf-8


'''下面先介绍 urllib.parse 子模块中用于解析 URL 地址和查询字符串的函数：
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)：该函数用于解析 URL 字符串。程序返回一个 ParseResult 对象,可以获取解析出来的数据。
urllib.parse.urlunparse(parts)：该函数是上一个函数的反向操作,用于将解析结果反向拼接成 URL 地址。
urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')：该该函数用于解析查询字符串（application/x-www-form-urlencoded 类型的数据）,并以 dict 形式返回解析结果。
urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')：该函数用于解析查询字符串（application/x-www-form-urlencoded 类型的数据）,并以列表形式返回解析结果。
urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)：将字典形式或列表形式的请求参数恢复成请求字符串。该函数相当于 parse_qs()、parse_qsl() 的逆函数。
urllib.parse.urljoin(base, url, allow_fragments=True)：该函数用于将一个 base_URL 和另一个资源 URL 连接成代表绝对地址的 URL。
'''
from urllib import parse,request

#解析访问url返回的results
result = parse.urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(type(result),result)
print('scheme:', result.scheme,result[0])
print('主机和端口名：',result.netloc,result[1])
print('主机名称：',result.hostname)
print('端口名称：',result.port)
print('资源路径：',result.path,result[2])
print('访问参数：',result.params,result[3])
print('查询字符串：',result.query,result[4])
print('fragment:',result.fragment,result[5])
print(result.geturl)

#将解析的结果拼接为url
result=parse.urlunparse(('http','www.crazyit.org:80','/index.php','yeeku','name=fkit','frag'))
print('url=',result)

#解析字符串以dict形式返回结果
result=parse.parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)

#解析字符串以list形式返回结果
result=parse.parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)

#将dict或list形式恢复为字符串
res=parse.urlencode(result)
print(res)

'''urljoin() 函数负责将两个 URL 拼接在一起，返回代表绝对地址的 URL。这里主要可能出现 3 种情况： 
被拼接的 URL 只是一个相对路径 path（不以斜线开头），那么该 URL 将会被拼接到 base 之后，如果 base 本身包含 path 部分，则用被拼接的 URL替换 base 所包含的 path 部分。
被拼接的 URL 是一个根路径 path（以单斜线开头），那么该 URL 将会被拼接到 base 的域名之后。
被拼接的 URL 是一个绝对路径 path（以双斜线开头），那么该 URL将会被拼接到 base 的 scheme 之后。'''

# 被拼接URL不以斜线开头
result = parse.urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result) # http://www.crazyit.org/users/help.html
result = parse.urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result) # http://www.crazyit.org/users/book/list.html
# 被拼接URL以斜线（代表根路径path）开头
result = parse.urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result) # http://www.crazyit.org/help.html
# 被拼接URL以双斜线（代表绝对URL）开头
result = parse.urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result) # http://help.html

