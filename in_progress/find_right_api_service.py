#!/usr/bin/env python3
"""
Simple CLI tool to browse APIs.guru directory and download API specs.
"""

import json
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


BASE_URL = "https://api.apis.guru/v2"


def fetch_json(url):
    """Fetch JSON data from a URL."""
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)


def fetch_yaml(url):
    """Fetch YAML data from a URL."""
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as response:
            return response.read().decode('utf-8')
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except URLError as e:
        print(f"URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching YAML: {e}", file=sys.stderr)
        sys.exit(1)


def list_all_apis():
    """Fetch and return all APIs from the directory."""
    print("Fetching API list from APIs.guru...\n")
    url = f"{BASE_URL}/list.json"
    return fetch_json(url)


def display_apis(apis_data):
    """Display all available APIs in a numbered list."""
    # Convert APIs dict to a sorted list for easier selection
    api_list = []
    
    for api_id, api_info in sorted(apis_data.items()):
        # Get the preferred version info
        preferred_version = api_info.get('preferred')
        if preferred_version and 'versions' in api_info:
            version_info = api_info['versions'].get(preferred_version, {})
            title = version_info.get('info', {}).get('title', api_id)
            description = version_info.get('info', {}).get('description', 'No description')
            # Truncate long descriptions
            if len(description) > 80:
                description = description[:77] + '...'
        else:
            title = api_id
            description = 'No description'
        
        api_list.append({
            'id': api_id,
            'title': title,
            'description': description,
            'info': api_info
        })
    
    print(f"Found {len(api_list)} APIs:\n")
    print("-" * 80)
    
    for idx, api in enumerate(api_list, 1):
        print(f"{idx}. {api['title']}")
        print(f"   ID: {api['id']}")
        print(f"   {api['description']}")
        print("-" * 80)
    
    return api_list


def get_user_selection(api_list):
    """Prompt user to select an API."""
    while True:
        try:
            print(f"\nEnter a number (1-{len(api_list)}) to select an API, or 'q' to quit: ", end='')
            choice = input().strip()
            
            if choice.lower() == 'q':
                print("Goodbye!")
                sys.exit(0)
            
            selection = int(choice)
            if 1 <= selection <= len(api_list):
                return api_list[selection - 1]
            else:
                print(f"Please enter a number between 1 and {len(api_list)}")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def get_yaml_spec(api_info):
    """Get the YAML spec URL for the selected API."""
    preferred_version = api_info['info'].get('preferred')
    if not preferred_version or 'versions' not in api_info['info']:
        print("Error: Could not find version information for this API", file=sys.stderr)
        return None
    
    version_info = api_info['info']['versions'].get(preferred_version)
    if not version_info:
        print(f"Error: Could not find info for version {preferred_version}", file=sys.stderr)
        return None
    
    yaml_url = version_info.get('swaggerYamlUrl')
    if not yaml_url:
        print("Error: No YAML URL found for this API", file=sys.stderr)
        return None
    
    return yaml_url


def main():
    """Main CLI function."""
    print("=" * 80)
    print("APIs.guru API Browser")
    print("=" * 80)
    print()
    
    # Fetch all APIs
    apis_data = list_all_apis()
    
    # Display APIs and get list
    api_list = display_apis(apis_data)
    
    # Get user selection
    selected_api = get_user_selection(api_list)
    
    print(f"\nYou selected: {selected_api['title']}")
    print(f"API ID: {selected_api['id']}")
    
    # Get YAML spec URL
    yaml_url = get_yaml_spec(selected_api)
    
    if not yaml_url:
        sys.exit(1)
    
    print(f"\nFetching YAML spec from: {yaml_url}")
    print()
    
    # Fetch and display YAML
    yaml_content = fetch_yaml(yaml_url)
    
    print("=" * 80)
    print("YAML SPECIFICATION:")
    print("=" * 80)
    print(yaml_content)
    
    # Ask if user wants to save to file
    print("\n" + "=" * 80)
    print(f"\nWould you like to save this to a file? (y/n): ", end='')
    try:
        save_choice = input().strip().lower()
        if save_choice == 'y':
            # Generate filename from API ID
            filename = selected_api['id'].replace(':', '-').replace('/', '-') + '.yaml'
            with open(filename, 'w') as f:
                f.write(yaml_content)
            print(f"✓ Saved to: {filename}")
    except KeyboardInterrupt:
        print("\nSkipping save.")


if __name__ == "__main__":
    main()

