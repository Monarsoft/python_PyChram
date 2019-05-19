# utf-8
import requests
#print(eval(input("na:")))

ulr = "http://www.renren.com/967360453/profile"

headers = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
def _cookie():
    cookie = "anonymid=jkl33937-mkxpcq; depovince=GW; _r01_=1; ick_login=092b660b-7787-4b73-9bac-37ecec09dc6c; id=967360453; JSESSIONID=abcTf_9yUB4_caxgYAzuw; __utmc=151146938; jebe_key=8df69edf-3187-497b-a746-0bd75061b41c%7C9ff7ad4a6dd185af5ce38adc01354e46%7C1533729778508%7C1%7C1533816236623; t=07ac1765982493b2e7502ff1b6de901b3; societyguester=07ac1765982493b2e7502ff1b6de901b3; xnsid=e16d1908; jebecookies=bed635ee-c75d-4359-9571-6ca0d59711b4|||||; wp_fold=0; __utma=151146938.166676804.1533729789.1533729789.1533816292.2; __utmz=151146938.1533816292.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/967360453/profile; __utmt=1; __utmb=151146938.2.10.1533816292"
    return cookie

_cookie_dic = {i.split("=")[0]:i.split(";")[-1] for i in _cookie().split(";")}
#print(_cookie_dic)
try:
    response = requests.get(ulr,headers=headers,cookies=_cookie_dic)
except Exception as result:
    print(result)
with open("qqkongjian2.html", encoding="utf-8") as f:
    f.write(response.content.decode())