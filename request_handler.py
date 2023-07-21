import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import (
    get_all_entries,
    get_single_entry,
    create_entry,
    delete_entry,
    update_entry,
    get_all_moods,
    get_single_mood,
    create_mood,
    delete_mood,
    update_mood,
    get_all_tags,
    get_single_tag,
    create_tag,
    delete_tag,
    update_tag,
    get_all_entry_tags,
    get_single_entry_tag,
    create_entry_tag,
    delete_entry_tag,
    update_entry_tag
)

class HandleRequests(BaseHTTPRequestHandler):
    """
    Controls the functionality of any GET, PUT, POST, DELETE
    requests to the server
    """

    def _set_headers(self, status, location=None):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        if location:
            self.send_header('Location', location)
        self.end_headers()

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def do_GET(self):
        """
        Handle HTTP GET requests.

        """
        self._set_headers(200)
        response = {}  # Default response

        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            if id is not None:
                response = get_single_entry(id)
            else:
                response = get_all_entries()
        elif resource == "moods":
            if id is not None:
                response = get_single_mood(id)
            else:
                response = get_all_moods()
        elif resource == "tags":
            if id is not None:
                response = get_single_tag(id)
            else:
                response = get_all_tags()
        elif resource == "entry_tags":
            if id is not None:
                response = get_single_entry_tag(id)
            else:
                response = get_all_entry_tags()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """
        Handle HTTP POST requests.

        """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_entry = None
        new_mood = None
        new_tag = None
        new_entry_tag = None

        if resource == "entries":
            new_entry = create_entry(post_body)
        elif resource == "moods":
            new_mood = create_mood(post_body)
        elif resource == "tags":
            new_tag = create_tag(post_body)
        elif resource == "entry_tags":
            new_entry_tag = create_entry_tag(post_body)

        if new_entry is not None:
            self._set_headers(201, f"/entries/{new_entry['id']}")
            self.wfile.write(json.dumps(new_entry).encode())
        elif new_mood is not None:
            self._set_headers(201, f"/moods/{new_mood['id']}")
            self.wfile.write(json.dumps(new_mood).encode())
        elif new_tag is not None:
            self._set_headers(201, f"/tags/{new_tag['id']}")
            self.wfile.write(json.dumps(new_tag).encode())
        elif new_entry_tag is not None:
            self._set_headers(201, f"/entry_tags/{new_entry_tag['id']}")
            self.wfile.write(json.dumps(new_entry_tag).encode())

    def do_PUT(self):
        """
        Handle HTTP PUT requests.

        """
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        put_body = self.rfile.read(content_len)
        put_body = json.loads(put_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            update_entry(id, put_body)
        elif resource == "moods":
            update_mood(id, put_body)
        elif resource == "tags":
            update_tag(id, put_body)
        elif resource == "entry_tags":
            update_entry_tag(id, put_body)

        self.wfile.write("".encode())

    def do_DELETE(self):
        """
        Handle HTTP DELETE requests.

        """
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            delete_entry(id)
        elif resource == "moods":
            delete_mood(id)
        elif resource == "tags":
            delete_tag(id)
        elif resource == "entry_tags":
            delete_entry_tag(id)

        self.wfile.write("".encode())

def main():
    """
    Starts the server on port 8088
    using the HandleRequests class

    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
