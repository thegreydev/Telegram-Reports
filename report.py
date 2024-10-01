import pyautogui
import time

# Coordinates for reporting actions (update these based on your screen)
report_button_x, report_button_y = 1000, 500  # Replace with coordinates of the 'Report' button
confirm_report_x, confirm_report_y = 1050, 600  # Replace with coordinates of 'Confirm' button

def report_telegram_url():
    # Move to the report button and click it
    pyautogui.moveTo(report_button_x, report_button_y)
    pyautogui.click()
    time.sleep(1)  # Wait for report window to open

    # Move to the confirm report button and click it
    pyautogui.moveTo(confirm_report_x, confirm_report_y)
    pyautogui.click()
    time.sleep(2)  # Wait for the report action to complete

# Loop the report 1000 times
for i in range(1000):
    report_telegram_url()
    print(f"Report {i+1} submitted")
    time.sleep(1)  # Adjust the sleep time to avoid detection

print("All reports submitted.")
