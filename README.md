# Asynchronous Browser Manager

This is a Python script that allows you to launch multiple browsers asynchronously, each with its own configuration, using the `nodriver` library. The script randomly selects user agents and proxies, opens specified links in separate browser instances, and sets their window size and position.

## Features

- Launch multiple browser instances asynchronously.
- Use different user agents and proxy settings for each browser.
- Navigate to random links from a provided list.
- Option to run browsers in headless mode.
- Dynamically manage browser windows by setting their size and position.

## Requirements

- Python 3.7 or higher
- `nodriver` library

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Connor9994/Proxy-View-Bot
   cd Proxy-View-Bot
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the necessary files:**
   - Create a file named `proxies_datacenter.txt` and populate it with your proxy addresses (one per line).
   - Create a file named `useragents.txt` and populate it with your desired user agent strings (one per line).
   - Create a file named `links.txt` and add the URLs you want to open (one per line).

4. **Set your Chrome executable path:**
   Update the `browserPath` variable in the script to point to your own Chrome executable location if necessary.
   
   Note: We used a Chormium folder inside of the local directory. We had issues accessing Chrome directly in the Program Files folder.
   https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/

## Usage

To run the script, simply execute:

```bash
python "Proxy View Bot.py"
```

## Customization

You can customize the following parameters in the script:
- `number_of_browsers`: Adjust the number of browsers to be opened.
- `headless`: Set to `True` if you want to run the browsers in headless mode, or leave it as `False` to see the browser windows.

## Note

- Make sure to handle proxies responsibly and in compliance with the terms of service of the websites you are accessing.
- This script is intended for educational purposes and should be used ethically.

## Contributing

If you have suggestions for improvements or feature requests, please feel free to open an issue or submit a pull request.  

## Acknowledgments

- [nodriver](https://pypi.org/project/nodriver/) - The library used for controlling the browser instances.  
- Special thanks to the open-source community for their invaluable contributions!
