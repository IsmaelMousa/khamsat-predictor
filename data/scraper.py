import os
import time

import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (StaleElementReferenceException,
                                        NoSuchElementException,
                                        TimeoutException)


def scrap(driver: Chrome, category_name: str, category_url: str) -> None:
    """
    Scrape all the available offers of the different services for a given category,
    and saving the scraped data in a csv file that named according to the category name.

    :param driver: The webdriver instance (Google Chrome)
    :param category_name: The name of the category to scrap
    :param category_url: The URL of the category to scrap
    :return: Printed message that tell us we are done
    """
    selector = By.CSS_SELECTOR
    data = []
    visited_services = set()

    try:
        driver.get(url=category_url)

        wait = WebDriverWait(driver=driver, timeout=10)

        services = driver.find_elements(by=selector, value=".grid-items a.lh-lg")

        service_collected = 0

        while service_collected < len(services):
            service = services[service_collected]

            service_name = service.text.strip()
            service_url = service.get_attribute(name="href")

            if service_name in visited_services:
                service_collected += 1
                continue

            visited_services.add(service_name)

            driver.get(url=service_url)

            offers_set = set()

            while True:
                try:
                    offers = driver.find_elements(by=selector, value=".product-title a")

                    new_offers_found = False

                    for offer in offers:
                        offer_url = offer.get_attribute(name="href")

                        if offer_url in offers_set:
                            continue

                        offers_set.add(offer_url)

                        new_offers_found = True

                        offer_name = offer.text.strip()

                        driver.get(url=offer_url)

                        try:
                            offer_rating_elements = wait.until(ec.presence_of_element_located(
                                (selector, "ul.c-list--rating"))).find_elements(by=selector, value="li.c-list__item i")

                            offer_stars = 0.0

                            for star in offer_rating_elements:
                                star_class = star.get_attribute("class")

                                if "fa-star-half-o" in star_class:
                                    offer_stars += 0.5

                                elif "fa-star" in star_class and "fa-star-o" not in star_class:
                                    offer_stars += 1

                            offer_raters = driver.find_element(by=selector,
                                                               value=".c-list__item.info").text.strip("()")

                            offer_response_time_elements = driver.find_elements(by=selector,
                                                                                value=".card-body .col-6 span")

                            offer_response_time = offer_response_time_elements[2].text.strip()

                            offer_buyers = offer_response_time_elements[4].text.strip()

                            pending = offer_response_time_elements[6].text.strip()

                            price = offer_response_time_elements[8].text.strip()

                            duration = offer_response_time_elements[10].text.strip()

                        except (NoSuchElementException, TimeoutException, IndexError):
                            driver.back()
                            continue

                        try:
                            reviews = len(driver.find_element(by=By.ID, value="reviews-section")
                                          .find_elements(by=selector, value=".review_section"))

                        except NoSuchElementException:
                            reviews = 0

                        available_additions = len(driver.find_elements(by=selector,
                                                                       value="table#service_upgrades_table tbody tr"))

                        additions_price = sum(float(addition.find_element(by=selector, value=".service_upgrade_price").
                                                    get_attribute("data-price")) for addition in driver.
                                              find_elements(by=selector, value="table#service_upgrades_table tbody tr"))

                        owner_name = driver.find_element(by=selector, value="h3 a.sidebar_user").text.strip()

                        verified_element = driver.find_elements(by=selector, value="img.verification-badge")

                        owner_verified = True if verified_element else False

                        owner_level = driver.find_element(by=selector, value="ul.details-list li").text.strip()

                        owner_url = driver.find_element(by=selector, value="h3 a.sidebar_user").get_attribute("href")

                        driver.get(url=owner_url)

                        owner_stars_elements = (driver.find_element(by=selector, value="ul.c-list--rating").
                                                find_elements(by=selector, value="li.c-list__item i"))
                        owner_stars = 0.0

                        for star in owner_stars_elements:
                            star_class = star.get_attribute("class")

                            if "fa-star-half-o" in star_class:
                                owner_stars += 0.5

                            elif "fa-star" in star_class and "fa-star-o" not in star_class:
                                owner_stars += 1

                        owner_statistics = driver.find_element(by=selector, value=".card-body #sidebar")

                        owner_raters = owner_statistics.find_element(by=selector,
                                                                     value=".c-list__item.info").text.strip("()")

                        owner_completion_rate = owner_statistics.find_elements(by=selector,
                                                                               value=".list.col-6 span")[2].text.strip()

                        owner_services = (owner_statistics.find_elements(by=selector, value=".list.col-6 span")[4].
                                          find_element(by=By.TAG_NAME, value="a").text.strip()) if (
                            owner_statistics.find_elements(by=selector, value=".list.col-6 span")[4].
                            find_elements(by=By.TAG_NAME, value="a")) else "0"

                        owner_customers = owner_statistics.find_elements(by=selector,
                                                                         value=".list.col-6 span")[6].text.strip()

                        owner_response_time = owner_statistics.find_elements(by=selector,
                                                                             value=".list.col-6")[9].text.strip()

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

                        driver.back()
                        time.sleep(1)

                        driver.back()
                        time.sleep(1)

                    if not new_offers_found:
                        break

                except StaleElementReferenceException:
                    driver.refresh()
                    time.sleep(2)

            service_collected += 1

            driver.get(url=category_url)

            services = driver.find_elements(by=selector, value=".grid-items a.lh-lg")

        category_dir = os.path.join("raw", "categories")

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

for category_name, category_url in categories_meta.items():
    scrap(driver=chrome, category_name=category_name, category_url=category_url)

chrome.quit()

files = [file for file in os.listdir("raw/categories") if file.endswith(".csv")]

raw = pd.concat([pd.read_csv(os.path.join("raw/categories", file)) for file in files], ignore_index=True)

raw.to_csv(path_or_buf="raw.csv", index=False)
