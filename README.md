# Feature Flag Project
### LaunchDarkly

This project emulates a shipping API, where Fedex, 
USPS, and UPS rates can be turned turned on or off. 
The implementation uses a Python app and runs a 
small web app to display values.

## Setup

1. In LaunchDarkly, create the following feature flags:
  * `shipQuoteFedex`
  * `shipQuoteUSPS`
  * `shipQuoteUPS`

2. Clone this repo and navigate to its directory in a terminal

3. From the terminal, run: `pip install -r requirements.txt`

4. Next, run: `mv app.ini.example app.ini`

5. Open the `app.ini` file and replace the fake SDK key with your SDK key
```
[App]
SDKKey=YOUR_KEY_HERE
```

6. From the terminal, run: `python app.py`

7. In your browser, navigate to http://127.0.0.1:5000

8. Toggle feature flags in LaunchDarkly and refresh the browser to view various shipping rates

Enjoy!
