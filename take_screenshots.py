import os
import time
from playwright.sync_api import sync_playwright

OUTPUT_DIRS = [
    r"C:\Users\MY\.gemini\antigravity-ide\scratch\django-onlinecourse-assessment-system",
    r"C:\Users\MY\.gemini\antigravity-ide\brain\f8c5e049-0a7d-474d-9d64-8ba5d0a1f9a0",
    r"C:\Users\MY\.gemini\antigravity-ide\scratch"
]

for d in OUTPUT_DIRS:
    os.makedirs(d, exist_ok=True)

def capture():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2)
        page = context.new_page()

        # --- TASK 3: Admin Site Screenshot ---
        print("Navigating to Django admin login...")
        page.goto('http://127.0.0.1:8000/admin/login/?next=/admin/')
        page.wait_for_load_state('networkidle')
        
        # Fill credentials
        page.fill('input[name="username"]', 'admin')
        page.fill('input[name="password"]', 'admin12345')
        page.click('input[type="submit"]')
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        print("Capturing 03-admin-site...")
        admin_path = os.path.join(OUTPUT_DIRS[0], "03-admin-site.png")
        page.screenshot(path=admin_path, full_page=False)
        for d in OUTPUT_DIRS[1:]:
            page.screenshot(path=os.path.join(d, "03-admin-site.png"), full_page=False)
        print("03-admin-site.png saved successfully!")

        # --- TASK 7: Mock Exam Result Screenshot ---
        print("Navigating to user login...")
        page.goto('http://127.0.0.1:8000/onlinecourse/login/')
        page.wait_for_load_state('networkidle')

        # Fill credentials for student
        page.fill('input[name="username"]', 'student')
        page.fill('input[name="psw"]', 'password123')
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        # Navigate to submission result
        print("Navigating to exam result...")
        page.goto('http://127.0.0.1:8000/onlinecourse/1/submission/1/result/')
        page.wait_for_load_state('networkidle')
        time.sleep(1)

        print("Capturing 07-final...")
        final_path = os.path.join(OUTPUT_DIRS[0], "07-final.png")
        page.screenshot(path=final_path, full_page=False)
        for d in OUTPUT_DIRS[1:]:
            page.screenshot(path=os.path.join(d, "07-final.png"), full_page=False)
        print("07-final.png saved successfully!")

        browser.close()

if __name__ == '__main__':
    capture()
