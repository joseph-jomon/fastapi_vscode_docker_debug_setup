Behind a TLS Termination Proxy¶
If you are running your container behind a TLS Termination Proxy (load balancer) like Nginx or Traefik, add the option --proxy-headers, this will tell Uvicorn (through the FastAPI CLI) to trust the headers sent by that proxy telling it that the application is running behind HTTPS, etc.


CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]


https://fastapi.tiangolo.com/deployment/docker/#use-cmd-exec-form