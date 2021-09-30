from selenium import webdriver
import selenium
from time import sleep
import json
driver = webdriver.Chrome("./chromedriver.exe")
#driver.get("https://dantri.com.vn/suc-khoe/viet-nam-co-ca-tu-vong-thu-32-vi-covid-19-20200829121932549.htm")
driver.get("https://www.google.com/search?q=covid+site:dantri.com.vn")
sleep(2)
loop = 0
countPage = 0
time = []
titles = []
sapo = []
contents = []
authors = []
sources = []
limitCountPage=int(input("Enter the number limit of the Google search page: "))
try:
    elemens = driver.find_elements_by_css_selector('div.g')
    links = [elemen.find_element_by_tag_name("a").get_attribute('href') for elemen in elemens]
    while loop <=3 and countPage<limitCountPage:
        sleep(2)
        try:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            count = 0
            size = len(links)
            countPage +=1
            for link in links:
                try:
                    driver.get(link)
                    try:
                        time.append(driver.find_element_by_class_name("dt-news__time").text)
                        titles.append(driver.find_element_by_class_name("dt-news__title").text)
                        sapo.append(driver.find_element_by_class_name("dt-news__sapo").text)
                        contents.append(driver.find_element_by_class_name("dt-news__content").text)
                        sources.append(link)
                    except:
                        print("ERROR PAGE")
                        pass
                except:
                    pass
                count+=1
                print("%d in %d page %d" %(count, size, countPage))
                loop=0
            print("================================================")
            print("Crawled: %d page" %(len(titles)))
            print("================================================")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.find_element_by_xpath("//span[@style='display:block;margin-left:53px']").click()
        except:
            loop+=1
            print("ERROR TIMEOUT: %d" %(loop))
            pass
except:
    print("ERROR TIMEOUT")
    print("=> CLOSE")
    pass
finally:
    with open(r'data.json', 'w', encoding='utf-8') as dt:
        data = []
        for num in range(len(titles)):
            data.append({
                "time" : time[num],
                "title" : titles[num],
                "sapo" : sapo[num],
                "content" : contents[num],
                "source" : sources[num]
            })
        json.dump(data,dt, ensure_ascii=False)
try:
    print("Crawl well done!")
    driver.close()
except:
    print("Unexpectedly closed!")
finally:
    print("Crawled: %d page" %(len(data)))
