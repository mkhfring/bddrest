
from ..proxy import ObjectProxy
from ..specification import FirstCall, AlteredCall, Call

from .story import Story
from .given import Given
from .manipulation import Manipulator, Append, Remove, Update, \
    CompositeManipulatorInitializer
from .fileinfo import FileInfo


story = ObjectProxy(Given.get_current)
response = ObjectProxy(lambda: story.response)
status = ObjectProxy(lambda: response.status)
given = CompositeManipulatorInitializer()


def when(*args, **kwargs):
    return story.when(*args, **kwargs)

