import io
import cgi
import json
import hashlib
import binascii
import tempfile
from os import path

import pytest

from bddrest import Given, when, story, response, InvalidUrlParametersError, \
    CallVerifyError, Call, AlteredCall, Story


HERE = path.dirname(__file__)
STUFF = path.join(HERE, 'stuff')
SAMPLEFILE = path.join(STUFF, 'sample-file.txt')


def wsgi_application(environ, start_response):
    form = cgi.FieldStorage(
        fp=environ['wsgi.input'],
        environ=environ,
        strict_parsing=False,
        keep_blank_values=True
    )
    submitted_file = form['a']

    start_response('200 OK', [
        ('Content-Type', 'application/json;charset=utf-8'),
    ])
    result = dict(
        filename=submitted_file.filename
    )

    identity = environ.get('HTTP_AUTHORIZATION')
    if identity:
        result['identity'] = identity
    yield json.dumps(result).encode()


def test_url_parameters():
    call = dict(
        title='Sending file in multipart',
        verb='POST',
        multipart=dict(
            a=io.FileIO(SAMPLEFILE),
        ),
    )

    with Given(wsgi_application, **call):
        assert response.status == '200 OK'
        dumped_story = story.dumps()

