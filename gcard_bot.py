from selenium import webdriver
import urllib3
import json

webhook = 'https://discord.com/api/webhooks/825779409604444200/MvHJ_JN6yGxqon695T2o4AFQUg6DRsctwlnrxQdC7SEEYvwDuQFjWYFq6Wu1RW37XHr5'

def alert_string(value, tts = False):
    bot_string = {"username": "GCard Bot", "content": str(value), "tts": tts}
    data = json.dumps(bot_string).encode('utf-8')
    client = urllib3.PoolManager()
    request = client.request("POST", webhook, body=data, headers={'Accept': 'application/json', 'Content-type': 'application/json'})

def alert_purchase(price):
    alert_string("Graphics Card Alert! @everyone \n Purchase Attempt at : $" + str(price), tts=True)

def alert_current_price(price, card_name='-', card_url='-'):
    alert_string("Current Price of Card: $" + str(price) + " Card: " + card_name + "\n" + "Link: " + card_url)

class gcardbot():
    def __init__(self, amazon_link, name, limit, tax, amazon_username, amazon_password):
        self.driver = webdriver.Chrome('C:\\Program Files\\Chromedriver\\chromedriver.exe')
        self.price_limit = limit
        self.tax_limit = tax
        self.debug = True
        self.purchased = False
        self.link = amazon_link
        self.card_name = name
        self.username = amazon_username
        self.password = amazon_password

    def goto_card_page(self):
        self.driver.get(self.link)

    def login(self):
        self.goto_card_page()
        expand_sign_in = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]')
        expand_sign_in.click()
        email_entry = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
        continue_bttn = self.driver.find_element_by_xpath('//*[@id="continue"]')
        email_entry.send_keys(self.username)
        continue_bttn.click()
        password_entry = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
        password_entry.send_keys(self.password)
        signin_bttn = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
        signin_bttn.click()

    def get_price(self):
        price_e = self.driver.find_element_by_xpath('//*[@id="price_inside_buybox"]')
        print(price_e.text)
        return price_e      
        
    def refresh_page(self):
        self.driver.refresh()

    def search_for_card(self):
        while(not bot.purchased):
            bot.refresh_page()
            try:
                price = bot.get_price()
                if(price):
                    price_clean = price.text.replace("$", "")
                    price_array = price_clean.split('.')
                    real_price = int(price_array[0])
                    alert_current_price(real_price, self.card_name, self.link)
                    if(real_price < bot.price_limit):
                        print("Price Below limit! Purchasing")
                        alert_purchase(real_price)
                        # do stuff to actually buy the card
                        bot.purchase_card()
                        bot.purchased = True
                    else:
                        print("Price Above limit! not purchasing")
                        alert_string("Price Above limit : $" + str(real_price) + " >" + str(self.price_limit))
            except:
                print("no stock / error - refreshing")

    def purchase_card(self):
        add_to_cart = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
        if(add_to_cart):
            add_to_cart.click()
        go_to_checkout = self.driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
        if(go_to_checkout):
            go_to_checkout.click()
        try:
            confirm_address = self.driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a')
            if(confirm_address):
                confirm_address.click()
        except:
            print("address already filled\n")

        try:
            continue_bttn = self.driver.find_element_by_xpath('//*[@id="shippingOptionFormId"]/div[1]/div[2]/div/span[1]/span/input')
            if(continue_bttn):
                continue_bttn.click()       
        except:
            print("shipping already filled")

        try:
            continue_bttn2 = self.driver.find_element_by_xpath('//*[@id="pp-xM6QMF-74"]/span/input')
            if(continue_bttn2):
                continue_bttn2.click()
        except:
            print("shipping already confirmed")
        try:
            place_order = self.driver.find_element_by_xpath('//*[@id="placeYourOrder"]/span/input')
            if(place_order):
                total = self.driver.find_element_by_xpath('//*[@id="subtotals-marketplace-table"]/tbody/tr[7]/td[2]')
                total_real = total.text.replace('$', "")
                total_array = total_real.replace(',', "").split('.')
                final_total = total_array[0]
                
                # Tax Buffer
                if(int(final_total) > self.price_limit + 0):
                    alert_string("Final Total : $" + final_total + " Greater than price limit $" + str(self.price_limit))
                    exit()
                alert_string("Ordered at Price: $" + final_total)
                place_order.click()
        except:
            print("place error")

bot = gcardbot(
    amazon_link='https://www.amazon.com/dp/B083Z5P6TX?smid=ATVPDKIKX0DER&tag=fixitservices-20',
    name="GeForce RTX 3060Ti 8GB GDDR6",
    limit=600,
    tax=20,
    amazon_username='<email>',
    amazon_password='<password>')

bot.login()
print('make sure that the catchpa has not triggered, if it has fill it out then enter any key in the console')
# wait for user input after they finished logging in
unused = input()
bot.search_for_card()
print("Purchase complete exiting...")