# https://www.geeksforgeeks.org/performing-google-search-using-python-code/

from urllib.parse import urlparse

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

import time
# to search
query = ["hurdacimdan.com","domain:hurdacimdan.com", "www.hurdacimdan.com","https://hurdacimdan.com/","https://www.hurdacimdan.com/"]

network= ["com","net","org","gov",".tr"]
notdomain=["hurdacimdan.com", "www.hurdacimdan.com", "www.facebook.com",
           "facebook.com","www.twitter.com","twitter.com","tr.linkedin.com",
           "linkedin.com", "www.linkedin.com"]

print("Start")
print("Please, Wait")
try:
    for item in query:
        time.sleep(0.5)
        for j in search(item, tld="co.in", num=100):
            # Burda .txt dosya okuma ve kayıt etmede kesin yeri burası
            with open("disavow.txt", "r+") as f:
                liste= f.read().split()
                domain=urlparse(j).netloc
                dm="domain:"+domain
                print(dm)
                time.sleep(0.5)
                # .txt dosyasında yoksa
                if dm not in liste:
                    time.sleep(0.1)
                    # Domain adresinin sonu com, net, org bitmiyorsa
                    if domain[-3:] not in network:
                        time.sleep(0.2)
                        if domain not in notdomain:
                            f.write(dm+"\n")
except:
    print("Error: HTTP Error 429: Too Many Requests")
    print("Description: Try again later. :( ")
else:
    print("Finish")
    print("New disavow.txt created :)")
    print("Good By")



