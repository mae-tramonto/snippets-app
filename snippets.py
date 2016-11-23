import logging
import argparse
import psycopg2

logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established.")

def put(name, snippet):
    """ Store a snippet with an associated name """
    logging.info("Storing a snippet {!r}: {!r}".format(name, snippet))
    with connection, connection.cursor() as cursor:
        try:
            command = "insert into snippets values (%s, %s)"
            cursor.execute(command, (name, snippet))
        except psycopg2.IntegrityError as e:
            connection.rollback()
            command= "update snippets set message=%s where keyword=%s"
            cursor.execute(command, (snippet, name))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet
    
def get(name):
    """Retrieving a snippet with a given keyword"""
    logging.info("Retrieving a snippet {!r}".format(name))
    #select = "select keyword, message from snippets where keyword=(%s)"
    with connection, connection.cursor() as cursor:
        cursor.execute("select keyword, message from snippets where keyword=(%s)", (name,))
        row = cursor.fetchone()
    if not row:
        return "404: Snippet not found"
    logging.info("Retrieved snippet {!r} as {!r} ".format(row[1], row[0]))
    logging.debug("Snippet was successfully retrieved.")
    return row
    

    
def main():
    """main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description = "Store and retrieve snippets of text")
    
    subparsers =parser.add_subparsers(dest= "command", help= "Available commands") 
    
    #Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser= subparsers.add_parser("put", help = "Store a snippet")
    put_parser.add_argument("name", help= "Name of the snippet")
    put_parser.add_argument("snippet", help= "Snippets text")
    
    #Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help= "Retrieve a snippet")
    get_parser.add_argument("name", help= "Name of the snippet")

    
    arguments = parser.parse_args()
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        name = get(**arguments)
        print("Retrieved snippet: {!r}".format(name))
    
if __name__ == "__main__":
    main()

