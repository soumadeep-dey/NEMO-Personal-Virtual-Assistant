from requests_html import HTMLSession
from getuseragent import UserAgent

'''Using Google Scrapping'''
def check_temperature(query):
    try:
        if 'in' or 'of' or 'around' in query:
            query_list = list(query.split())
            if "in" in query:
                location = query_list[query_list.index("in") + 1]
            elif "of" in query:
                location = query_list[query_list.index("of") + 1]
            else:
                location = query_list[query_list.index("around") + 1]

    except: location = 'near me'
    
    try:
        s = HTMLSession()
        myuseragent = UserAgent("all", requestsPrefix=True).Random()
        
        url = f"https://www.google.com/search?q=weather+{location}"
        r = s.get(url, headers=myuseragent)

        temp = r.html.find('span#wob_tm', first=True).text
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
        desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
        return "Current Temperature is "+ temp + unit +" and weather forecast is "+ desc
    except:
        return "Sorry unable to find the given location."

# print(check_temperature("today's weather in delhi"))


'''Using API'''
# import requests
# def check_temperature(query):
# #    Api_Key = ""  # Paste Your API ID Here
#     try:
#         if 'in' or 'of' or 'around' in query:
#             query_list = list(query.split())
#             if "in" in query:
#                 location = query_list[query_list.index("in") + 1]
#             elif "of" in query:
#                 location = query_list[query_list.index("of") + 1]
#             else:
#                 location = query_list[query_list.index("around") + 1]

#     except: location = 'near me'

#     try:
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={Api_Key}"

#         result = requests.get(url)
#         data = result.json()

#         temprature = round(data['main']['temp'])
        
        
#         return "Current Temperature is "+ temprature

#     except:
#             return "Sorry unable to find the given location."

# print(temprature)

