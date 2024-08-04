import os
from datetime import datetime
from dotenv import load_dotenv
from utils import Search

load_dotenv()


if __name__ == "__main__":
    subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
    bing = Search.Bing(subscription_key)
    
    if not os.path.isdir("Scans"):
        os.mkdir("Scans")
    

    output_location = f"Scans/{datetime.now().strftime('%m-%d_%H-%M')}.txt"

    bing.scan("nvidia", output_location)

    
