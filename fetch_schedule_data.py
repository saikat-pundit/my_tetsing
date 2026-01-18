import requests
import json

def fetch_schedule_hearing_data():
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
    
    # Headers - YOU NEED TO PASTE YOUR BEARER TOKEN HERE
    headers = {
        "Host": "gateway-officials.eci.gov.in",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "applicationName": "ERONET2.0",
        "PLATFORM-TYPE": "ECIWEB",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJDczJZLThBb3c2bEU4NW5xMnJuRE94bVpWTkRxYmpHUE5wLVNGdzQ3RjdzIn0.eyJleHAiOjE3Njg3ODA1MjIsImlhdCI6MTc2ODczNzMyMiwianRpIjoiNDAyNGY1ODUtNjliNi00MGNhLWFlNGUtNmI5NjQ5YTI4N2VkIiwiaXNzIjoiaHR0cDovLzEwLjIxMC4xMTMuMjE6ODA4MC9yZWFsbXMvZWNpLXByb2QtcmVhbG0iLCJhdWQiOlsicmVhbG0tbWFuYWdlbWVudCIsImFjY291bnQiXSwic3ViIjoiODhhNTQ1YzYtYzg1OS00MjVmLTk1ZjItYjhhNzE0NTQ1MGIxIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYXV0aG4tY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6IjJjYzhjZmY1LWY4MWYtNDNkYS1iNDgwLTU2MGJjMjdhOGM4OSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiYWVybyIsImRlZmF1bHQtcm9sZXMtZWNpLXByb2QtcmVhbG0iXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbImltcGVyc29uYXRpb24iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6IjJjYzhjZmY1LWY4MWYtNDNkYS1iNDgwLTU2MGJjMjdhOGM4OSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiYXV0aG9yaXplZFN0YXRlcyI6WyJTMjUiXSwicm9sZUlkIjo5LCJhdXRob3JpemVkRGlzdHJpY3RzIjpbIlMyNTIwIl0sImVtYWlsSWQiOiJzYWRhcnVyYWJhbjFjaXJjbGVAZ21haWwuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiZmJhOTFlNzktOTdmNS00MTM5LTk5MWMtMmNhMGZlNDA4MDgyIiwiYXV0aG9yaXplZEFjcyI6WzI2MF0sImdpdmVuX25hbWUiOiJTYXRhYmRpIiwibG9naW5OYW1lIjoiQUVST1MyNUEyNjBOMjAiLCJuYW1lIjoiU2F0YWJkaSBEdXR0YSIsInBob25lX251bWJlciI6IjkxNjM0OTE2NjUiLCJmYW1pbHlfbmFtZSI6IkR1dHRhIiwiYXV0aG9yaXplZFBhcnRzIjpbMTY3LDg3LDcsMjA5LDksODYsMjE2LDIxNCwyMTcsMTYzLDg5LDE2NiwxMTksMjA2LDg4LDE2NCwxNjUsMjEwLDEwLDIxMiwyMTEsMTIwLDE2MCwyMTMsMTYyLDEyMywyMDcsMjE1LDE2OCwxNjEsMjA4LDgsMTIxXX0.dN602ZRHYHMjFjFBjh2nRt6YCa8jwppjlpavK_gyXmF0s5nkU71-EX06Z6JAFdWkL_jUUphJ_VqvQy0geHQdYdZLAjdT_L64BiDf4wTm1bTOL2AdbgilQB4a8DG4DJOWEVj9NC9JJIl5NG4CZ2q3bGUicKueexJm5n61uBw-XDxcZkg1gdpBkvUWtl2ruIL8soECk_SixJ1CPIUqHhhM-TcbHrzMHmNcnLgs3MptU9LB45DuHlmpDeOPQD_SHY2L4S9fiPZvmkAOcxMhaRVZyH3M7MHTKyi_fDG4sSPgGEr2lvOn4jjimAR6W-_3XKM3yiAhjHnTXGtkzIk0gi1yUg",  # REPLACE WITH YOUR TOKEN
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
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            
            # Print the response in a readable format
            print("API Request Successful!")
            print(f"Status Code: {response.status_code}")
            print("\nResponse Data:")
            print(json.dumps(data, indent=2))
            
            # You can also save to a file
            with open('schedule_hearing_data.json', 'w') as f:
                json.dump(data, f, indent=2)
            print("\nData has been saved to 'schedule_hearing_data.json'")
            
            return data
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON response: {e}")
        print(f"Raw response: {response.text}")
        return None

if __name__ == "__main__":
    # Instructions for the user
    print("=" * 60)
    print("ECI Schedule Hearing API Fetcher")
    print("=" * 60)
    print("\nIMPORTANT: You need to paste your bearer token in the script.")
    print("1. Open the script in a text editor")
    print("2. Find the line: 'Authorization': 'Bearer YOUR_BEARER_TOKEN_HERE'")
    print("3. Replace 'YOUR_BEARER_TOKEN_HERE' with your actual bearer token")
    print("4. Save the file and run it again")
    print("=" * 60)
    
    # Check if token is still the placeholder
    import inspect
    source = inspect.getsource(fetch_schedule_hearing_data)
    if "YOUR_BEARER_TOKEN_HERE" in source:
        print("\n✗ Token not updated yet. Please update the bearer token as instructed above.")
    else:
        print("\n✓ Fetching data...")
        fetch_schedule_hearing_data()
