<template>
  <div class="container" id="make-predict" v-bind:class="{noStats: borrowUrls.length === 0}">
     <div v-if="borrowUrls.length === 0">
        <span class="col-lg-12"><icon name="facebook" class="logo"></icon></span>
        <h2 class="header col-lg-12""> Predict /r/borrow Loan Repayment </h2>
        <div class="row col-lg-12">
            <div class = "input-group">
            <b-form-input v-model="threadUrl" type="text" placeholder="Enter /r/borrow post URL" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
            <span class="input-group-btn">
               <b-btn @click="getUserPrediction" variant="primary" class="predict-submit"><span class="hidden-md-up"><icon name="search"></icon></span><span class="hidden-sm-down">Predict</span></b-btn>
            </span>
            </div>
        </div>
     </div>

     <div v-if="borrowUrls.length > 0" class="hasStats row">
        <div class="col-lg-1 col-md-1 col-sm-2"><icon name="facebook" class="logo-sm"></icon></div>
        <div class="row col-lg-11 col-md-11 col-sm-10" style="height:100%;vertical-align: bottom;">
            <div class = "input-group">
            <b-form-input v-model="threadUrl" type="text" placeholder="Enter /r/borrow post URL" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
            <span class="input-group-btn">
               <b-btn @click="getUserPrediction" variant="primary" class="predict-submit"><span class="hidden-md-up"><icon name="search"></icon></span><span class="hidden-sm-down">Predict</span></b-btn>
            </span>
            </div>
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
  padding: 40px;
}

#make-predict{
  min-height: 100vh;

}

.noStats{
  display: flex;
  flex-direction: column;
  justify-content: center;
}

input{
  border-radius:0px;
  border-color: white white #E0E0E0 white;
}

input:focus{
  border-color: white white red white;
}

.hideTitle{
  display:none;
}

button{
  border-radius:0px;
}

.logo{
  width: 100%;
  height: 8em;
}

.logo-sm{
  width: 100%;
  height: 3em;
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

