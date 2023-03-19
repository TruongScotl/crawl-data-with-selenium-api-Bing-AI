# crawl datawith selenium and api Bing AI
* API Bing Chat follow here: https://github.com/acheong08/EdgeGPT
* API Google map follow here: https://github.com/googlemaps/google-maps-services-python
This repo crawl information of company: 
email: using api Bing Chat for crawl data, the format to search: 'get email of' + name
fanpage: using selenium, format: 'facebook fanpage' + name 
taxcode, phone: using selenium, format: website taxcode + name (usually phone will come with taxcode)
latitude, longitude: using api Google map from google, input: address
* also some function like: check valid email, parser email, read data input,.. from utils file
