#import webbrowser
from cloudflare_error_page import render as render_cf_error_page

# This function renders an error page based on the input parameters
error_page = render_cf_error_page({
    "html_title": "网页找不到了喵",
    "title": "The Myth Of \"Consensual\" Internet",
    "error_code": "lmao",
    "time": "",  # Current UTC time will be shown if empty

    # Configuration of "Visit ... for more information"
    "more_information": {
        "hidden": False,
        "text": "Home Page", 
        "link": "/",
        "for": "going back to the home page",
    },

    # Configuration of the Browser/Cloudflare/Host status block
    "browser_status": {
        "status": "ok", # "ok" or "error"
        "location": "You",
        "name": "Browser",
        "status_text": "I Consent",
        "status_text_color": "#9bca3e",
    },
    "cloudflare_status": {
        "status": "error",
        "location": "Wherever",
        "name": "Cloudflare",
        "status_text": "I Don't!",
        "status_text_color": "#bd2426",
    },
    "host_status": {
        "status": "ok",
        "location": "Remote",
        "name": "Host",
        "status_text": "I Consent",
        "status_text_color": "#9bca3e",
    },
    # Position of the error indicator, valid options are 'browser', 'cloudflare', and 'host'
    "error_source": "cloudflare",

    "what_happened": "<p>Nothing happened.</p>",
    "what_can_i_do": "<p>Go back to the <a href=\"javascript:history.back()\">previous page</a>, or go back to the <a href=\"/\">home page</a>.</p>",

    "ray_id": '1145141919810114',  # Random hex string will be shown if empty
    "client_ip": '1.1.1.1',

    # Configuration of 'Performance & security by ...' in the footer
    "perf_sec_by": {
        "text": "Cloudflare",
        "link": "https://www.cloudflare.com/",
    },
})

# Write generated webpage to file
with open('404.astro', 'w') as f:
    f.write(error_page)

# Open the generated page in browser
#webbrowser.open('error.html')