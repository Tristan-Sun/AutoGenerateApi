# coding: UTF-8

import httplib2
import urllib
import sys
import re

import xml.dom.minidom

# The request parameters which all method have.
COMMON_REQUEST_PARAMETERS = ('api_key', 'v', 'call_id', 'sig', 'client_info', 'format')

def writeToFile(fileName, content):
    f = open('F:\\%s.txt' % fileName, 'w')
    f.write(content)
    f.close()

class Parameter(object):
    def __init__(self):
        self.required = None
        self.name = None
        self.type = None
        self.description = None

    def __str__(self):
        return "%s\t%s\t%s" % (self.required, self.type, self.name)

class Api(object):
    def __init__(self):
        # group of this api
        self.group = None
        # name of this api
        self.name = None
        # decription of this api
        self.description = None
        # whether need sessionKey or not
        self.needSessionKey = None
        # who developed this api
        self.developer = None
        # url of the detail info page
        self.url = None

        # detail introduction
        self.introduction = None
        # request method
        self.method = None
        # request parameters
        self.parameters = list()

        # According Response
        self.responseName = None

    def addRequestParameter(self, parameter):
        if not parameter:
            return
        if parameter.name not in COMMON_REQUEST_PARAMETERS:
            if parameter.type == 'int':
                parameter.type = 'int32'
            elif parameter.type == 'long':
                parameter.type = 'int64'
            elif parameter.type == 'true\false':
                parameter.type = 'bool'
            self.parameters.append(parameter)

    def generateRequestParameter(self):
        if len(self.parameters) == 0 or self.name == None:
            return ''

        body = list()
        body.append('message ')
        for part in self.name.split('.'):
            body.append(part[0].capitalize() + part[1:])
        body.append('Request {\n')
        for parameter in self.parameters:
            body.append('\t%s\t%s\t%s\n' % (parameter.required, parameter.type, parameter.name))
        body.append('}\n\n')
        return ''.join(body)

    def __str__(self):
        return "%s\t%s\t%s\t%s\t%s" % (self.group, self.name, self.description, self.needSessionKey, self.developer)


DOMAIN = 'http://3g.d.xiaonei.com'
URL_PREFIX = DOMAIN + '/wiki/'
HOME_URL = URL_PREFIX + 'index.php'
# Url used to login.
API_URL = URL_PREFIX + 'api.php'
REST_API_EN_URL = HOME_URL + "/Renren_3G_RESTful_API_platform"

http = httplib2.Http()

# Login
userName = 'ËïÍ¤'.decode('gb2312').encode('UTF-8')
password = '123456'
    
headers = dict()
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Connection'] = 'Keep-Alive'

params = dict()
params['action'] = 'login'
params['format'] = 'xml'
params['lgname'] = userName
params['lgpassword'] = password

response, content = http.request(API_URL, method='POST', body=urllib.urlencode(params), headers=headers)

cookie = response.get('set-cookie')
xmldoc = xml.dom.minidom.parseString(content)
token = xmldoc.getElementsByTagName('login')[0].getAttribute('token')

headers['Cookie'] = cookie
params['lgtoken'] = token

response, content = http.request(API_URL, method='POST', body=urllib.urlencode(params), headers=headers)
xmldoc = xml.dom.minidom.parseString(content)
node = xmldoc.getElementsByTagName('login')[0]
status = node.getAttribute('result')
if status != 'Success':
    print "Not success..."
    exit()
print "Success Login..."

token = node.getAttribute('lgtoken')
userId = node.getAttribute('lguserid')
userName = urllib.quote(userName)
cookiePrefix = node.getAttribute('cookieprefix')

# Construct request headers
cookies = list()
cookies.append(cookie)
cookies.append(cookiePrefix + 'UserName=' + userName)
cookies.append(cookiePrefix + 'UserId=' + userId)
cookies.append(cookiePrefix + 'Token=' + token)

headers['Cookie'] = '; '.join(cookies)

# Get API Lists
response, content = http.request(REST_API_EN_URL, method='GET', headers=headers)

