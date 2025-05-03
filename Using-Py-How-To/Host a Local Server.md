## 🚀 One-Liner HTTP Servers – Serve Current Directory Only

| **Language/Tool**  | **One-Liner Command**                                            | **Port** | **Notes**                            |
| ------------------ | ---------------------------------------------------------------- | -------- | ------------------------------------ |
| **Python 3**       | `python3 -m http.server 8080`                                    | 8080     | Most common, built-in                |
| **Python 2**       | `python -m SimpleHTTPServer 8080`                                | 8080     | For legacy systems                   |
| **PHP**            | `php -S 0.0.0.0:8080`                                            | 8080     | Great for .php too                   |
| **Ruby**           | `ruby -run -e httpd . -p 8080`                                   | 8080     | Clean & quick                        |
| **Node.js (npx)**  | `npx http-server -p 8080`                                        | 8080     | Requires `http-server` npm package   |
| **BusyBox**        | `busybox httpd -f -p 8080 -h .`                                  | 8080     | Lightweight, great in embedded Linux |
| **Go (Quick)**     | `go run -e '...'`                                                | 🤯       | Not truly 1-liner unless precompiled |
| **Docker (Nginx)** | `docker run -d -p 8080:80 -v "$PWD":/usr/share/nginx/html nginx` | 8080     | Serves current dir via Nginx         |

---

### 🧠 Pro Notes:

* All commands serve **current directory (`.`)** only.
* Replace `8080` with any port if needed.
* Perfect for:

  * Hosting payloads in web exploits.
  * Testing CORS, open redirect, SSRF.
  * Dropping files during engagements.
