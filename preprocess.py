import re
import pandas as pd
from urllib.parse import urlparse
import requests
from datetime import datetime

# Suspicious keyword list
suspicious_keywords = ["login", "verify", "update", "free", "bonus",
                       "click", "secure", "account", "banking"]

def count_special_chars(url):
    return sum(not c.isalnum() for c in url)

def keyword_presence(url):
    return any(keyword in url.lower() for keyword in suspicious_keywords)

def get_domain_age(domain):
    try:
        # WHOIS API (free alternative required)
        api = f"https://api.api-ninjas.com/v1/whois?domain={domain}"
        response = requests.get(api, headers={'X-Api-Key': 'YOUR_API_KEY'})
        data = response.json()

        creation_date = data.get('creation_date')
        if creation_date:
            creation_date = datetime.fromisoformat(creation_date)
            age_days = (datetime.now() - creation_date).days
            return age_days
    except:
        return -1  # Unknown age
    return -1


def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    return {
        "url_length": len(url),
        "special_chars": count_special_chars(url),
        "has_suspicious_keywords": int(keyword_presence(url)),
        "domain_age": get_domain_age(domain)
    }
