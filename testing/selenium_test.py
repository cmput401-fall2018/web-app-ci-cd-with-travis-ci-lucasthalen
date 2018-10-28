from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
    driver = webdriver.Firefox() # My dev environment has chromium installed, not sure if that works with the Chrome driver.
    driver.get("http://204.209.76.222:8000")
    e_names = {
        'name':"NAME", 
        'about':"About", 
        'education':"Education", 
        'skills':"Skills", 
        'work':"Work", 
        'contact':"Contact"
    }
    print("Testing for data in elements:")
    justify = len(max(e_names, key = lambda x: len(x)))
    for elem in e_names:
        resStr = ""
        val = driver.find_element_by_id(elem)
        assert val != None and val.text != e_names[elem] # check values are populating from db and exist

        # Report results
        resStr = "    {} | ID: {} | Src: {}".format(
            "PASS",
            elem + " "*((justify - len(elem)) + 2),
            'sqlite_db' if val.text != e_names[elem] else 'default'
        )
        
        print(resStr)
    driver.quit() # End driver so it doesn't hang

test_home() # Call tests on Homepage (Index.html)   ##### REMOVE THIS IF THERE ARE IMPORT ISSUES