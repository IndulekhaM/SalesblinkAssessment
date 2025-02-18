# Selenium Automation Script for Google Search and Login

This Python script uses **Selenium** to automate the following tasks:

1. Open Google and search for "SalesBlink.io".
2. Wait for the user to manually solve the CAPTCHA (if prompted).
3. Click the first result.
4. Navigate to the SalesBlink.io login page.
5. Enter credentials and log in.

## Prerequisites

Before running this script, ensure you have the following installed:

- **Python** (3.6 or above)
- **Google Chrome** (or any other browser you wish to automate)
- **ChromeDriver** (for Chrome automation) - make sure it matches your Chrome version
- **Selenium** library installed

### Install Selenium

If you haven't installed Selenium, you can do so via pip:

```bash
pip install selenium
```

### Install WebDriver

Make sure to download the appropriate [ChromeDriver](https://sites.google.com/chromium.org/driver/) for your version of Google Chrome and ensure it's accessible in your system's PATH, or specify the path to the ChromeDriver executable in your script.

## How to Run the Script

1. **Clone the repository** (if this code is part of one):
    ```bash
    git clone https://github.com/your-repo-name.git
    ```

2. **Navigate to the directory** where your script is located:
    ```bash
    cd path/to/your/repository
    ```

3. **Update your credentials**: 
    Replace the `EMAIL_ID` and `PASSWORD` variables in the script with your own login credentials for SalesBlink.io.

    ```python
    EMAIL_ID = 'your-email@example.com'
    PASSWORD = 'your-password'
    ```

4. **Run the script**:
    ```bash
    python path/to/your/script.py
    ```

## Script Details

1. The script will open Google and search for "SalesBlink.io".
2. It will then wait for the CAPTCHA challenge to be solved manually. You will need to verify you're not a robot by solving the CAPTCHA and selecting images (if prompted).
3. Once the CAPTCHA is completed, the script will click on the first search result.
4. The script will then navigate to the SalesBlink.io login page.
5. It will enter your email and password automatically and click the login button.
