import requests

def get_weather(api_key, location):
    url = f"https://api.seniverse.com/v3/weather/daily.json?key={api_key}&location={location}&language=zh-Hans&unit=c&start=0&days=3"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["results"][0]["daily"]
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None

if __name__ == "__main__":
    api_key = "SS1bl-Np_N8JKlArP"  # 替换为你的知心网API密钥
    location = "hangzhou"  # 你想查询的地点
    weather_data = get_weather(api_key, location)
    if weather_data:
        for day in weather_data:
            print(f"{day['date']}：{day['text_day']}，{day['low']}℃ ~ {day['high']}℃")
    else:
        print("无法获取天气数据")
