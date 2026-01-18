import os
import requests
import json
from datetime import datetime

def fetch_schedule_hearing_data():
    """
    Fetch schedule hearing data from ECI API
    """
    bearer_token = os.getenv('BEARER_TOKEN')
    
    if not bearer_token:
        print("❌ Error: BEARER_TOKEN environment variable not set")
        return None
    
    url = "https://gateway-officials.eci.gov.in/api/v1/s25/scheduleHearing/getSchedulingAction"
    
    params = {
        "partNo": 86,
        "stateCd": "S25",
        "acNo": 260,
        "pageNumber": 1,
        "pageLimit": 100,
        "isTotalCount": "Y"
    }
    
    headers = {
        "Host": "gateway-officials.eci.gov.in",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "applicationName": "ERONET2.0",
        "PLATFORM-TYPE": "ECIWEB",
        "Authorization": f"Bearer {bearer_token}",
        "currentRole": "aero",
        "state": "S25",
        "appName": "ERONET2.0",
        "channelidobo": "ERONET",
        "Origin": "https://officials.eci.gov.in",
        "DNT": "1"
    }
    
    print(f"📅 Starting data fetch at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Optional: Configure proxy if needed
    proxies = {}
    http_proxy = os.getenv('HTTP_PROXY')
    https_proxy = os.getenv('HTTPS_PROXY')
    
    if http_proxy or https_proxy:
        proxies = {
            'http': http_proxy,
            'https': https_proxy
        }
        print(f"🔌 Using proxy: {proxies}")
    
    try:
        # Increased timeout and added retries
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=60,  # Increased timeout
            proxies=proxies if proxies else None,
            verify=True  # SSL verification
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API Request Successful!")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"schedule_data_{timestamp}.json"
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"💾 Data saved to: {filename}")
            
            # Basic response analysis
            if isinstance(data, dict):
                print(f"📊 Response keys: {list(data.keys())}")
                total_count = data.get('totalCount', data.get('total', 'N/A'))
                print(f"📈 Total count: {total_count}")
            
            return data
            
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text[:200]}")
            return None
            
    except requests.exceptions.Timeout:
        print("❌ Request timeout. The server is taking too long to respond.")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Connection error: {e}")
        print("This often means the API is blocking GitHub's IP addresses.")
        print("Try: 1) Self-hosted runner, or 2) Different network/VPN")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}: {e}")
        return None

def main():
    print("=" * 60)
    print("ECI Schedule Hearing API Fetcher")
    print("=" * 60)
    
    # Debug: Check if we can resolve the domain
    import socket
    try:
        socket.gethostbyname('gateway-officials.eci.gov.in')
        print("✅ Domain resolves successfully")
    except socket.gaierror:
        print("❌ Cannot resolve domain name")
    
    data = fetch_schedule_hearing_data()
    
    if data:
        print("\n✅ Data fetch completed successfully!")
    else:
        print("\n❌ Data fetch failed. Possible solutions:")
        print("   1. Use a self-hosted GitHub runner")
        print("   2. Check if API is accessible from your location")
        print("   3. Verify the bearer token is still valid")
        print("   4. Try with VPN/proxy if geographically restricted")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
