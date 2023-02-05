import re
import json

from loguru import logger
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

NEXT_JS_STATIC_ROUTES = {}
NEXT_JS_DYNAMIC_ROUTES = []
DYNAMIC_ROUTE_REGEX = re.compile('\[[^\/]+\]')

with open('.next/server/pages-manifest.json') as fh:
    for path, file_location in json.load(fh).items():
        if DYNAMIC_ROUTE_REGEX.search(path):
             NEXT_JS_DYNAMIC_ROUTES.append(
                ('^' + DYNAMIC_ROUTE_REGEX.sub('[^\/]+', path) + '$', file_location))
        else:
            NEXT_JS_STATIC_ROUTES[path] = file_location

       
@app.route('/admin')
def admin_page():
    return render_template('tamplates/admin_page.html')


@app.route('/_next/static/<path:path>')
def next_static_route(path):
    return send_from_directory('.next/server', path)


@app.route('/<path:path>')
def next_route(path):
    path = '/' + path
    if path in NEXT_JS_STATIC_ROUTES:
        return send_from_directory('.next/server', NEXT_JS_STATIC_ROUTES[path])
    for path_regex, file_location in NEXT_JS_DYNAMIC_ROUTES:
        if re.match(path_regex, path):
            send_from_directory('.next/server', file_location)
    abort(404)
   