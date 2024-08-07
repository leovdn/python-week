import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Insert the stock ticker: ")
stock_data = yfinance.Ticker(ticker).history(start="2022-01-01", end="2022-12-31")

year_end_close = stock_data.Close
year_end_close.plot()

max_quotation = round(year_end_close.max(), 2)
min_quotation = round(year_end_close.min(), 2)
average_quotation = round(year_end_close.mean(), 2)

recipient = "leo.vdn@gmail.com"
subject = "Python Automatization Practice"
message = f"""
Dear manager,

We have received your request to get the {ticker} stock quotation:

Max: R$ {max_quotation}
Min: R$ {min_quotation}
Average: R$ {average_quotation}

Any doubts, please contact us!

Best regards,

The Leovdn Automatization Team

"""

# Open Browser
webbrowser.open("https://mail.google.com")
time.sleep(3)

# Pausing for 3 seconds before click
pyautogui.PAUSE = 3

# Click on Write button
pyautogui.click(x=1319, y=-921)

# Type recipient's email address
pyperclip.copy(recipient)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Type the e-mail subject
pyperclip.copy(subject)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Type the e-mail message
pyperclip.copy(message)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Send e-mail
pyautogui.click(x=1738, y=-103)

print("E-mail sent successfully!")