import requests
import sys

def list_dns_records(api_token, zone_id):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'

    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dns_records = response.json()
        for record in dns_records['result']:
            print(f"Type: {record['type']}, Name: {record['name']}, Content: {record['content']}, ID: {record['id']}, TTL: {record['ttl']}, proxied: {record['proxied']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python list_dns_records.py <api_token> <zone_id>")
    else:
        api_token = sys.argv[1]
        zone_id = sys.argv[2]
        list_dns_records(api_token, zone_id)
