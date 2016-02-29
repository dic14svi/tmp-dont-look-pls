
class Database():

	def __init__(self, boards, threads, posts):
		self.boards  = boards
		self.threads = threads
		self.posts   = posts

	def boards():
		cmd = "select name from boards"
		cur = g.db.execute(cmd)
		entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
		return boards

	def threads():
		cmd = "select id from threads"
		return threads()

	def posts():
		cmd = "select post from posts"
		return posts()

