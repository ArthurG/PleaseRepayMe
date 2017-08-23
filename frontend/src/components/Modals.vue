<template>
    <div>
      <b-modal id="modal-coming-soon" title="Coming soon!" hide-footer>
        <p>
           This feature is not available at the moment. Please check back soon!
        </p>
      </b-modal>

       <b-modal id="modal-about" title="About" hide-footer>

        <p class="summary">
 TL;DR: We use <a href="https://en.wikipedia.org/wiki/Machine_learning">Machine Learning</a> to predict loan outcomes on Reddit's /r/borrow. Our algorithm is quite good at predicting loan outcomes. We would love for you to try it out!
        </p>

        <hr/>
        <h3 class="info">
So you think you know what makes a good borrower? 
        </h3>
        <h6 class="info">
Well, at least 300 Redditors don't.
        </h6>

        <p class="info">
Having facilitated more than 9000 loans, <a href="http://reddit.com/r/borrow/">www.reddit.com/r/borrow/</a> holds a ton of information on what makes a Redditor trustworthy (read: not a scammer on /r/borrow and is likely to repay their loans). PleaseRepay.me seeks to capitalize on this information, and use it to predict the outcome of a loan. 
        </p>
        <p class="info"> 
We categorize all "[REQ]" on /r/borrow into three buckets:
          <ul>
              <li> Repaid </li>
              <li> Unpaid </li>
              <li> Loan Unfulfilled (No lender willing to give a loan) </li>
          </ul>
        </p>
        <p class="info">
Using a process known as <a href="https://en.wikipedia.org/wiki/Machine_learning">Machine Learning</a>, we analyzed [REQ]uesters for more than 30 characteristics. We asked the question: If a user has a certain characteristic, does it correlate to the user being in a certain bucket? </p>
        <p class="info">
After taking note of the characteristics that correlate with each bucket, we can predict what bucket any old Redditor belongs to. 
        </p>
        <p class="info"> 
Our algorithm is quite good at predicting outcomes, with an <a href="https://en.wikipedia.org/wiki/F1_score">F1 Score</a> of more than 95%.  
        </p>
        <p class="info"> 
Special shoutout goes to <a href="https://www.reddit.com/user/Stuck_In_the_Matrix"> /u/Stuck_In_the_Matrix </a> for providing the data for this project!
        </p>
        <h5>
Try it out! It's pretty cool :)
        </h5>
      </b-modal>
    </div>
</template>

<script>
  export default{
    name: 'Modals'
  }
</script>


<style scoped>

h3, p, h5{
  margin: 1.5em 0.6em;
}

.info {
  text-align: left;
}

hr {
  margin: 2.5em;

}

h3, h5{
  font-weight: 600;
}

</style>

<style>

  #modal-about>.modal-dialog {
    max-width: 800px !important;
    width: 95%;
  }

</style>

