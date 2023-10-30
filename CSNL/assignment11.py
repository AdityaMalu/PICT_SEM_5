import socket

def ip_to_url(ip_address):
    try:
        url = socket.gethostbyaddr(ip_address)
        return url[0]
    except socket.herror:
        return "Could not resolve the IP to a URL."

def url_to_ip(url):
    try:
        ip_list = [addrinfo[4][0] for addrinfo in socket.getaddrinfo(url, None)]
        return ip_list
    except socket.gaierror:
        return "Could not resolve the URL to an IP address."

while True:
    print("Choose an option:")
    print("1. IP to URL")
    print("2. URL to IP")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        ip_address = input("Enter an IP address: ")
        result = ip_to_url(ip_address)
        print("URL for IP", ip_address, "is:", result)
    elif choice == '2':
        url = input("Enter a URL: ")
        result = url_to_ip(url)
        if isinstance(result, list):
            print("IP addresses for URL", url, "are:", ", ".join(result))
        else:
            print(result)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
