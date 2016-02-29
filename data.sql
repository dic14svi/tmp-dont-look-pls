
drop table if exists posts;
create table posts (
	id integer primary key autoincrement,
	text text not null,
	thread integer not null
);

drop table if exists threads;
create table threads (
	id integer primary key autoincrement,
	title text not null,
	op text not null,
	board text not null
);

drop table if exists boards;
create table boards (
	name text not null primary key,
);

threads = [ (thread_id, title, op) ]

posts = [ (id, content, thread_id) ]


function get_threads()
	threads = []
	for thread in threads
		posts_in_thread = []
		for post in posts:
			if post.thread_id == thread.id
				posts_in_thread += post
		thread.add(posts)
		threads += thread
	return threads

