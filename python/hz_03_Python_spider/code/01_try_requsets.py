import requests
import json

url = "http://www.biaud.com"

headers_uer = {"User-Agent":" Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Mobile Safari/537.36",
          "Referer": "http://fanyi.baidu.com/?aldtype=16047",
          "Cookie": "BAIDUID=474CA1AE138F945825111D8FBD511CEB:FG=1; BIDUPSID=09E3E7DB18DC6D2E90DAEEF408DC1903; PSTM=1533181042; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=3; H_PS_PSSID=26936_1447_21078_26350_20930; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1533357427; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1533357427; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1533357259,1533357427,1533357495; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1533357495; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"}


response = requests.get(url)

#response.encoding = "utf-8"
#print(response.text)
print(response.content.decode())

