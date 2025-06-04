from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Selenium
driver = webdriver.Chrome()

# Go to Infosys Springboard (auto-login is optional, or log in manually)
driver.get("https://infyspringboard.onwingspan.com/web/en/viewer/video/lex_auth_01384359147969740842319_shared?collectionId=lex_auth_01384359096053760041392_shared&collectionType=Course&pathId=lex_auth_01384358840773836841382_shared")

input("Login manually and press Enter once you're on the video page...")

# Wait for video player to load
time.sleep(5)

# Inject JS to seek video to near the end
seek_script = """
var video = document.querySelector('video');
if (video) {
    video.currentTime = video.duration - 5;
    video.muted = true;
    video.play();
}
"""
driver.execute_script(seek_script)

print("Fast-forwarded video. Waiting for it to play a few seconds...")

# Wait for video to finish playing (adjust if needed)
time.sleep(10)

# Click the "Next" button (right arrow inside the turquoise circle)
try:
    next_button = driver.find_element(By.XPATH, "//div[contains(@class, 'vjs-next-button') or contains(@class, 'icon-right-arrow') or contains(@aria-label, 'Next')]")
    next_button.click()
    print("Clicked Next button.")
except Exception as e:
    print("Couldn't find or click next button:", e)

# You can wrap this in a loop for multiple videos

# Done
driver.quit()
