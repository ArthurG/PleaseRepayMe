import numpy as np
import pandas as pd
import json
from glob import glob
import pickle

from sklearn import svm, preprocessing, model_selection, externals

def train():
  lines = []
  for f_name in glob('/mnt/3F5127B6515F1249/reddit/linked_with_comments/part-00*'):
     f = open(f_name, 'r')
     lines.extend(f.read().split("\n")[:-1])
  df = pd.DataFrame.from_records(map(json.loads, lines))
  df.drop(["borrower", "author", "currency", "lender","repaid_thread_body","repaid_thread_id","repaid_thread_name","repaid_thread_start_date", "repaid_thread_title"], 1,inplace=True)
  df.fillna(0, inplace=True)

  df["repaid"] = df["repaid"].map(lambda x: 1 if x == "true" else 0)

  columns = df.drop("repaid", 1).columns.tolist()
  pickle.dump(columns, open("sk1col.pkl", "wb"))

  X = np.array(df.drop("repaid", 1))
  y = np.array(df["repaid"])
  print(y.mean())

  X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)


  clf = svm.SVC(kernel='linear', class_weight={1: 1, 0:400})

  clf.fit(X_train, y_train)
  externals.joblib.dump(clf, 'predictor.pkl')
  return X_test, y_test



X_test, y_test = train()
clf = externals.joblib.load('predictor.pkl')
lines = []
for f_name in glob('/mnt/3F5127B6515F1249/reddit/linked_with_comments/part-00*'):
   f = open(f_name, 'r')
   lines.extend(f.read().split("\n")[:-1])
df = pd.DataFrame.from_records(map(json.loads, lines))
df.drop(["borrower", "author", "currency", "lender","repaid_thread_body","repaid_thread_id","repaid_thread_name","repaid_thread_start_date", "repaid_thread_title"], 1,inplace=True)
df.fillna(0, inplace=True)

df["repaid"] = df["repaid"].map(lambda x: 1 if x == "true" else 0)

#X_test = np.array(df.drop("repaid", 1))
#y_test = np.array(df["repaid"])

print(clf.score(X_test, y_test))

print((clf.predict(X_test) == 1).sum())
print((clf.predict(X_test) == 0).sum())
print((y_test == 1).sum())

a = pd.DataFrame(data={"pred": clf.predict(X_test), "ans": y_test})

print(len(a.loc[(a["pred"] == 0 ) & (a["ans"] == 1)]))
print(len(a.loc[(a["pred"] == 1 ) & (a["ans"] == 0)]))
