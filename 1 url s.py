import hashlib

# A dictionary to store the mapping of short URLs to long URLs
url_mapping = {}

# Function to generate a short URL
def generate_short_url(long_url):
    # Create an MD5 hash of the long URL
    hash_object = hashlib.md5(long_url.encode())
    # Use the first 6 characters of the hash as the short URL
    short_url = hash_object.hexdigest()[:6]
    
    # Store the mapping in the dictionary
    url_mapping[short_url] = long_url
    return short_url

# Function to retrieve the original long URL from the short URL
def get_long_url(short_url):
    # Look up the short URL in the dictionary
    return url_mapping.get(short_url, "URL not found!")

# Main program loop
def main():
    while True:
        print("\n--- URL Shortener ---")
        print("1. Shorten a URL")
        print("2. Retrieve original URL")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            long_url = input("Enter the long URL: ")
            short_url = generate_short_url(long_url)
            print(f"Short URL is: {short_url}")
        
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            long_url = get_long_url(short_url)
            print(f"Original URL is: {long_url}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()