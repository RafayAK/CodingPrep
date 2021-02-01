"""
This problem was asked by Twitch.

Describe what happens when you type a URL into your browser and press Enter
"""

"""
A general high-level overview of of how requests are made, comprises of the follows parts:
    - DNS lookup
    - HTTP Request
    - Server Handler
    - Rendering
     
DNS LOOKUP
    First, the URL, or domain name, mush be converted into an IP (internet protocol) address that the browser can
    use to send an HTTP request. Each domain name is associated with and IP address, much like
    in a Phonebook a phone number is associated to a  person's name. If the domain name, IP pair 
    is not saved in the browser's cache, then most browsers will ask the OS to look up or resolve the domain for it.
    
    Here, the OS usually have default DNS nameservers that it can lookup. These DNS servers are 
    essentially huge lookup tables. If an entry is not found in these nameservers, then it may query 
    other (usually ISP's DNS) to see if it exits there, and forward the results ( and store then in its own cache. )
     
HTTP REQUEST
    Once the browser has the correct IP address, it then sends an HTTP GET request to that IP.
    
    The HTTP request mush go through many networking layers (for example SSL if it's encrypted).
    These layers generally serve to protect the integrity of the data and do error correction.
    For example, the TCP layer handles reliability of the dat and orderedness. If packets underneath
    the TCP layer are corrupted (detected via checksum), the protocol dictates that the request 
    must be resent. If the packets arrive in the wrong order, it will reorder them.
    
    But basically, in the end, the server will receive a request from the client at the URL specified, 
    along with metadata in the headers and cookies.
    
    For more info lookup OSI model.
    
SERVER HANDLER
    Now the request has been received by some server. Popular server engines are nginx and Apache.
    What these servers do is handle it accordingly. If the website is static, for example, the server
    can serve a file from the local file system. More often, though, the request is forwarded to an
    application running on the webserver such as Django or Ruby on Rails.
    
    What these applications do is eventually return a response to the request, but sometimes it may have to perform
    some logic to serve it. For example, if you're of Facebook, their servers wil parse the request, see that
    you are logged in, and query their database and get the data for your Facebook feed.

RENDERING
    Now you browser has received a response to its request, usually in form of a HTML and CSS. HTML
    and CSS are markup languages that your browser can interpret to load content and style the page.
    Rendering and laying out HTML/CSS is very tricky process, and rendering engines have to be very flexible
    so that unclosed tags, for example, do crash the page.
    
    The request might also ask to load more resources, such and images, stylesheets, or JavaScript. 
    This makes more requests, and JavaScript may also be used to dynamically alter the page and make
    requests to the backend.
    
    More and more, web apps these days simply load a bare page containing JavaScript bundle, which, once 
    executed, fetches content from APIs. The JavaScript application then manipulates the DOM to add 
    the content it loaded.  
    
    resources: - Lets build a browser engine: https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html
               - How Browsers work : https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/ 
"""