import unittest
import requests

class TestAPIs(unittest.TestCase):

    def test_weather_api(self):
        # 自定义地区天气信息查询，查询“南京市”的天气
        url = 'https://api.oioweb.cn/api/weather/weather?city_name=南京市'
        response = requests.get(url)
        data = response.json()

        # 检查返回状态码
        self.assertEqual(data['code'], 200, "API returned a non-200 status code")

        # 获取并打印city_name和current_condition
        city_name = data['result']['city_name']
        current_condition = data['result']['current_condition']
        print(f"City: {city_name}, Condition: {current_condition}")
        
         # 进一步检查返回的内容是否符合预期
        self.assertIsNotNone(city_name, "City name is None")
        self.assertIsNotNone(current_condition, "Current condition is None")


    def test_icp_api(self):
        # 查询域名备案信息，查询domain为qq.com
        url = 'https://api.oioweb.cn/api/site/icp?domain=qq.com'
        response = requests.get(url)
        data = response.json()

        # 检查返回状态码
        self.assertEqual(data['code'], 200, "API returned a non-200 status code")

        # 获取并打印company_name和site_name
        company_name = data['result']['company_name']
        site_name = data['result']['site_name']
        print(f"Company: {company_name}, Site: {site_name}")
        
        # 进一步检查返回的内容是否符合预期
        self.assertIsNotNone(company_name, "Company name is None")
        self.assertIsNotNone(site_name, "Site name is None")

if __name__ == '__main__':
    unittest.main()
