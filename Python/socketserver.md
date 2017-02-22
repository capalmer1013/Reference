# socketserver module **Python 3**

Basic Server Classes:
- TCPServer - uses the internet TCP protocol - continuous streams between client and server.
- UDPServer - uses datagrams, discrete packets, may arrive out of order or be lost.
- UnixStreamServer - use Unix domain sockets
- UnixDatagramServer - use Unix domain sockets

These 4 classes process requests **synchronously** each request must be completed before the next can be started.

If necessary to be async for throughput, can use the ForkingMixIn or ThreadingMixIn classes.

## Creating a server:
- create a request handler class by subclassing the BaseRequestHandler and overriding handle() method (to handle incoming requests)
- instantiate one of the server classes, passing it the server's address and the request handler class
- call handle_request() or serve_forever() method of the server object to process one or many requests.
- call server_close() to close the socket

## ThreadingMixIn notes:
when inheriting from ThreadingMixIn for threaded connection behaviour, you should explicitly declare how you want your threads to behave on an abrupt shutdown.
The ThreadedMixIn class defines an attribute *daemon_threads*, which indicates whether or not the server should wait for thread termination.
Default is False, meaning that Python will not exit until all threads created by ThreadingMixIn have exited.

All server classes have the same external methods and attributes , no matter what network protocol they use.

---

## Server creation notes
```python
class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass
```
The mix0in class must come first, since it overrides a method defined in UDPServer. Setting the various attributes also change the behaviour of the underlyung server mechanism.

To implement a service, you must derive a class from BaseRequestHandler and redefine its `handle()` method. You can then run various versions of the service by combining one of the server classes with your request hander class. The request handler class must be different for datagram or stream services. This can be hidden by using the handler subclasses StreamRequestHandler of DatagramRequestHandler

Building an HTTP server where all data is stored externally (i.e. file system), a synchronous class will essentially render the service "dead" while one request is being handled - which may be for a while. Using a threading or forking server is approrpiate here.

---

## Server Objects


class socketserver.BaseServer:
	superclass of all Server objects in the module. It defines the interface, given below, but does not implement most of the methods, which is done in subclasses.
- BaseServer:
	- fileno(): returns an integer file descriptor for the socket on which the server is listening.
	- handle_request(): Process a single request. calls following mehods in order:
		1. get_request()
		2. verify_request()
		3. process_request()

	- serve_forever(poll_interval=0.5): handle requests until explicit shutdown() request.
	
	- service_actions(): called by the serve_forever() loop.
	
	- shutdown(): Tell the serve_forever() loop to stop and wait until it does.
	
	- server_close(): clean up the server. may be overridden.
	
	- address_family: family of protocols that the serer's socket belongs.
		- socket.AF_INET
		- socket.AF_UNIX
		
	- RequestHandlerClass: user-provided request handler class (instance created for each request)
	
	- server_address: the address that the server is listening.
	
	- socket: the socket object on which the server will listen for incoming requests
	
	- allow_reuse_address: whether the server will allow the reuse of an address. default False.
	
	- request_queue_size: the size of the request queue for requests that are received while busy.
	
	- socket_type: type of socket used by the server. Common Values:
		- socket.SOCK_STREAM
		- socket.SOCK_DGRAM
		
	- timeout: timeout duration, measured in seconds. if handle_request() receives no incoming requests wihin timeout period, the handle_timeout() method is called.
	
	- finish_request(): actually processes the request by instantiating RequestHandlerClass and calling its handle() method.
	
	- get_request(): must accept a request from the socket, and return a 2-tuple containing the *new*socket object to be used to communicate with the client, and the client's address.

	- handle_error(request, client_address): This function is called if the RequestHandlerClass's handle() method reaises and exception. the default action is to print the traceback to standard outpu and continue handling further requests.
	
	- handle_timeout(): method that is called when the timeout sttribute has been set to a value other than None and the timeout period has passed with no requests being received.
