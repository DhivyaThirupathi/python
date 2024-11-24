import re

def count_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return len(emails), emails

def extract_phone_numbers(text):
    phone_pattern = r'\b(\+?\d{1,3})?[-. (]?(\d{3})[-. )]?(\d{3})[-. ]?(\d{4})\b'
    phone_numbers = re.findall(phone_pattern, text)
    formatted_numbers = ["".join(number) for number in phone_numbers]
    return formatted_numbers

def find_pattern_positions(text, pattern):
    pattern_compiled = re.compile(pattern)
    positions = [(match.start(), match.end()) for match in pattern_compiled.finditer(text)]
    return positions

def find_urls(text):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(url_pattern, text)
    return urls

def find_ip_addresses(text):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ip_addresses = re.findall(ip_pattern, text)
    return ip_addresses

# Example usage
text = """ I'm MCA students at CIT ,My mail id is  2403717662222040@cit.edu.in and my personal mail-id is "devi2103@gmail.com" 
you can reach me at 9012345679 .I'm interested in Data science.Data science is a fascinating field. Data science includes statistics.
Visit me at https://example.com or http://example.net.Server IP: 192.168.1.1."""
email_count, emails = count_emails(text)
print(f"Number of emails: {email_count}")
print(f"Emails found: {emails}")

phone_numbers = extract_phone_numbers(text)
print(f"Phone numbers found: {phone_numbers}")

pattern = r'\bData science\b'
positions = find_pattern_positions(text, pattern)
print(f"Positions of 'data science': {positions}")

urls = find_urls(text)
ip_addresses = find_ip_addresses(text)
print(f"URLs found: {urls}")
print(f"IP addresses found: {ip_addresses}")