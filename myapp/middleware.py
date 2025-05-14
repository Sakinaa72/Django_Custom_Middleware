from django.http import HttpResponseForbidden

# - Custom middleware to intercept and inspect incoming HTTP headers
# - Blocks requests from predefined blacklisted User-Agent strings
# - Adds a response header for verified requests
class BlockSuspiciousUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response=get_response
        self.blocked_agents=['BadBot','EvilScrapper','FakeBrowser']
        print("Middleware initialized")
        
    def __call__(self, request):
        user_agent=request.META.get("HTTP_USER_AGENT","")
        for agent in self.blocked_agents:
            return HttpResponseForbidden("Access Denied: Suspicious User Detected")
        response=self.get_response(request)
        response["X-Middleware"]='User-Agent Check Passed'
        return response
    
