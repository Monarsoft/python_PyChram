import requests

class TestJenkins:
  def test_jenkins(self):
    response = requests.get("http://baidu.com")
    print(response)
