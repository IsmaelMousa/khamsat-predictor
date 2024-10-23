import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
import pandas as pd

def scrap(driver, category_name, category_url):
    data = []
    visited_services = set()
    max_offers = 2

    try:
        driver.get(category_url)
        wait = WebDriverWait(driver, timeout=10)

        print(f"Category Name: {category_name}")
        print(f"Category URL: {category_url}")

        services = driver.find_elements(by=By.CSS_SELECTOR, value=".grid-items a.lh-lg")

        service_collected = 0
        while service_collected < len(services):
            service = services[service_collected]
            service_name = service.text.strip()
            service_url = service.get_attribute("href")

            print(f"Service Name: {service_name}")
            print(f"Service URL: {service_url}")

            if service_name in visited_services:
                service_collected += 1
                continue

            visited_services.add(service_name)

            driver.get(service_url)

            offers_collected = 0
            offers_set = set()

            while offers_collected < max_offers:
                try:
                    offers = driver.find_elements(by=By.CSS_SELECTOR, value=".product-title a")

                    for offer in offers:
                        offer_url = offer.get_attribute("href")

                        if offer_url in offers_set:
                            continue

                        offers_set.add(offer_url)

                        offer_name = offer.text.strip()

                        print(f"Offer Name: {offer_name}")
                        print(f"Offer URL: {offer_url}")

                        driver.get(offer_url)

                        try:
                            offer_rating_elements = wait.until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.c-list--rating"))
                            ).find_elements(by=By.CSS_SELECTOR, value="li.c-list__item i")
                            offer_stars = 0.0

                            for star in offer_rating_elements:
                                star_class = star.get_attribute("class")

                                if "fa-star-half-o" in star_class:
                                    offer_stars += 0.5
                                elif "fa-star" in star_class and "fa-star-o" not in star_class:
                                    offer_stars += 1

                        except (NoSuchElementException, TimeoutException):
                            offer_stars = None

                        offer_raters = driver.find_element(by=By.CSS_SELECTOR, value=".c-list__item.info").text.strip("()")
                        offer_response_time_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".card-body .col-6 span")
                        offer_response_time = offer_response_time_elements[2].text.strip()
                        offer_buyers = offer_response_time_elements[4].text.strip()
                        pending = offer_response_time_elements[6].text.strip()
                        price = offer_response_time_elements[8].text.strip()
                        duration = offer_response_time_elements[10].text.strip()

                        print(f"Offer Stars: {offer_stars}")
                        print(f"Offer Raters: {offer_raters}")
                        print(f"Offer Response Time: {offer_response_time}")
                        print(f"Offer Buyers: {offer_buyers}")
                        print(f"Pending: {pending}")
                        print(f"Price: {price}")
                        print(f"Duration: {duration}")

                        try:
                            reviews = len(driver.find_element(by=By.ID, value="reviews-section").find_elements(by=By.CSS_SELECTOR, value=".review_section"))

                        except NoSuchElementException:
                            reviews = 0

                        available_additions = len(driver.find_elements(by=By.CSS_SELECTOR, value="table#service_upgrades_table tbody tr"))
                        additions_price = sum(float(addition.find_element(by=By.CSS_SELECTOR, value=".service_upgrade_price").get_attribute("data-price")) for addition in driver.find_elements(by=By.CSS_SELECTOR, value="table#service_upgrades_table tbody tr"))
                        owner_name = driver.find_element(by=By.CSS_SELECTOR, value="h3 a.sidebar_user").text.strip()
                        verified_element = driver.find_elements(by=By.CSS_SELECTOR, value="img.verification-badge")
                        owner_verified = True if verified_element else False
                        owner_level = driver.find_element(by=By.CSS_SELECTOR, value="ul.details-list li").text.strip()
                        owner_url = driver.find_element(by=By.CSS_SELECTOR, value="h3 a.sidebar_user").get_attribute("href")

                        print(f"Reviews: {reviews}")
                        print(f"Available Additions: {available_additions}")
                        print(f"Additions Price: {additions_price}")
                        print(f"Owner Name: {owner_name}")
                        print(f"Owner Verified: {owner_verified}")
                        print(f"Owner Level: {owner_level}")
                        print(f"Owner URL: {owner_url}")

                        driver.get(owner_url)

                        owner_stars_elements = driver.find_element(by=By.CSS_SELECTOR, value="ul.c-list--rating").find_elements(by=By.CSS_SELECTOR, value="li.c-list__item i")
                        owner_stars = 0.0

                        for star in owner_stars_elements:
                            star_class = star.get_attribute("class")

                            if "fa-star-half-o" in star_class:
                                owner_stars += 0.5

                            elif "fa-star" in star_class and "fa-star-o" not in star_class:
                                owner_stars += 1

                        owner_statistics = driver.find_element(by=By.CSS_SELECTOR, value=".card-body #sidebar")
                        owner_raters = owner_statistics.find_element(by=By.CSS_SELECTOR, value=".c-list__item.info").text.strip("()")
                        owner_completion_rate = owner_statistics.find_elements(by=By.CSS_SELECTOR, value=".list.col-6 span")[2].text.strip()
                        owner_services = owner_statistics.find_elements(by=By.CSS_SELECTOR, value=".list.col-6 span")[4].find_element(by=By.TAG_NAME, value="a").text.strip() if owner_statistics.find_elements(by=By.CSS_SELECTOR, value=".list.col-6 span")[4].find_elements(by=By.TAG_NAME, value="a") else "0"
                        owner_customers = owner_statistics.find_elements(by=By.CSS_SELECTOR, value=".list.col-6 span")[6].text.strip()
                        owner_response_time = owner_statistics.find_elements(by=By.CSS_SELECTOR, value=".list.col-6")[9].text.strip()

                        print(f"Owner Stars: {owner_stars}")
                        print(f"Owner Raters: {owner_raters}")
                        print(f"Owner Completion Rate: {owner_completion_rate}")
                        print(f"Owner Services: {owner_services}")
                        print(f"Owner Customers: {owner_customers}")
                        print(f"Owner Response Time: {owner_response_time}")

                        data.append({"Category Name": category_name,
                                     "Category URL": category_url,
                                     "Service Name": service_name,
                                     "Service URL": service_url,
                                     "Offer Name": offer_name,
                                     "Offer URL": offer_url,
                                     "Offer Stars": offer_stars,
                                     "Offer Raters": offer_raters,
                                     "Offer Response Time": offer_response_time,
                                     "Offer Buyers": offer_buyers,
                                     "Pending": pending,
                                     "Price": price,
                                     "Duration": duration,
                                     "Reviews": reviews,
                                     "Available Additions": available_additions,
                                     "Additions Price": additions_price,
                                     "Owner Name": owner_name,
                                     "Owner URL": owner_url,
                                     "Owner Verified": owner_verified,
                                     "Owner Level": owner_level,
                                     "Owner Stars": owner_stars,
                                     "Owner Raters": owner_raters,
                                     "Owner Completion Rate": owner_completion_rate,
                                     "Owner Services": owner_services,
                                     "Owner Customers": owner_customers,
                                     "Owner Response Time": owner_response_time})

                        offers_collected += 1

                        driver.back()
                        time.sleep(1)

                        driver.back()
                        time.sleep(1)

                        if offers_collected % 30 == 0:
                            print(f"{offers_collected} Offers of {service_name} Collected!")
                            print("عرض المزيد")

                        if offers_collected >= max_offers:
                            break

                except StaleElementReferenceException:
                    driver.refresh()
                    time.sleep(2)

            services_dir = os.path.join("khamsat", category_name)
            os.makedirs(services_dir, exist_ok=True)
            service_file = os.path.join(services_dir, f"{service_collected + 1}_of_services.csv")

            pd.DataFrame(data).to_csv(path_or_buf=service_file, index=False)
            print(f"Service: {service_name} Completed!")

            service_collected += 1
            driver.get(category_url)
            services = driver.find_elements(by=By.CSS_SELECTOR, value=".grid-items a.lh-lg")

        category_dir = os.path.join("khamsat", "categories")
        os.makedirs(category_dir, exist_ok=True)
        category_file = os.path.join(category_dir, f"{category_name}.csv")

        pd.DataFrame(data).to_csv(path_or_buf=category_file, index=False)
        print(f"Category: {category_name} Completed!")

    except Exception as e:
        print(f"Error: {e}")

categories_meta = {"تصميم": "https://khamsat.com/designing",
                   "كتابة وترجمة": "https://khamsat.com/writing",
                   "تسويق رقمي": "https://khamsat.com/marketing",
                   "برمجة وتطوير": "https://khamsat.com/programming",
                   "فيديو وأنيميشن": "https://khamsat.com/video-design",
                   "هندسة وعمارة": "https://khamsat.com/engineering",
                   "أعمال": "https://khamsat.com/business",
                   "صوتيات": "https://khamsat.com/audio",
                   "تعليم عن بعد": "https://khamsat.com/training",
                   "بيانات": "https://khamsat.com/data",
                   "أسلوب حياة": "https://khamsat.com/lifestyle"}

chrome = Chrome()
scrap(driver=chrome, category_name="صوتيات", category_url="https://khamsat.com/audio")
chrome.quit()