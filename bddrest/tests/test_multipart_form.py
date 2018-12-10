from os import path
import base64
import cgi
import hashlib
import io

from bddrest import Given, response, status


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

    start_response('200 OK', [
        ('Content-Type', 'text/plain;charset=utf-8'),
    ])
    binary_file = form['a'].file
    yield base64.encodebytes(hashlib.md5(binary_file.read()).digest()).decode()


BINARY_CONTENT = \
    b'{\xe2\xbd\x8a\x8eo\x19\x88\xbe\xf1+\xb6}\xccqoDz\xf3\xb7>\x8c\x83' \
    b'\x0f\xfe\xecj\xbcg\xbe0\x0f\xe25\x1d\x80\x1f\x023\x16\xe0\xf8\x0f' \
    b'\xc8\xca!\xe8\x01\n'

BINARY_CONTENT_HASH = hashlib.md5(BINARY_CONTENT).digest()


with open(SAMPLEFILE, 'rb') as f:
    SAMPLEFILE_CONTENT_HASH = hashlib.md5(f.read()).digest()


def test_upload_binary_file_bytesio():

    call = dict(
        title='Uploading an image',
        verb='POST',
        multipart=dict(a=io.BytesIO(BINARY_CONTENT))
    )

    with Given(wsgi_application, **call):
        assert status == '200 OK'
        assert base64.decodebytes(response.body) == BINARY_CONTENT_HASH

def test_upload_binary_file_fileio():

    call = dict(
        title='Uploading an image using fileio',
        verb='POST',
        multipart=dict(a=io.FileIO(SAMPLEFILE))
    )

    with Given(wsgi_application, **call):
        assert status == '200 OK'
        assert base64.decodebytes(response.body) == SAMPLEFILE_CONTENT_HASH

