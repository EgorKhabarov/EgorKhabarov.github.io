<!-- -->

# Коды ответов

[https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP](https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP)

- [100 информационный](#1xx)
- [200 успешный](#2xx)
- [300 перенаправление](#3xx)
- [400 клиентская ошибка](#4xx)
- [500 серверная ошибка](#5xx)

## 1xx Status Codes: Information Requests

- [100 CONTINUE](#100-continue)
- [101 SWITCHING PROTOCOLS](#101-switching-protocol)
- [102 PROCESSING](#102-processing)
- [103 EARLY HINTS](#103-early-hints)

### 100 Continue
This interim response indicates that everything so far is OK and that the client should continue the request, or ignore the response if the request is already finished
### 101 Switching Protocol
This code is sent in response to an Upgrade request header from the client, and indicates the protocol the server is switching to
### 102 Processing
This code indicates that the server has received and is processing the request, but no response is available yet
### 103 Early Hints
This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response

<details>
    <summary>1xx</summary>
    <img alt="http-status-code1-xx.png" src="General/HTTP/1xx.png" style="width: 20em;">
</details>

## 2xx Status Codes: Successful Requests

- [200 OK](#200-ok)
- [201 CREATED](#201-created)
- [202 ACCEPTED](#202-accepted)
- [203 NON-AUTHORITATIVE INFORMATION](#203-non-authoritative-information)
- [204 NO CONTENT](#204-no-content)
- [205 RESET CONTENT](#205-reset-content)
- [206 PARTIAL CONTENT](#206-partial-content)
- [207 MULTI-STATUS](#207-multi-status)
- [208 ALREADY REPORTED](#208-already-reported)
- [226 IM USED PROCESSING](#226-im-used-processing)

### 200 OK
The request has succeeded.
The meaning of success depends on the HTTP method:
• GET: The resource has been fetched and is transmitted in the message body
• HEAD: The entity headers are in the message body
• PUT or POST: The resource describing the result of the action is transmitted in the message body
• TRACE The message body contains the request message as received by the server
### 201 Created
The request has succeeded and a new resource has been created as a result.
This is typically the response sent after POST requests, or same FUT requests
### 202 Accepted
The request has been received but not yet acted upon.
It is noncommittal since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request.
It is intended for cases where another process or server handles the request, or for batch processing
### 203 Non-Authoritative information
This response code means the returned meta information is not exactly the same
as is available from the origin servet, but is collected from a local or a third-party copy.
This is mostly used for mirrors or backups of another resource.
Except for that specific case, the "200 OK" response is preferred to this status
### 204 No Content
There is no content to send for this request, but the headers may be useful.
The user-agent may update its cached headers for this resource with the new ones
### 205 Reset Content
Tells the user agent to reset the document which sent this request
### 206 Partial Content
This response code is used when the Range header is sent from the client to request only part of a resource
### 207 Multi-Status
Conveys information about multiple resources, for situations where multiple status codes might be appropriate
### 208 Already Reported
Used inside a response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection
### 226 IM Used
The server has fulfilled a GET request for the resource, and the response
is a representation of the result of one or more instance manipulations applied to the current instance

<details>
    <summary>2xx</summary>
    <img alt="http-status-code2-xx.png" src="General/HTTP/2xx.png" style="width: 20em;">
</details>

## 3xx Status Codes: Redirections

- [300 MULTIPLE CHOICES](#300-multiple-choices)
- [301 MOVED PERMANENTLY](#301-moved-permanently)
- [302 FOUND](#302-found)
- [303 SEE OTHER](#303-see other)
- [304 NOT MODIFIED](#304-not-modified)
- [305 USE PROXY](#305-use-proxy)
- [306 SWITCH PROXY](#306-switch-proxy)
- [307 TEMPORARY REDIRECT](#307-temporary-redirect)
- [308 PERMANENT REDIRECT](#308-permanent-redirect)

### 300 Multiple Choice
The request has more than oné possible response.
The user-agent or user should choose one of them. (There is no standardized way of choosing
one of the responses, but HTML links to the possibilities are recommended so the user can pick)
### 301 Moved Permanently
The URL of the requested resource has been changed permanently.
The new URL is given in the response.
### 302 Found
This response code means that the URI of requested resource has been changed temporarily.
Further changes in the URI might be made in the future.
Therefore, this same URi should be used by the client in future requests
### 303 See Other
The server sent this response to direct the client to get the requested resource at another URI with a GET request
### 304 Not Modified
This is used for caching purposes it tells the client that the response
has not been modified, so the client can continue to use the same cached version of the response,
### 305 Use Proxy
Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by
a proxy it has been deprecated due to security concerns regarding in-band configuration ol a proxy.
### 306 Unused
This response code is no longer used, it is just reserved.
It was used in a previous version of the HTTP/1.1 specification.
### 307 Temporary Redirect
The server sends this response to direct the client to get the requested resource at another URI with the same method that was used in the prior request.
This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP method used
if a POST was used in the first request a POST must be used in the second request.
### 308 Permanent Redirect
This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header.
This has the same semantics as the 301 Moved Permanently HTTP response code,
with the exception that the user agent must not change the HTTP method used:
if a POST was used in the fist request, a POST must be used in the second request.

<details>
    <summary>3xx</summary>
    <img alt="http-status-code3-xx.png" src="General/HTTP/3xx.png" style="width: 20em;">
</details>

## 4xx Status Codes: Client Errors

- [400 Bad Request](#400-bad-request)
- [401 Unauthorized](#401-unauthorized)
- [402 Payment Required](#402-payment-required)
- [403 Forbidden](#403-forbidden)
- [404 Not Found](#404-not-found)
- [405 Method Not Allowed](#405-method-not-allowed)
- [406 Not Acceptable](#406-not-acceptable)
- [407 Proxy Authentication Required](#407-proxy-authentication-required)
- [408 Request Timeout](#408-request-timeout)
- [409 Conflict](#409-conflict)
- [410 Gone](#410-gone)
- [411 Length Required](#411-length-required)
- [412 Precondition Failed](#412-precondition-failed)
- [413 Payload Too Large](#413-payload-too-large)
- [414 URI Too Long](#414-uri-too-long)
- [415 Unsupported Media Type](#415-unsupported-media-type)
- [416 Range Not Satisfiable](#416-range-not-satisfiable)
- [417 Expectation Failed](#417-expectation-failed)
- [418 I'm a Teapot](#418-i'm-a-teapot)
- [421 Misdirected Request](#421-misdirected-request)
- [422 Unprocessable Entity](#422-unprocessable-entity)
- [423 Locked](#423-locked)
- [424 Failed Dependency](#424-failed-dependency)
- [425 Too Early](#425-too-early)
- [426 Upgrade Required](#426-upgrade-required)
- [428 Precondition Required](#428-precondition-required)
- [429 Too Many Requests](#429-too-many-requests)
- [431 Request Header Fields Too Large](#431-request-header-fields-too-large)
- [440 Login Timout](#440-login-timout)
- [444 No Response](#444-no-response)
- [449 Retry With](#449-retry-with)
- [450 Blocked By Windows Parental Controls](#450-blocked-by-windows-parental-controls)
- [451 Unavailable For Legal Reasons](#451-unavailable-for-legal-reasons)
- [451 Redirect](#451-redirect)
- [495 Cert Error](#495-cert-error)
- [496 No Cert](#496-no-cert)
- [497 HTTP to HTTPS](#497-http-to-https)
- [498 Token Expired/Invalid](#498-token-expired/invalid)
- [499 Client Closed Request](#499-client-closed-request)
- [499 Token Required](#499-token-required)

### 400 Bad Request
The server could not understand the request due to invalid syntax.
### 401 Unauthorized
Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated".
That is, the client must authenticate itself to get the requested response.
### 402 Payment Required
This response code is reserved for future use.
The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists.
### 403 Forbidden
The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource.
Unlike 401 the client's identity is known to the server.
### 404 Not Found
The server can not find the requested resource.
In the browser, this means the URL is not recognized.
In an API, this can also mean that the endpoint is valid but the resource itself does not exist.
Servers may also send this response instead of 403 to hide the existence of a resource from an unauthorized client.
This response code is probably the most famous one due to its frequent occurrence on the web.
The resource could not be found.
This is often used as a catch-all for all Invalid URis requested of the server.
### 405 Method Not Allowed
The request method is known by the server but has been disabled and cannot be used.
For example, an API may forbid DELETE-ing a resource.
The two mandatory methods, GET and HEAD, must never be disabled and should not return this error code.
### 406 Not Acceptable
This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.
### 407 Proxy Authentication Required
This is similar to 401 but authentication is needed to be done by a proxy.
### 408 Request Timeout
This response is sent on an idle connection by some servers, even without any previous request by the client.
It means that the server would like to shut down this unused connection.
This response is used much more since some browsers, like Chrome, Firefox, or IE9, use HTTP pre connection mechanisms to speed up surfing.
Also, note that some servers merely shut down the connection without sending this message.
### 409 Conflict
This response is sent when a request conflicts with the current state of the server.
### 410 Gone
This response is sent when the requested content has been permanently deleted from the server, with no forwarding address.
Clients are expected to remove their caches and links to the resource.
The HTTP specification intends this status code to be used for "limited-time, promotional services".
APIs should not feel compelled to indicate resources that have been deleted with this status code.
### 411 Length Required
Server rejected the request because the Content-Length header field is not defined and the server requires it.
### 412 Precondition Failed
The client has indicated preconditions in its headers which the server does not meet.
### 413 Payload Too Large
Request entity is larger than limits defined by server;
the server might close the connection or return an Retry-After header field.
### 414 URI Too Long
The URI requested by the client is longer than the server is willing to interpret.
### 415 Unsupported Media Type
The media format of the requested data is not supported by the server, so the server is rejecting the request.
### 416 Range Not Satisfiable
The range specified by the Range header field In the request can't be fullfilled;
it's possible that the range is outside the size of the target URI's data.
### 417 Expectation Failed
This response code means the expectation indicated by the Expect request header field can't be met by the server.
### 418 I'm a Teapot
Any attempt to brew coffee with a teapot should result in the error code "418 I'm a teapot".
The resulting entity body MAY be short and stout.
### 421 Misdirected Request
The request was directed at a server that is not able to produce a response.
This can be sent by a server that is not configured to produce responses
for the combination of scheme and authority that are included in the request URI.
### 422 Unprocessable Entity
The request was formatted correctly but cannot be processed in its current form.
Often used when the specified parameters fail validation errors.
### 423 Locked
The requested resource was found but has been locked and will not be returned.
### 424 Failed Dependency
The request failed due to a failure of a previous request.
### 425 Too Early
Indicates that the server is unwilling to risk processing a request that might be replayed.
### 426 Upgrade Required
The server refuses to perform the request using the current protocol
but might be willing to do so after the client upgrades to a different protocol.
The server sends an Upgrade header in a 426 response to indicate the required protocol(s).
### 428 Precondition Required
The origin server requires the request to be conditional.
This response is intended to prevent the 'lost update' problem,
where a client GETs a resource's state, modifies it, and PUTs it back to the server,
when meanwhile a third party has modified the state on the server, leading to a conflict.
### 429 Too Many Requests
The user has sent too many requests in a given amount of time ("rate limiting").
### 431 Request Header Fields Too Large
The server is unwilling to process the request because its header fields are too large.
The request may be resubmitted after reducing the size of the request header fields.
### 440 Login Timout
A Microsoft extension. Indicates that your session has expired.
### 444 No Response
Used in Nginx logs to indicate that the server has returned
no information to the client and closed the connection (useful as a deterrent for malware).
### 449 Retry With
A Microsoft extension. The request should be retried after performing the appropriate action.
### 450 Blocked By Windows Parental Controls
A Microsoft extension, This error is given when Windows Parental Controls
are turned on and are blocking access to the given webpage.
### 451 Unavailable For Legal Reasons
A server operator has received a legal demand to deny access to a resource
or to a set of resources that Includes the requested resource.
### 451 Redirect
Used in Exchange ActiveSync if there either is a more efficient server
to use or the server cannot access the users mailbox.
### 495 Cert Error
Nginx internal code used when SSL client certificate error occurred
to distinguish it from 4XX in a log and an error page redirection.
### 496 No Cert
Nginx internal code used when client didn't provide certificate
to distinguish it from 4XX in a log and an error page redirection.
### 497 HTTP to HTTPS
Nginx internal code used for the plain HTTP requests that are sent to HTTPS port
to distinguish it from 4XX in a log and an error page redirection.
### 498 Token Expired/Invalid
Returned by ArcGIS for Server. A code of 498 indicates an expired or otherwise invalid token.
### 499 Client Closed Request
Used in Nginx logs to indicate when the connection has been closed by client
while the server is still processing its request, making server unable to send a status code back.
### 499 Token Required
Returned by ArcGIS for Server. A code of 499 indicates that a token is required (if no token was submitted).


<details>
    <summary>4xx</summary>
    <img alt="http-status-code4-xx.png" src="General/HTTP/4xx.png" style="width: 30em;">
</details>

## 5xx Status Codes: Server Errors

- [500 INTERNAL SERVER ERROR](#500-internal-server-error)
- [501 NOT IMPLEMENTED](#501-not-implemented)
- [502 BAD GATEWAY](#502-bad-gateway)
- [503 SERVICE UNAVAILABLE](#503-service-unavailable)
- [504 GATEWAY TIMEOUT](#504-gateway-timeout)
- [505 HTTP VERSION NOT SUPPORTED](#505-http-version-not-supported)
- [506 VARIANT ALSO NEGOTIATES](#506-variant-also-negotiates)
- [507 INSUFFICIENT STORAGE](#507-insufficient-storage)
- [508 LOOP DETECTED](#508-loop-detected)
- [509 BANDWIDTH LIMIT EXCEEDED (APACHE BW/LIMITED EXT)](#509-bandwidth-limit-exceeded-(apache-bw/limited-ext))
- [510 NOT EXTENDED](#510-not-extended)
- [511 NETWORK AUTHENTICATION REQUIRED](#511-network-authentication-required)
- [520 UNKNOWN ERROR (MICROSOFT / CLOUDFLARE)](#520-unknown-error-(-microsoft-/-cloudflare))
- [521 WEB SERVER IS DOWN (CLOUDFLARE)](#521-web-server-is-down-(cloudflare))
- [522 CONNECTION TIMED OUT (CLOUDFLARE)](#522-connection-timed-out-(cloudflare))
- [523 ORIGIN IS UNREACHABLE (CLOUDFLARE)](#523-origin-is-unreachable-(cloudflare))
- [524 A TIMEOUT OCCURRED (CLOUDFLARE)](#524-a-timeout-occurred-(cloudflare))
- [525 SSL HANDSHAKE FAILED (CLOUDFLARE)](#525-ssl-handshake-failed-(cloudflare))
- [526 INVALID SSL CERTIFICATE (CLOUDFLARE)](#526-invalid-ssl-certificate-(cloudflare))
- [527 RAILGUN ERROR (CLOUDFLARE)](#527-railgun-error-(-cloudflare))

<details>
    <summary>5xx</summary>
    <img alt="http-status-code5-xx.png" src="General/HTTP/5xx.png" style="width: 30em;">
</details>






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
