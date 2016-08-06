import names
import requests



#r = requests.post('https://www.spotify.com/us/xhr/json/sign-up-for-spotify.php', headers=headers)
#print(r.text)

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})


r1 = session.get("https://www.spotify.com/us/signup/")

lineArray = r1.text.split("\n")

for lineOfHTML in lineArray:
  if "name=\"sp_csrf\"" in lineOfHTML:
    componentArray = lineOfHTML.split("\"")
    print lineOfHTML
    break

print componentArray

print componentArray[5]

username = names.get_full_name().replace(" ", "")+"69".lower()

print username
payload = { "sp_csrf":componentArray[5],
"creation_flow":"1",
"forward_url":"https://www.spotify.com/us/download/",
"signup_pre_tick_eula":"true",
"username":username,
"password":username,
"email":username+"@gmail.com",
"confirm_email":username+"@gmail.com",
"dob_month":"03",
"dob_day":"24",
"dob_year":"1994",
"gender":"male",
"thirdpartyemail":"true"
}

r2 = session.post('https://www.spotify.com/us/xhr/json/sign-up-for-spotify.php', data=payload)
print r2.text

r25 = session.get('https://play.spotify.com')
print r25.text


#log in to web player
r3 = session.post('https://play.spotify.com/xhr/json/auth.php', data)
#print r3.text

r4 = session.get('https://play.spotify.com/track/4IDdUssauEYJ9kTit6tOU6')
#print r4.text


# POST /xhr/json/auth.php HTTP/1.1
# Host: play.spotify.com
# Connection: keep-alive
# Content-Length: 1382
# X-NewRelic-ID: VQ8PU1FTGwIFUFNVAAkO
# Origin: https://play.spotify.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
# Content-type: application/x-www-form-urlencoded
# Accept: */*
# DNT: 1
# Referer: https://play.spotify.com/
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-US,en;q=0.8
# Cookie: sp_t=1776725245ce120c53f6d1bcb1830008; sp_new=1; optimizelyEndUserId=oeu1470510551430r0.38182152006797; fbm_174829003346=base_domain=.spotify.com; mp_mixpanel__c=0; mp_329e66c6399f2a6f728674b8c0062881_mixpanel=%7B%22distinct_id%22%3A%20%221566143aded25c-079f02fec00721-37637b02-13c680-1566143adee19c%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.spotify.com%2Fus%2Fdownload%2Fmac%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.spotify.com%22%7D; sp_landing=play.spotify.com%2F; sp_landingref=https%3A%2F%2Fwww.google.com%2F; plp=cd68cfa0ace62ecda7a1db90a515d7e30dd6976b; spp_1f8011eb=eyJib29rbWFya19zZWVuIjp0cnVlfQ__; fbsr_174829003346=6txmwMW2Csp70tu2_V_k6xx84aHSH4viLXSt4tU74Us.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURqUkJ6T2xpWFhSU3FKd01tQ3Z5LTVmaEJwUmpaQWxiV05KWWM0YW8yLTQxWGNNZGIzaVVxUDhPQkxrWElMekdVbGpEZldmOTJXb1NEemlTd0JHN3hMQXFkOW9IcTZSX193RkF2dzFSMVZMTy0wd0lmUjExU1d1bTUyTmVFS1d0cVdONkhqcXpzTXVuVzVreWxPOTJ5WnBBVy1wN1F4alE2dHVDSlVFeFAtNXRzdk0tTTFTVTF0SXJLNjhMNWQ3bXN0QndjMzM0ZzRFOWRYNEl6emRaaVJ2V2JsQk9nZXV2Q29KUFJteFI0SnozeUVtV3ZZMU8tUm52aVpLUUtKYURzS2oyN2hidlExLVZ6ZzZIU3FMOFY1TlRGNm03YU9YOGs5b19CMU40cUJpSVRYTk5GMmNTd1c0WVpwT3ZSVzJXNCIsImlzc3VlZF9hdCI6MTQ3MDUxNzU2OSwidXNlcl9pZCI6IjE1MTYzMDQ2NTIifQ; spot=%7B%22t%22%3A1470517589%2C%22m%22%3A%22us%22%2C%22p%22%3A%22open%22%7D; justRegistered=null; sp_dc=AQAawPhfGBVRM3hUDmiGIBuN-ngG8idaR53gSOOJbYS8lXXXVR4RGTuayiR5fOS7dYCt8xsO-CvcMMhbK_vGJzjP; optimizelySegments=%7B%22172210784%22%3A%22none%22%2C%22172815652%22%3A%22referral%22%2C%22172898846%22%3A%22false%22%2C%22173064250%22%3A%22gc%22%2C%223210740148%22%3A%22true%22%7D; optimizelyBuckets=%7B%226336271351%22%3A%226340231362%22%7D; __tdev=VwV1c6bJ; __tvis=oZtvVcgC; __tums=00c94f031e97486e8a4d; __tumi=00c94f031e97486e8a4d; from_wp=1; locale=en; sp_fi=1; sp_cc=1; spp_08734339=eyJwcyI6IjAifQ__; __utma=200548975.2009761211.1470510552.1470510686.1470517773.2; __utmb=200548975.47.9.1470518925152; __utmc=200548975; __utmz=200548975.1470510686.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga=GA1.2.2009761211.1470510552; _gali=sp-login-form



