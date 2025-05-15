from django.http import HttpResponseForbidden
from datetime import datetime
import time 

# Blocks HTTP requests from User-Agents matching a known list of bots or scrapers.
class BlockSuspiciousUserAgentsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_agents = ["badbot", "evilscraper", "fakebrowser"]  # lowercase match
        print("🛡️ BlockSuspiciousUserAgentsMiddleware initialized.")

    def __call__(self, request):
        user_agent = request.META.get("HTTP_USER_AGENT", "").lower()
        print(f"User-Agent Received: {user_agent}")  # Log what agent came in

        for agent in self.blocked_agents:
            if agent in user_agent:
                return HttpResponseForbidden("Access Denied: Suspicious User Detected")

        response = self.get_response(request)
        response["X-Middleware"] = "User-Agent Check Passed"
        return response

    
# Logs each incoming request's method, path, IP address, and timestamp to the console.
class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("📋 RequestLoggerMiddleware initialized.")

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR", "")
        path = request.path
        method = request.method
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"[{timestamp}] {method} request to {path} from IP: {ip}")

        response = self.get_response(request)
        return response
    
class ExecutionTimeLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response=get_response
    
    def __call__(self,request, *args, **kwds):
        start_time=time.time()
        response=self.get_response(request)
        duration=(time.time()-start_time)*1000
        print(f"[ExectuionTimeLoggerMiddleware]{request.method}{request.path} took {duration:.2f}ms")
        return response 
    
class BlockIPMiddleware:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwds):
        pass
    
class EnforceHTTPSMiddleware:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwds):
        pass
    
class CustomHeaderMiddleware:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwds):
        pass