## $5 Tech Unlocked 2021!
[Buy and download this Book for only $5 on PacktPub.com](https://www.packtpub.com/product/python-microservices-development/9781785881114)
-----
*If you have read this book, please leave a review on [Amazon.com](https://www.amazon.com/gp/product/1785881116).     Potential readers can then use your unbiased opinion to help them make purchase decisions. Thank you. The $5 campaign         runs from __December 15th 2020__ to __January 13th 2021.__*

# Python Microservices Development
This is the code repository for [Python Microservices Development](https://www.packtpub.com/web-development/python-microservices-development?utm_source=github&utm_medium=repository&utm_campaign=9781785881114), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
We often deploy our web applications into the cloud, and our code needs to interact with many third-party services. An efficient way to build applications to do this is through microservices architecture. But, in practice, it's hard to get this right due to the complexity of all the pieces interacting with each other.


## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.

Chapter 11 does not have any code files

The source code for the Runnerly application that is developed across the book is also provided in the code bundle.

The code will look like the following:
```
import time

def application(environ, start_response):
    headers = [('Content-type', 'application/json')]
    start_response('200 OK', headers)
    return bytes(json.dumps({'time': time.time()}), 'utf8')
```

To execute the commands and applications in this book, you will need Python 3.x, Virtualenv 1.x, and Docker CE installed on your system. Detailed instructions are given in the chapters where needed.

## Related Products
* [Microservices: Building Scalable Software](https://www.packtpub.com/application-development/microservices-building-scalable-software?utm_source=github&utm_medium=repository&utm_campaign=9781787285835)

* [Learning Python Application Development](https://www.packtpub.com/application-development/learning-python-application-development?utm_source=github&utm_medium=repository&utm_campaign=9781785889196)

* [wxPython Application Development Cookbook](https://www.packtpub.com/application-development/wxpython-application-development-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781785287732)
