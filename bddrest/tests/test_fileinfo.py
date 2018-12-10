from os import path
from bddrest import FileInfo


HERE = path.dirname(__file__)
STUFF = path.join(HERE, 'stuff')
SAMPLEFILE = path.join(STUFF, 'sample-file.txt')


def test_fileinfo():
    file_info = FileInfo(SAMPLEFILE)
    assert file_info.name == 'sample-file.txt'
    assert file_info.directory == \
        '/home/mohamad/workspace/bddrest/bddrest/tests/stuff'

    assert 'name', 'directory' in file_info.to_dict()

