from akavesdk.client import AkaveClient  # Adjust path if needed
from akavesdk.client import AkaveClient

client = AkaveClient()
client.connect()  # Test the connect method
client.upload_file("example.txt")  # Test uploading a file
client.download_file("example.txt")  # Test downloading a file

def main():
    client = AkaveClient(
        private_key="your-private-key",
        node_address="connect.akave.ai:5500"
    )

    # Example usage (list buckets)
    buckets = client.list_buckets()
    print("Buckets:", buckets)

if __name__ == "__main__":
    main()
