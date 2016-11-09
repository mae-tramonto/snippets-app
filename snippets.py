import logging

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name,snippet))
    return name, snippet
    
def get(name):
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return " "