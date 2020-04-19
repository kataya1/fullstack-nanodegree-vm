# "Database code" for the DB Forum.

import datetime
import psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]


def get_posts():
  """Return all posts from the 'database', most recent first."""
  connection = psycopg2.connect("dbname=forum")
  cursor = connection.cursor()
  cursor.execute("select content, time from posts order by time desc;")
  posts = list(cursor.fetchall())
  connection.close()
  return posts
  


def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  connection = psycopg2.connect("dbname=forum")
  cursor = connection.cursor()
   
  cursor.execute("insert into posts values (%s);", (content,))
  connection.commit()
  connection.close()
  # POSTS.append((content, datetime.datetime.now()))


