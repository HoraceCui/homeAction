import requests
import sys

def update_dns_record(api_token,zone_id, record_id, record_name, record_type, record_content, proxied=True,ttl=1):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"

    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    data = {
        "type": record_type,
        "name": record_name,
        "content": record_content,
        "ttl": ttl,
        "proxied": proxied
        }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print("DNS record updated successfully.")
        return response.json()
    else:
        print(f"Failed to update DNS record: {response.status_code}")
        return response.json()

# Example usage when calling the module
if __name__ == "__main__":
    if len(sys.argv) != 7:
        print(len(sys.argv))
        print("Usage: python update_dns_record.py api_token, zone_id, record_id, record_name, record_type, record_content")
    else:
        # Replace with your actual data
        api_token = sys.argv[1]
        zone_id = sys.argv[2]
        record_id = sys.argv[3]
        record_name = sys.argv[4]
        record_type = sys.argv[5]
        record_content = sys.argv[6]
        #proxied = sys.argv[7]
        result = update_dns_record(api_token, zone_id, record_id, record_name, record_type, record_content)

        print(result)
