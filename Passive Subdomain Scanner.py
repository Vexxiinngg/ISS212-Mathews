#PassiveSubdomainScanner
#Lauren Mathews
#Resources: Jen Moody Past Scripts and ChatGPT
import socket

# The Target domain
domain = ("example.com")

#The subdomains to be checked
subdomains = ["www", "mail", "blog", "dev", "api", "ftp", "test"]

# File that will save found subdomains
output_file = ".venv/TheDiscovered_subdomains.txt"

with open(output_file, "w") as file:
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            # Trying to resolve the subdomain
            ip = socket.gethostbyname(subdomain)
            print(f"[+] Found: {subdomain} - {ip}")
            file.write(f"{subdomain} - {ip}\n")
        except socket.gaierror:
            # If it can't resolve, prompt to skip it
            print(f"[-] Not found: {subdomain}")

print(f"\nScan complete. Results saved to {output_file}")