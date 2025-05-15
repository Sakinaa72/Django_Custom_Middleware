# Django Custom Middlware

This is a simple Django Project demonstrating the use of **custom middleware** for:

- Blocking suspicious user-agents
- Logging all incoming HTTP requests

---

## Features

- **BlockSuspiciousUserAgentsMiddleware**  
  Blocks requests containing suspicious keywords in the `User-Agent` header.

- **RequestLoggerMiddleware**  
  Logs the method and path of every incoming request for monitoring purposes.

- **Execution Time Logger**
  Measures and logs the time each request takes to process.

- **Block IP Middleware**
  Blocks requests from specific IP addresses.

- **Enforce HTTPS**
  Automatically redirects all HTTP traffic to HTTPS.

- **Custom Header Middleware**
  Adds custom headers (e.g., app version, developer name) to all responses.

## 🚀 Setup and Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Django_Custom_Middleware.git
cd Django_Custom_Middleware
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
Copy code
pip install -r requirements.txt
```

### 4. Run the Server

```bash
Copy code
python manage.py runserver
App will run on: http://127.0.0.1:8000
```

📌 Endpoints

### 1. Root Endpoint

GET /

```bash
Description: Simple test route to verify middleware functionality.
Authentication: ❌ No token or login required
```

### ✅ Request:

```bash
curl http://127.0.0.1:8000/
```

### ✅ Expected Response:

```bash
{
"message": "Hello, World!"
}
```
