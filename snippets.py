import logging
import argparse

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name,snippet))
    return name, snippet
    
def get(name):
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return " "
    
def main():
    """main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description = "Store and retrieve snippets of text")
    arguments = parser.parse_args()
    
    
    
if __name__ == "__main__":
    main()
