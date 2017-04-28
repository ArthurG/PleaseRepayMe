<template>
  <div class="container" id="make-predict">
        <h2 class="header col-lg-12"> Predict /r/borrow Loan Repayment </h2>
        <div class="row col-lg-12">
            <div class = "input-group">
            <b-form-input v-model="threadUrl" type="text" placeholder="Enter /r/borrow post URL" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
            <span class="input-group-btn">
               <b-btn @click="getUserPrediction" variant="primary" class="predict-submit"><span class="hidden-md-up"><icon name="search"></icon></span><span class="hidden-sm-down">Predict</span></b-btn>
            </span>
            </div>
        </div>
        
        <UserStatCards :RedditBorrowUrls="{borrowUrls}" />
  </div>
</template>

<script>

import BorrowStatBar from './BorrowStatBar'
import UserStatCards from './UserStatCard'

export default {
  name: 'PredictUser',
  data () {
    return {
      threadUrl: '',
      borrow: 'https://www.reddit.com/r/uwaterloo/comments/67ynix/this_description_about_the_virginia_tech_logo_on/',
      borrowUrls: []
    }
  },
  components: {
    BorrowStatBar,
    UserStatCards
  },
  methods: {
    getLink (user) {
      return 'https://www.reddit.com/u/' + user
    },
    getUserPrediction () {
      this.borrowUrls.push(this.threadUrl)
    }

  }
}
</script>

<style scoped>
.container{
  border: 2px solid red;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 20px;
}

input{
  border-radius:0px;
  border-color: white white #E0E0E0 white;
}

input:focus{
  border-color: white white red white;

}

button{
  border-radius:0px;
}

.risk{
  background-color: red;
  border: 2px solid black;
}

.bar-risk{
  background-color: red;
  min-height: 10px;
}
.bar-safe{
  background-color: blue;
  min-height: 10px;
}

</style scoped>

