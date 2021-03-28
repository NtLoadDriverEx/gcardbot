# Graphics Card Bot
Written in an hour and by someone who codes C++ so it is nothing pretty.

Can be used to search for several cards. I don't know how to thread or if you can thread in python but it would require threading unless you wanted to run several instances of chrome.

if you wanted you could feasibly have each tab and refresh each on individually and check for the price and the code for all of that is already there.

configuration is as simple as changing the webhook link at the top and the constructor inputs for the bot.

it checks the price twice and doesn't care how many things are in the cart. That is very easy to add if you want to, however I didn't need it so I didn't add it.

I'm sure this is slow as havivng an entire chrome instance just to buy a card is kind of ubsurd, don't expect to use this to be a scalper. however its still fast enough to hopefully *beat* the scalpers and get an individual card. that's what I wrote this for anyway.

Most likely won't work in other localized pages. I don't know if xpath's change depending on localization. (again not a python dev)

# Chrome Webdriver

make sure the webdriver version you have matches your chrome version. The executable in the repository is for the latest (3/28/2021) version of chrome to date.

# Extra Configuration 

Make sure that the process to go from cart to checkout matches whats in the code i.e. dry run it without the card or with something cheap and make sure it can purchase something.

simple things I can think of to check would be:
    1: make sure you have a valid address saved
    2: make sure you have a card added
    3: make sure that there isn't going to be one of those free 75$ credit card offers

