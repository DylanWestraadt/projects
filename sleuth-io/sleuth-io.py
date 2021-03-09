import requests

def trace(ip):
    response = requests.get("https://api.hackertarget.com/mtr/?q={}".format(ip))
    r = response.text
    return r

def revdns(ip):
    response = requests.get("https://api.hackertarget.com/reversedns/?q={}".format(ip))
    r = response.text
    return r

def whois(ip):
    response = requests.get("https://api.hackertarget.com/whois/?q={}".format(ip))
    r = response.text
    return r
def request_ip(ip):
    token = '7d226dd187e12c'
    response = requests.get('http://ipinfo.io/{}/?token={}'.format(ip,token))
    r = response.json()
    return r

print(
    """
       ...               ..                                s                            .                
   .x888888hx    : x .d88"                                :8      .uef^"               @88>              
  d88888888888hxx   5888R                 x.    .        .88    :d88E                  %8P          u.   
 8" ... `"*8888%`   '888R        .u     .@88k  z88u     :888ooo `888E                   .     ...ue888b  
!  "   ` .xnxx.      888R     ud8888.  ~"8888 ^8888   -*8888888  888E .z8k            .@88u   888R Y888r 
X X   .H8888888%:    888R   :888'8888.   8888  888R     8888     888E~?888L          ''888E`  888R I888> 
X 'hn8888888*"   >   888R   d888 '88%"   8888  888R     8888     888E  888E            888E   888R I888> 
X: `*88888%`     !   888R   8888.+"      8888  888R     8888     888E  888E            888E   888R I888> 
'8h.. ``     ..x8>   888R   8888L        8888 ,888B .  .8888Lu=  888E  888E 88888888   888E  u8888cJ888  
 `88888888888888f   .888B . '8888c. .+  "8888Y 8888"   ^%888*    888E  888E 88888888   888&   "*888*P"   
  '%8888888888*"    ^*888%   "88888%     `Y"   'YP       'Y"    m888N= 888>            R888"    'Y"      
     ^"****""`        "%       "YP'                              `Y"   888              ""               
                                                                      J88"                               
                                                                      @%                                 
                                                                    :"                                   
"""
)
print(" Welcome to Sleuth-io. This program does some cool stuff that includes Tracerouting, Whois checks, Reverse DNS and IP Geolocating.")
print("\n So select what you would like to do:")
user_in = input("\n [1] Tracerouting \n [2] Reverse DNS search \n [3] WHOIS Lookup \n [4] IP-Geolocation \n \n >>> ")


if user_in == "1":
    print("\n Ok so lets start doing this. We'll sleuth everything out for you.\n Just enter an ip address: ")
    ip = input("\n >>> ")
    trace = trace(ip)
    print("[Results:] \n",trace)
elif user_in == "2":
    print("\n Ok so lets start doing this. We'll sleuth everything out for you.\n Just enter an ip address: ")
    ip = input("\n >>> ")
    revdns = revdns(ip)
    print("[Results:]",revdns)
elif user_in == "3":
    print("\n Ok so lets start doing this. We'll sleuth everything out for you.\n Just enter an ip address: ")
    ip = input("\n >>> ")
    whois = whois(ip)
    print("[Results:] \n" , whois)
elif user_in == "4":
    print("\n Ok so lets start doing this. We'll sleuth everything out for you.\n Just enter an ip address: ")
    ip = input("\n >>> ")
    trace = request_ip(ip)
    print("\n" , trace)
else:
    print("Try a valid option buddy")


