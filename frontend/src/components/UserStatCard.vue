<template>
    <div class="row col-lg-12">
        <div class="col-lg-6" v-for="user in userDetails" >
          <div class="user-card">
          <a class="card-link" v-bind:href="user.url">
            <div>
              <div class="user-card-header">
                 {{user.name}}
              </div>
              <div v-if="user.hasResult">
                  <div class="borrow-statistics user-card-section">
                      <h5 class="user-card-subheader">/r/borrow Statistics</h5>
                      <borrow-stat-bar :userBorrowData="user.userBorrowData" class="chart-wrapper px-1" height="90"/>
                  </div>
                  <div class="repayment-prediction user-card-section">
                      <h5 class="user-card-subheader">Repayment Prediction</h5>
                      <div class="bar-risk">
                          <div class="bar-safe" v-bind:style="user.width">
                              {{user.prob}}
                          </div>
                      </div>
                  </div>
              </div>
              <div v-else class="user-card-empty">
                  <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
              </div>
            </div>
          </a>
          </div>
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
        item.url = url
        item.name = '/u/' + resp.body.user
        item.prob = resp.body.prediction
        item.width = 'width: ' + (resp.body.prediction * 100).toString() + '%'
        item.userBorrowData = [resp.body.num_req, resp.body.num_borrow, 0]
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
  color: #f5f5f5;
  text-align: center;
  padding-left: 0.5em;
}

.card-link{
  color: black;
  text-decoration: none;
}

.user-card-empty{
  text-align: center;
}

.user-card{
  text-align: left;
  margin: 1em 0;
  border: 1px solid #eeeeee;
}

.user-card:hover{
  margin: 0.5em 0;
}
.user-card-header{
  font-size: 1.5em;
  font-weight: 600;
  margin: 0.5em;
  color: #616161;
}
.user-card-section{
  margin: 1em;
}
.user-card-subheader{
  font-weight: 300;
  font-size: 0.9em;
  color: #9e9e9e;
}

</style scoped>
