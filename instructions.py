
##TERMINAL
# 1. install scrapy, cmd: pip install scrapy
# 2. start a project using scrapy. cmd: scrapy startproject foldername
# 3. fetch url, commands: scrapy shell,  fetch('url')
# 4. everything is saved in the response variable, command: response
# 5. Find the css element you're interested in, cmd: response.css('div.classname').get
#    //get() with fetch the first item , getall() for all items
# 6. save the filtered response to a variable. cmd : products = response.css('div.classname')
# 7. Look for the specific item from css to fetch it. cmd: products.css('small.author::text').get()
#  //u can use .replace('') to remove certain elements from strings


#Now to assembel spider py file
# create a new .py file to write script under spider folder
