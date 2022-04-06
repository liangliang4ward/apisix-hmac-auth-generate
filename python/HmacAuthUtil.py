
import base64
import hashlib
import hmac
import datetime
from urllib import parse


def generate_sign_string(request_url, method, ak, sk):
    o = parse.urlparse(request_url)
    query_array = parse.parse_qs(o.query)
    new_query = []
    for k, v in query_array.items():
        new_query.append(parse.unquote(k)+'='+parse.unquote(v[0]))
    new_query.sort()
    query_str = '&'.join(new_query)
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    gmt_date = datetime.datetime.utcnow().strftime(GMT_FORMAT)
    sign_str = method+'\n'+o.path+'\n'+query_str+'\n'+ak+'\n'+gmt_date+'\n'
    message = bytes(sign_str, 'utf-8')
    secret = bytes(sk, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    hash.hexdigest()
    signature = base64.b64encode(hash.digest()).decode("utf-8")
    print("Date:"+gmt_date)
    print("X-HMAC-ACCESS-KEY:"+ak)
    print("X-HMAC-SIGNATURE:"+str(signature))
    print("X-HMAC-ALGORITHM:hmac-sha256")
    return signature


url="http://xxx:9080/xx/xxx/xxxx/post?test=123&v=123"
generate_sign_string(url, "POST", "test", "tet")