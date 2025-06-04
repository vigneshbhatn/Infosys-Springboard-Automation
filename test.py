from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
options = Options()
options.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=options)

# Start from first video page if needed
driver.get("https://infyspringboard.onwingspan.com/web/en/viewer/video/lex_auth_01320401403424768058_shared?collectionType=Course&collectionId=lex_auth_01320399563070668844_shared&pathId=lex_auth_01320400494635417653_shared")

while True:
    try:
        # Wait for video to load
        time.sleep(5)

        # Step 1: Click play
        try:
            play_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "vjs-big-play-button"))
            )
            play_button.click()
            print("▶️ Play clicked")
        except Exception as e:
            print("⚠️ Play button not found, maybe already playing:", e)

        # Step 2: Fast-forward
        time.sleep(3)
        driver.execute_script("""
            var video = document.querySelector('video');
            if (video) {
                video.currentTime = video.duration - 2;
            }
        """)
        print("⏩ Skipped to end")

        # Step 3: Wait for video to "complete"
        time.sleep(5)

        # Step 4: Click Next
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="next content"]'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            next_button.click()
            print("✅ Moved to next video")
        except Exception as e:
            print("❌ No more 'Next' button or couldn't click it:", e)
            print("🎉 Course might be complete or last video reached.")
            break

    except Exception as e:
        print("💥 Unexpected error:", e)
        break

print("🚀 All videos done!")
