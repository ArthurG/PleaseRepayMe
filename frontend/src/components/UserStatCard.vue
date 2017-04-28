<template>
    <div class="row col-lg-12">
        <div class="col-lg-6 user-card" v-for="user in userDetails">
            <b-card :header="user.name">
              <div v-if="user.hasResult">
                  <h6>/r/borrow Statistics</h6>
                  <borrow-stat-bar :userBorrowData="user.userBorrowData" class="chart-wrapper px-1" height="90"/>

                  <h6>Repayment Prediction</h6>
                  <div class="bar-risk">
                      <div class="bar-safe" style="width: {user.width}%">
                          {{user.prob}}
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
      pastUrls: []
    }
  },
  components: {
    BorrowStatBar,
    PulseLoader
  },
  watch: {
    RedditBorrowUrls: function (newUrl) {
      newUrl.borrowUrls.forEach((url) => {
        if (this.pastUrls.indexOf(url) === -1) {
          this.addUserDetails(url)
          this.pastUrls.push(url)
        }
      })
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

}

</style scoped>

