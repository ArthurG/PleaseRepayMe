import praw
from pprint import pprint 
from .settings import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD
import datetime
import pickle
from sklearn import externals
import pandas as pd
import numpy as np

def retreive_data(username):
  r = praw.Reddit(user_agent='TwoKate | https://github.com/guoarthur/reddit-queries',
      client_id=CLIENT_ID, client_secret=CLIENT_SECRET, 
      username=USERNAME, password=PASSWORD)
  user = r.redditor(username)

  #Get the users comments per subreddit
  sub_comments = {}
  for comment in user.comments.new(limit=None):
    #pprint(vars(comment))
    sub_name = comment.subreddit.display_name
    sub_comments[sub_name] = sub_comments.get(sub_name, 0) + 1

  sub_posts = {}
  for comment in user.submissions.new(limit=None):
    #pprint(vars(comment))
    sub_name = comment.subreddit.display_name
    sub_posts[sub_name] = sub_posts.get(sub_name, 0) + 1
  #Get the users post per subreddit

  count_by_time = {}
  get_count_data(count_by_time, user.comments.new(limit=None), "comm")
  get_count_data(count_by_time, user.submissions.new(limit=None), "posts")

  return count_by_time, sub_comments, sub_posts

def predict(username):
  return predict_user_repayment2( retreive_data( username ) [1] )[0].item()

def get_user_from_thread_url(thread_url):
  r = praw.Reddit(user_agent='TwoKate | https://github.com/guoarthur/reddit-queries',
      client_id=CLIENT_ID, client_secret=CLIENT_SECRET, 
      username=USERNAME, password=PASSWORD)
  submission = r.submission(url=thread_url)
  return submission.author.name

def predict_user_repayment(data):
  col = pickle.load( open("app/prediction/sk2col.pkl", "rb"))
  df = pd.DataFrame([data], columns=col)
  df.fillna(0, inplace=True)
  test_item = np.array(df)
  clf = externals.joblib.load('app/prediction/predictor2.pkl')
  return clf.predict(test_item)


def predict_user_repayment2(data):
  col = pickle.load( open("app/prediction/sk1col.pkl", "rb"))
  df = pd.DataFrame([data], columns=col)
  df.fillna(0, inplace=True)
  test_item = np.array(df)
  clf = externals.joblib.load('app/prediction/predictor.pkl')
  return clf.predict(test_item)


  

def get_count_data(count_by_time, iter_items, pref):
  #TODO Upgrade num_comm_lst_wk to num_comm_1_wk

  one_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).timestamp()
  two_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=14)).timestamp()
  three_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=21)).timestamp()
  four_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=28)).timestamp()
  two_mt = (datetime.datetime.utcnow() - datetime.timedelta(days=58)).timestamp()
  three_mt = (datetime.datetime.utcnow() - datetime.timedelta(days=88)).timestamp()
  six_mt = (datetime.datetime.utcnow() - datetime.timedelta(days=6*30)).timestamp()

  for item in iter_items:
    ct = int(item.created_utc)
    if(ct > one_wk):
      count_by_time["num_"+pref+"_last_wk"] =  count_by_time.get("num_"+pref+"_last_wk", 0) + 1
    elif(ct > two_wk):
      count_by_time["num_"+pref+"_2_wk"] =  count_by_time.get("num_"+pref+"_2_wk", 0) + 1
    elif(ct > three_wk):
      count_by_time["num_"+pref+"_3_wk"] =  count_by_time.get("num_"+pref+"_3_wk", 0) + 1
    elif(ct > four_wk):
      count_by_time["num_"+pref+"_4_wk"] =  count_by_time.get("num_"+pref+"_4_wk", 0) + 1
    elif(ct > two_mt):
      count_by_time["num_"+pref+"_2_mth"] =  count_by_time.get("num_"+pref+"_2_mth", 0) + 1
    elif(ct > three_mt):
      count_by_time["num_"+pref+"_3_mth"] =  count_by_time.get("num_"+pref+"_3_mth", 0) + 1
    elif(ct > six_mt):
      count_by_time["num_"+pref+"_6_mth"] =  count_by_time.get("num_"+pref+"_6_mth", 0) + 1

#print( predict_user_repayment_thread("https://www.reddit.com/r/borrow/comments/4cmsp5/req_400_oxford_ohio_usa_15_on_515_paypal/") )
