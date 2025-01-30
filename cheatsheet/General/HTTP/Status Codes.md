# Коды ответов

[https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP](https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP)

- [100 информационный](#1xx)
- [200 успешный](#2xx)
- [300 перенаправление](#3xx)
- [400 клиентская ошибка](#4xx)
- [500 серверная ошибка](#5xx)

## 1xx Status Codes: Information Requests

<!--
- [100 CONTINUE](#)
- [101 SWITCHING PROTOCOLS](#)
- [102 PROCESSING](#)
- [103 EARLY HINTS](#)

### 100 Continue
This interim response indicates that everything so far is OK and that the client should continue the request, or ignore the response if the request is already finished.
### 101 Switching Protocol
This code is sent in response to an Upgrade request header from the client, and indicates the protocol the server is switching to.
### 102 Processing
This code indicates that the server has received and is processing the request, but no response is available yet.
### 103 Early Hints
This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response.

-->
<img alt="http-status-code1-xx.png" src="General/HTTP/1xx.png" style="width: 20em;">
## 2xx Status Codes: Successful Requests
<!--

- [200 OK](#200%20ok)
- [201 CREATED](#201%20created)
- [202 ACCEPTED](#202%20accepted)
- [203 NON-AUTHORITATIVE INFORMATION](#203%20non-authoritative%20information)
- [204 NO CONTENT](#204%20no%20content)
- [205 RESET CONTENT](#205%20reset%20content)
- [206 PARTIAL CONTENT](#206%20partial%20content)
- [207 MULTI-STATUS](#207%20multi-status)
- [208 ALREADY REPORTED](#208%20already%20reported)
- [226 IM USED PROCESSING](#226%20im%20used%20processing)

### 200 OK
The request has succeeded. The meaning of success depends on the HTTP method:
• GET: The resource has been fetched and is transmitted in the message body
• HEAD: The entity headers are in the message body.
• PUT or POST: The resource describing the result of the action is transmitted in the message body.
• TRACE The message bady contains the request message as received by the server
### 201 Created
The request has succeeded and a new resource has been created as a result. This is typically the response sent after POST requests, or same FUT requests
### 202 Accepted
The request has been received but not yet acted upon. It is noncommittal since there is no way in HTTP to later send an asynchronous response indicating the dutcome of the request. it is intended for cases where another process or server handles the request, or for batch processing.
### 203 Non-Authoritative information
This resporse code means the returned meta information is not exactly the same as is available from the origin servet, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the "200 OK" response is preferred to this status.
### 204 No Content
There is no content to send for this request, but the headers may be usetul The user agont may update its cached headers for this resource with the new ones.
### 205 Reset Content
Tells the user agent to reset the document which sent this request.
### 206 Partial Content
This response code is used when the Range header is sent from the client to request only part of a resource.
### 207 MuliStatus
Conveys information about multiple resources, for situations where multiple status codes might be appropriate.
### 208 Already Reported
Used inside a response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.
### 226 IM Used
The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance manipulations applied to the current instance.

-->
<img alt="http-status-code2-xx.png" src="General/HTTP/2xx.png" style="width: 20em;">
## 3xx Status Codes: Redirections
<!--

- [300 MULTIPLE CHOICES](#300%20multiple%20choices)
- [301 MOVED PERMANENTLY](#301%20moved%20permanently)
- [302 FOUND](#302%20found)
- [303 SEE OTHER](#303%20see other)
- [304 NOT MODIFIED](#304%20not%20modified)
- [305 USE PROXY](#305%20use%20proxy)
- [306 SWITCH PROXY](#306%20switch%20proxy)
- [307 TEMPORARY REDIRECT](#307%20temporary%20redirect)
- [308 PERMANENT REDIRECT](#308%20permanent%20redirect)

### 300 Multiple Choice
The request has more than oné possible response. The user-agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick)
### 301 Moved Permanently
The URL of the requested resource has been changed permanently. The new URL is given in the response.
### 302 Found
This response code means that the URI of requested resource has been changed temporarily, Further changes in the URI might be made in the future, Therefore. this same URi should be used by the client in future requests
### 303 See Other
The server sent this response to direct the client to get the requested resource at another URI with a GET request
### 304 Not Modified
This is used for caching purposes it tells the client that the response has not been modified, so the client can continue to use the same cached version of the response,
### 305 Use Proxy
Deline in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy it has been deprecated due to securny concerns regarding in-band configuration ol a proxy.
### 306 Unused
This response code is no longer used, it is just reserved. It was used in a previous versiion of the HTTP/1.1 specification.
### 307 Temporary Redirect
The server sends this response to direct the client to get the requested resource at another URI with the same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP methiod used ifa POST was used in the first request a POST must be used in the second request.
### 308 Permanent Redirect
This means that the resource is now permanently located at anather URI, specified by the Location: HTTP Response header. This has the same semantics as the 301 Moved Permanently HTTP response code, with the exception that the user agent must not change the HTTP method used: ifa POST was used in the fist request a POST must be used in the second request.

-->
<img alt="http-status-code3-xx.png" src="General/HTTP/3xx.png" style="width: 20em;">
## 4xx Status Codes: Client Errors
<!--

- [400 Bad Request](#400%20bad%20request)
- [401 Unauthorized](#401%20unauthorized)
- [402 Payment Required](#402%20payment%20required)
- [403 Forbidden](#403%20forbidden)
- [404 Not Found](#404%20not%20found)
- [405 Method Not Allowed](#405%20method%20not%20allowed)
- [406 Not Acceptable](#406%20not%20acceptable)
- [407 Proxy Authentication Required](#407%20proxy%20authentication%20required)
- [408 Request Timeout](#408%20request%20timeout)

### 400 Bad Request
The server could not understand the request due to Invalid syntax.
### 401 Unauthorized
Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.
### 402 Payment Required
This response code is reserved for future use, The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists.
### 403 Forbidden
The client does not have access rights to the content that is, it is unauthorized, so the server is refusing to give the requested. resource. Unlike 401 the client's identity is known to the server.
### 404 Not Found
The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 to hide the existence of a resource from an unauthorized client. This response code is probably the most famous one due to its frequent occurrence on the web. The resource could not be found. This is often used as a catch all for all Invalid URis requested of the server.
### 405 Method Not Allowed
The request method is known by the server but has been disabled and cannot be used. For example, an API may forbid DELFTE-ing a resource, The two mandatory methods, GET and HEAD, must never be disabled and should not return this error code.
### 406 Not Acceptable
This respanse is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.
### 407 Proxy Authentication Required
This is similar to 401 but authentication is needed to be done by a proxy.
### 408 Request Timeout
This response is sent on an idle connection by some servers, even without any previous request by the client, It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox, or IE9, use HTTP pre connection mechanisms to speed up surting. Also, note that some servers merely shut down the connection without sending this message.
-->

<img alt="http-status-code4-xx.png" src="General/HTTP/4xx.png" style="width: 30em;">
## 5xx Status Codes: Server Errors
<img alt="http-status-code5-xx.png" src="General/HTTP/5xx.png" style="width: 30em;">





<!--

# X


<div class="container-row" style="">
<img alt="http-status-code1-xx.png" src="General/HTTP/1xx.png" style="width: 20em;height: 50em;">
<img alt="http-status-code2-xx.png" src="General/HTTP/2xx.png" style="width: 20em;height: 139em;">
<img alt="http-status-code3-xx.png" src="General/HTTP/3xx.png" style="width: 20em;height: 131em;">
<img alt="http-status-code4-xx.png" src="General/HTTP/4xx.png" style="width: 30em;height: 351em;">
<img alt="http-status-code5-xx.png" src="General/HTTP/5xx.png" style="width: 30em;height: 175em;">
</div>


<div class="container-row" style="">
![http-status-code1-xx.png](General/HTTP/1xx.png)
![http-status-code2-xx.png](General/HTTP/2xx.png)
![http-status-code3-xx.png](General/HTTP/3xx.png)
![http-status-code4-xx.png](General/HTTP/4xx.png)
![http-status-code5-xx.png](General/HTTP/5xx.png)
</div>
-->


<!-- ![http-status-codes.png](General/HTTP/http-status-codes.png) -->
