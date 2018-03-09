import sys
import json

from bddrest.authoring import given, when, then, and_, response, composer


def wsgi_application(environ, start_response):
    path = environ['PATH_INFO']
    if path.endswith('/None'):
        start_response('404 Not Found', [('Content-Type', 'text/plain;charset=utf-8')])
        yield b''
    else:
        start_response('200 OK', [('Content-Type', 'application/json;charset=utf-8')])
        result = json.dumps(dict(
            foo='bar'
        ))
        yield result.encode()


if __name__ == '__main__':
    with given(
            wsgi_application,
            title='Quickstart!',
            url='/books/id: 1',
            as_='visitor') as story:

        then(response.status == '200 OK')
        and_('foo' in response.json)
        and_(response.json['foo'] == 'bar')

        when(
            'Trying invalid book id',
            url_parameters={'id': None}
        )

        then(response.status_code == 404)

    story.dump(sys.stdout)
    story.document(sys.stdout)

