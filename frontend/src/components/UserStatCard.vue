<template>
    <div class="row col-lg-12">
        <div class="col-lg-6 user-card" v-for="user in userDetails">
            <b-card :header="user.name">
              <div v-if="user.hasResult">

                  <div class="borrow-statistics card-section">
                      <h5>/r/borrow Statistics</h5>
                      <borrow-stat-bar :userBorrowData="user.userBorrowData" class="chart-wrapper px-1" height="90"/>
                  </div>

                  <div class="repayment-prediction card-section">
                      <h5>Repayment Prediction</h5>
                      <div class="bar-risk">
                          <div class="bar-safe" style="width: {user.width}%">
                              {{user.prob}}
                          </div>
                      </div>
                  </div>

              </div>
              <div v-else>
                  <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
              </div>
           </b-card>
        </div>

       <b-modal id="modal1" title="Error Retrieving Prediction" hide-footer="true" >
          <p>
             Your URL is likely invalid, or Reddit servers are down. Please try again.
          </p>
       </b-modal>

       <b-modal id="modal2" title="Request not processed" hide-footer="true" >
          <p>
             Statistics were previously retrieved for that user. In an effort to save computing power, that request was not processed. Please look in your current results to get the repayment liklihood instead.
          </p>
       </b-modal>
    </div>
</template>

<script>

import BorrowStatBar from './BorrowStatBar'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  props: ['RedditBorrowUrls'],
  name: 'UserStatCard',
  data () {
    return {
      userDetails: [],
      pastUrls: [],
      pastLength: 0
    }
  },
  components: {
    BorrowStatBar,
    PulseLoader
  },
  watch: {
    RedditBorrowUrls: function (newUrl) {
      var diff = newUrl.borrowUrls.filter(x => this.pastUrls.indexOf(x) < 0)

      // Process new request
      diff.forEach((url) => {
        this.addUserDetails(url)
        this.pastUrls.push(url)
      })

      // Request not processed since it's duplicate
      if (newUrl.borrowUrls.length > this.pastLength && diff.length === 0) {
        this.$root.$emit('show::modal', 'modal2')
      }
      this.pastLength = newUrl.borrowUrls.length
    }
  },
  methods: {
    getLink (user) {
      return 'https://www.reddit.com/u/' + user
    },
    addUserDetails (url) {
      var item = {hasResult: false}
      this.userDetails.unshift(item)
      this.$http.get('http://localhost:5000/predict?thread_url=' + url).then(resp => {
        item.name = resp.body.user
        item.prob = resp.body.prediction
        item.width = resp.body.prediction * 100 - 10
        item.userBorrowData = [1, 2, 3]
        item.hasResult = true
      }, () => {
        var idx = this.userDetails.indexOf(item)
        this.userDetails.splice(idx, 1)
        this.$root.$emit('show::modal', 'modal1')
      })
    }
  }
}
</script>

<style scoped>

.bar-risk{
  background-color: #FF5722;
  min-height: 10px;
}
.bar-safe{
  background-color: #2196F3;
  min-height: 10px;
}

.card{
  margin: 1em 0;
}

.card-header{
  background-color: #BBDEFB;
  font-size: 3em;
}

.card-section{
  padding: 1em 0;

}

</style scoped>

