import requests, time
from datetime import datetime
import pywhatkit as pyw

def main():
    group_id = "CRXy1CK8JroLwDr2yVOPt0"
    rate = get_exchange_rate()
    today = datetime.strftime(datetime.today(), "%a %d %b %Y")
    message = f"Today on {today} the exchange rate is as follows: \n1 GBP is worth AED {round(rate, 3)}"
    pyw.sendwhatmsg_to_group_instantly(group_id, message)
    time.sleep(3)
    #contact = "+971503517343"
    #pyw.sendwhatmsg_instantly(contact, message, )

def get_exchange_rate():
    API_KEY = "1861758373bede382c3fe15fdfba82df"
    BASE_URL = "http://api.exchangeratesapi.io/v1/"
    endpoint = "latest"
    request_url = f"{BASE_URL}{endpoint}?access_key={API_KEY}"
    resp = requests.get(request_url)

    print(resp.status_code)
    if resp.ok:
        data = resp.json()
        AED = data["rates"]["AED"]
        GBP = data["rates"]["GBP"]
        return AED / GBP
    else:
        print("Error Accessing data!")

if __name__ == "__main__":
    main()