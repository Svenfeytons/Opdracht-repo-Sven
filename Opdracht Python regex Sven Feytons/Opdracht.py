import requests

url = 'https://api.domainsdb.info/v1/domains/search'
params = {'domain': 'syntra.be'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.reason}")
    
    
    
    
import json
import re
import yaml




data = '{"domains": [{"domain": "syntra.be", "create_date": "2022-06-15T05:58:02.276425", "update_date": "2022-06-15T05:58:02.276428", "country": "BE", "isDead": "False", "A": ["188.93.156.240"], "NS": ["ns3.belnet.be", "nsmaster.belnet.be", "ns1.belnet.be", "ns2.belnet.be"], "CNAME": null, "MX": null, "TXT": ["a3388b287798454ab5580af5f9ac21fd"]}], "total": 1, "time": "499", "next_page": null}'

data_dict = json.loads(data)

create_date = data_dict["domains"][0]["create_date"]

match = re.match(r'(\d{4})-(\d{2})-(\d{2})', create_date)

year = match.group(1)
month = match.group(2)
day = match.group(3)

provider = r'belnet'
if re.search(provider, str(data_dict)):
    provider_output = f"{provider}"
else:
    provider_output = ''

a_records = data_dict["domains"][0]["A"]
ip_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
ip_addresses = []
for a_record in a_records:
    if re.match(ip_regex, a_record):
        ip_addresses.append(a_record)
        
country = r'BE'
if re.search(country, str(data_dict)):
    country_output = f"{country}"
else:
    country_output = ''

output_dict = {
    'Year': year,
    'Month': month,
    'Day': day,
    'Provider': provider_output,
    'IP addresses': ip_addresses,
    'Country': country_output
}

with open('Output.yaml', 'w') as file:
    documents = yaml.dump(output_dict, file)