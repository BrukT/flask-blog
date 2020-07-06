# flask-web
a simple web page using bootstrap and flask

This website is based on the tutorial which is found [here](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3).

An improvement is the page is containerized in docker. For running the mini blog post:

``` docker build -t app . && docker run -p 5000:5000 app ```