apis = []
tables = re.findall(r'<table.*?>.*?</table>', content, re.DOTALL)
table = tables[1]
currentGroup = None
currentDeveloper = None
for tr in re.findall(r'<tr.*?>.*?</tr>', table, re.DOTALL):
    tds = re.findall(r'<td.*?>(.*?)</td>', tr, re.DOTALL)
    tdsLength = len(tds)
    if tdsLength == 0:
        continue

    api = Api()
    if tdsLength == 5:
        currentGroup = tds[0].strip()
        currentDeveloper = tds[4].strip()
        api.group = currentGroup
        api.description = tds[2].strip()
        api.needSessionKey = tds[3].strip()
        api.developer = currentDeveloper
        match = re.search(r'<a href="(.+)" title=".+">(.+)</a>', tds[1])
        api.name = match.group(2)
        api.url = match.group(1)

    elif tdsLength == 4:
        currentDeveloper = tds[3].strip()
        api.group = currentGroup
        api.description = tds[1].strip()
        api.needSessionKey = tds[2].strip()
        api.developer = currentDeveloper
        match = re.search(r'<a href="(.+)" title=".+">(.+)</a>', tds[0])
        api.name = match.group(2)
        api.url = match.group(1)
    elif tdsLength == 3:
        api.group = currentGroup
        api.description = tds[1].strip()
        api.needSessionKey = tds[2].strip()
        api.developer = currentDeveloper
        match = re.search(r'<a href="(.+)" title=".+">(.+)</a>', tds[0])
        api.name = match.group(2)
        api.url = match.group(1)

    apis.append(api)

print "Api counts: %s" % (len(apis))

# Update each api's detail information.
for api in apis:
    response, content = http.request('%s%s' % (DOMAIN, api.url), method='GET', headers=headers)
    match = re.search(r'id="(Rsponse|Response|Return_Value|\.E8\.BF\.94\.E5\.9B\.9E\.E5\.80\.BC)".*?<pre>\s*(message)?(?P<response>.*?){.*?</pre>', content, re.DOTALL | re.IGNORECASE)
    # If responseName is None, then we set default value.
    if not match:
        api.responseName = 'SubmitResponse'
    elif match.group('response') == None or match.group('response').strip() == '':
        api.responseName = 'SubmitResponse'
    else:
        api.responseName = match.group('response').strip()

    print 'responseName = %s' % (api.responseName)

    match = re.search(r'id="(API_Description|API_Intruduction|API_Introduction|\.E6\.8E\.A5\.E5\.8F\.A3\.E8\.AF\.B4\.E6\.98\.8E)".*?<p>(?P<introduction>.+?)</p>.*?id="(Request_Method|\.E6\.8F\.90\.E4\.BA\.A4\.E6\.96\.B9\.E5\.BC\.8F)".*?<p>.*?<a.*?>http://api.m.renren.com/api/(?P<method>.*?)</a>.*?</p>.*?id="(Parameter_List|Request_Parameter[s]?_List|\.E8\.AF\.B7\.E6\.B1\.82\.E5\.8F\.82\.E6\.95\.B0\.E5\.88\.97\.E8\.A1\.A8)".*?<table class="wikitable".*?>(?P<table>.*?)</table>', content, re.DOTALL | re.IGNORECASE)
    # The order of introduction and method maybe changed, so we need to match for the second time.
    if not match:
        match = re.search(r'id="(API_Description|Request_Method|\.E6\.8F\.90\.E4\.BA\.A4\.E6\.96\.B9\.E5\.BC\.8F)".*?<p>.*?<a.*?>http://api.m.renren.com/api/(?P<method>.*?)</a>.*?</p>.*?id="(API_Intruduction|API_Introduction|\.E6\.8E\.A5\.E5\.8F\.A3\.E8\.AF\.B4\.E6\.98\.8E)".*?<p>(?P<introduction>.+?)</p>.*?id="(Parameter_List|Request_Parameter[s]?_List|\.E8\.AF\.B7\.E6\.B1\.82\.E5\.8F\.82\.E6\.95\.B0\.E5\.88\.97\.E8\.A1\.A8)".*?<table class="wikitable".*?>(?P<table>.*?)</table>', content, re.DOTALL | re.IGNORECASE)
    if not match:
        print 'api %s not match...' % (api.name)
        continue

    api.introduction = match.group('introduction').strip()
    api.method = match.group('method').strip().replace('/', '.')

    required = 'required'
    for tr in re.findall(r'<tr.*?>.*?</tr>', match.group('table'), re.DOTALL):
        tds = re.findall(r'<td.*?>(.*?)</td>', tr, re.DOTALL)
        tdsLength = len(tds)
        if tdsLength == 0:
            continue
        parameter = Parameter()
        if tdsLength >= 4:
            if tds[0].strip() != '':
                required = tds[0].strip()
            parameter.required = required
            parameter.name = tds[1].strip()
            parameter.type = tds[2].strip()
            parameter.description = tds[3].strip()
        elif tdsLength == 3:
            parameter.required = required
            parameter.name = tds[0].strip()
            parameter.type = tds[1].strip()
            parameter.description = tds[2].strip()

        api.addRequestParameter(parameter)

f = open('F:\\test.txt', 'w')
for api in apis:
    f.write(api.generateRequestParameter())
    #print api.responseName
f.close()
