import socket, os

HOST, PORT = 'localhost', 8888

error = {
    '404': "<h1>Error 404: Page not found</h1>"
}

ending = "\n<p>Webserver hosted on " + HOST + ":" + str(PORT) + "</p>"


pages = {}

pagesfileslistt = [os.path.join(dp, f.replace("\\", "/")) for dp, dn, filenames in os.walk("./server/") for f in filenames if os.path.splitext(f)[1] in (".html", ".css", ".js")]
pagesfileslist = []
print("Loading pages...")
for file in pagesfileslistt:
    pagesfileslist.append( ( file.replace("\\", "/"), (file.replace("\\", "/") + " ")[9:-1] ))
for fname in pagesfileslist:
    file = open(fname[0], 'r')
    pages[fname[1]] = {"content": "\n".join(file.readlines()), "type": (os.path.splitext(fname[0])[1] + " ")[1:-1]}
    file.close()
    print(f"  Loaded {fname[1]}")
print(f"Loaded {len(pagesfileslist)} files pages from './server/'!")
#print(pages)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    data = request_data.decode()
    page = data[4 : data.index("HTTP")-1]
    if (len(page) == 1) and page == "/": page = "/index.html"
    if len(page.split(".")) < 1: page += ".html"
    #print(request_data.decode())
    print(f"Requested page {HOST}:{PORT}{page}")
    if page == "/favicon.ico":
        http_response = b"HTTP/1.1 404"
    else:
        response = pages.get((page + " ")[1:-1])
        if not response:
            if not pages.get('404'):
                response = error['404'] + ending
            else:
                response = pages.get('404')
            print("  Page not found, sending 404")
        http_response = b"HTTP/1.1 200 OK\n\"Content-Type\": \"text/" + bytes(response['type'], 'utf-8') + b"\"\n\n" + bytes(response['content'], 'utf-8')
    client_connection.sendall(http_response)
    client_connection.close()
