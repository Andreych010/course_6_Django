from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open('html_files/main_page.html', encoding='utf-8') as f:
            return f.read()

    def __get_article_content(self, page_address):
        if page_address == 'Главная':
            with open('html_files/main_page.html', 'r', encoding='utf-8') as f:
                return f.read()
        elif page_address == 'Каталог':
            with open('html_files/Catalog.html', 'r', encoding='utf-8') as f:
                return f.read()
        elif page_address == 'Категории':
            with open('html_files/category.html', 'r', encoding='utf-8') as f:
                return f.read()
        elif page_address == 'Контакты':
            with open('html_files/contacts.html', 'r', encoding='utf-8') as f:
                return f.read()
        return 'Article not found!'

    def __get_blog_article(self, page_address):
        return f"""
        <html><head><title>Home_work_19.1</title></head><body>
        <p>{self.__get_article_content(page_address)}</p>
        </body>
        </html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_address = query_components.get('page')
        page_content = self.__get_index()
        if page_address:
            page_content = self.__get_blog_article(page_address[0])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
