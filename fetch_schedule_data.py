import os
import requests
import json
from datetime import datetime

def fetch_schedule_hearing_data():
    """
    Fetch schedule hearing data from ECI API
    """
    # Get bearer token from environment variable (GitHub Secret)
    bearer_token = os.getenv('BEARER_TOKEN')
    
    if not bearer_token:
        print("❌ Error: BEARER_TOKEN environment variable not set")
        print("   For GitHub Actions: Add BEARER_TOKEN as a GitHub Secret")
        print("   For local testing: export BEARER_TOKEN='your_token_here'")
        return None
    
    # API URL
    url = "https://gateway-officials.eci.gov.in/api/v1/s25/scheduleHearing/getSchedulingAction"
    
    # Query parameters
    params = {
        "partNo": 86,
        "stateCd": "S25",
        "acNo": 260,
        "pageNumber": 1,
        "pageLimit": 100,
        "isTotalCount": "Y"
    }
    
    # Headers
    headers = {
        "Host": "gateway-officials.eci.gov.in",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "applicationName": "ERONET2.0",
        "PLATFORM-TYPE": "ECIWEB",
        "Authorization": f"Bearer {bearer_token}",  # Use token from environment
        "currentRole": "aero",
        "state": "S25",
        "appName": "ERONET2.0",
        "atkn_bnd": "05fvv70Ia1fvv73vv70XJe+/vSkm77+9Xu+/ve+/vQnvv706Fe+/ve+/ve+/vR3vv717Xe+/vTg777+9",
        "rtkn_bnd": "77+977+977+9AyZlNe+/ve+/vV81SO+/vR7vv73vv73vv73vv71K77+977+9ThdE77+977+977+9WmwiV10=",
        "channelidobo": "ERONET",
        "Origin": "https://officials.eci.gov.in",
        "DNT": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=0"
    }
    
    print(f"📅 Starting data fetch at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔗 API URL: {url}")
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, params=params, timeout=30)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            
            print("✅ API Request Successful!")
            print(f"📊 Status Code: {response.status_code}")
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"schedule_data_{timestamp}.json"
            
            # Save to file
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"💾 Data saved to: {filename}")
            
            # Print summary if available
            if isinstance(data, dict):
                print("\n📋 Response Summary:")
                for key, value in data.items():
                    if isinstance(value, (str, int, float, bool)):
                        print(f"   {key}: {value}")
                    elif isinstance(value, list):
                        print(f"   {key}: List with {len(value)} items")
                    elif isinstance(value, dict):
                        print(f"   {key}: Dictionary with {len(value)} keys")
            
            return data
            
        else:
            print(f"❌ Request failed with status code: {response.status_code}")
            print(f"Response: {response.text[:500]}...")  # Show first 500 chars
            
            # Save error response for debugging
            error_filename = f"error_response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            try:
                error_data = response.json()
                with open(error_filename, 'w') as f:
                    json.dump(error_data, f, indent=2)
                print(f"💾 Error response saved to: {error_filename}")
            except:
                with open(error_filename, 'w') as f:
                    f.write(response.text)
                print(f"💾 Error response saved to: {error_filename}")
            
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network/Request error occurred: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON response: {e}")
        print(f"Raw response (first 1000 chars): {response.text[:1000]}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def main():
    """Main function"""
    print("=" * 60)
    print("ECI Schedule Hearing API Fetcher")
    print("=" * 60)
    
    data = fetch_schedule_hearing_data()
    
    if data:
        print("\n✅ Data fetch completed successfully!")
    else:
        print("\n❌ Data fetch failed. Check the errors above.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
