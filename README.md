# PleaseRepay.me

## So you think you know what makes a good borrower?

Well, at least 300 Redditors stole some money from lenders on /r/borrow. 

### What it does

Having seen more than 12,000 loan requests, [www.reddit.com/r/borrow/](http://reddit.com/r/borrow/) holds a ton of information on what types of Redditors are trustworthy. [PleaseRepay.me](http://pleaserepay.me/) seeks to capitalize on this information, and use it to predict the outcome of a given loan. 

### How it's done

We categorize all "[REQ]" threads on /r/borrow into three buckets:

* Repaid
* Unpaid
* Loan Unfulfilled (No lender willing to give a loan) 

 Using a process known as [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning), we analyzed [REQ]uesters for more than 30 characteristics. We asked the question: If a user has a certain characteristic, does it correlate to the user being in a certain bucket?

After taking note of the characteristics that correlate with each bucket, we can predict what bucket any old Redditor belongs to. 

### Why it's awesome

 Our algorithm is quite good at predicting outcomes, with an [F1 Score](https://en.wikipedia.org/wiki/F1_score) of more than 95%. 

### Other stuff

 Special shoutout goes to /u/Stuck_In_the_Matrix for providing the data for this project! 

* * *

## Running it locally

Create a file `backend/app/prediction/settings.py` with variables `CLIENT_ID`, `CLIENT_SECRET`, `USERNAME`, `PASSWORD` corresponding to your Reddit API settings

Installing Dependancies
    
    brew install redis
    redis-server
    
    // In another tab
    cd frontend
    npm install 
    bash rebuild
    cd ../backend
    pip3 install -r requirements.txt

Launching the app

    cd ../frontend
    bash rebuild.sh
    cd ../backend
    python3 manage.py runsever


