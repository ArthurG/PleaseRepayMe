import praw
from pprint import pprint 
from .settings import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD
import datetime
import pickle
from sklearn import externals
import pandas as pd
import numpy as np
def get_user_from_thread_url(thread_url):
  r = praw.Reddit(user_agent='BorrowR | https://github.com/guoarthur/reddit-queries',
      client_id=CLIENT_ID, client_secret=CLIENT_SECRET, 
      username=USERNAME, password=PASSWORD)
  submission = r.submission(url=thread_url)
  return submission.author.name

def get_predictive_data(username):
  r = praw.Reddit(user_agent='BorrowR | https://github.com/guoarthur/reddit-queries',
      client_id=CLIENT_ID, client_secret=CLIENT_SECRET, 
      username=USERNAME, password=PASSWORD)
  user = r.redditor(username)

  #Look through users [REQ] submissions, figure out how many were confirmed
  req_items = [submission 
               for submission in user.submissions.new(limit=None) 
               if (submission.title.upper().startswith("[REQ]") and submission.subreddit.display_name == "borrow")]
  num_borrow = 0
  for req in req_items:
    foundLender = 0
    for com in req.comments:
      if("$loan" in com.body):
        foundLender += 1
    if foundLender > 0:
      num_borrow += 1

  #Get the users post per subreddit
  predictive_data = {}
  get_count_data(predictive_data, user.comments.new(limit=None), "comm")
  get_count_data(predictive_data, user.submissions.new(limit=None), "posts")
  predictive_data["num_borrow"] = num_borrow
  predictive_data["num_req"] = len(req_items)
  predictive_data["pct_fulfilled"] = num_borrow/len(req_items)

  return predictive_data

#Liklihood of default/repayment
#return (prediction, [proba_default, proba_repay])
def predict_user_repayment2(data):
  col = pickle.load( open("app/prediction/sk2col.pkl", "rb"))
  df = pd.DataFrame([data], columns=col)
  #print(df.head())
  df.fillna(0, inplace=True)
  test_item = np.array(df)
  clf = externals.joblib.load('app/prediction/predictor2.pkl')
  return clf.predict(test_item), clf.predict_proba(test_item)

#Helper function, counts the number of submissions/comments within the last wk/2wk/month/etc
#mutates count_by_time, no return value
def get_count_data(count_by_time, iter_items, pref):
  #TODO Upgrade num_comm_lst_wk to num_comm_1_wk

  one_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).timestamp()
  two_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=14)).timestamp()
  three_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=21)).timestamp()
  four_wk = (datetime.datetime.utcnow() - datetime.timedelta(days=28)).timestamp()
  two_mt = (datetime.datetime.utcnow() - datetime.timedelta(days=58)).timestamp()
  three_mt = (datetime.datetime.utcnow() - datetime.timedelta(days=88)).timestamp()
  six_mt = (datetime.datetime.utcnow() - datetime.timedelta(days=6*30)).timestamp()
  one_yr = (datetime.datetime.utcnow() - datetime.timedelta(days=365)).timestamp()

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

    if(ct > one_yr):
      count_by_time["num_"+pref+"_last_year"] =  count_by_time.get("num_"+pref+"_last_year", 0) + 1

#Unused function, untested
def ret_data_2(username):
  #Get the users comments per subreddit
  sub_comments = {}
  for comment in user.comments.new(limit=None):
    sub_name = comment.subreddit.display_name
    sub_comments[sub_name] = sub_comments.get(sub_name, 0) + 1
  sub_posts = {}
  for comment in user.submissions.new(limit=None):
    sub_name = comment.subreddit.display_name
    sub_posts[sub_name] = sub_posts.get(sub_name, 0) + 1

#Unused, don't touch
def predict_user_repayment(data):
  col = pickle.load( open("sk1col.pkl", "rb"))
  df = pd.DataFrame([data], columns=col)
  df.fillna(0, inplace=True)
  test_item = np.array(df)
  clf = externals.joblib.load('predictor1.pkl')
  return clf.predict(test_item)



#print( predict_user_repayment_thread("https://www.reddit.com/r/borrow/comments/4cmsp5/req_400_oxford_ohio_usa_15_on_515_paypal/") )
#print(predict_user_repayment2(get_predictive_data("Throwaway_Luck")))
