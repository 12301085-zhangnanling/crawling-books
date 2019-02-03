import urllib3.request
import cookie06
import cookielib
import urllib2
import urllib

c = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
login_path = 'https://accounts.douban.com/passport/login'
data = {'name': '18810291286', 'passwd': '0307ling'}
post_info = urllib.urlencode(data)
request = urllib2.Request(login_path, post_info)
html = opener.open(request).read()

if c:
    print c

for item in c:
    print 'Name = '+item.name
    print 'Value = '+item.value
c.save('cookie.txt')

# cookie = cookielib.CookieJar()
# handler=urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.douban.com')
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value


# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)