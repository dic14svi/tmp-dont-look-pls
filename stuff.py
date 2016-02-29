
from dbapi import Database



dbapi = Database()

boards = [Board(name) for name in dbapi.boards()]

threads = [Thread(id, title, text, board) for (id, title, text, board) in dbapi.threads()]

posts = [Post(id, text, thread_id) for (id, text, thread_id) in dbapi.posts()]




