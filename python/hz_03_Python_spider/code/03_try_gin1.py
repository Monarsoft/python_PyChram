#   UTF-8   
import requests
from retrying import retry

url = "https://user.qzone.qq.com/1516042721"
headers_gin = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36","Cookie":"pgv_pvi=2087910400; ptui_loginuin=1516042721; pt2gguin=o1516042721; RK=RkQM2b5lbT; ptcz=7f37589295de275ff9917218abff59631caad09212bcb9f639aece32d4fe41bd; pgv_pvid=8556781236; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0; pgv_si=s1376966656; ptisp=ctc; _qpsvr_localtk=0.7047655101985846; pgv_info=ssid=s2986192938; uin=o1516042721; skey=@OY4DZNK8p; p_uin=o1516042721; pt4_token=yCC06N-UGQtiT2rf3Ev8JeNZUcAqpZ0eufADs7j7H8A_; p_skey=QSchbLwp0uI1ZL-if7Oep4h0f5c2PVqFTHfbvvJ3CFM_; fnc=2; Loading=Yes; qzmusicplayer=qzone_player_1516042721_1533529959185; qqmusic_uin=1516042721; qqmusic_key=@OY4DZNK8p; qqmusic_fromtag=6; 1516042721_todaycount=0; 1516042721_totalcount=14792"}

resptonse = requests.get(url,headers=headers_gin)

with open("qqkongjian.html","w",encoding="utf-8") as f:
    f.write(resptonse.content.decode())
    print("写入成功！")
