<template>
  <div class="container" id="make-predict" v-bind:class="{noStats: borrowUrls.length === 0}">
     <div v-if="borrowUrls.length === 0">
        <span class="col-lg-12"><img src="../assets/logo.svg" class="logo"></span>
        <h2 class="header col-lg-12"> Predict /r/borrow Loan Repayment </h2>
        <div class="row">
            <form class="col-lg-12" v-on:submit.prevent="getUserPrediction">
                <div class = "input-group predict-user-group">
                    <b-form-input v-model="threadUrl" type="text" placeholder="Enter /r/borrow post URL" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
                    <span class="input-group-btn">
                       <b-btn type="submit"  variant="primary" class="predict-submit"><span class="hidden-md-up"><icon name="search"></icon></span><span class="hidden-sm-down">Predict</span></b-btn>
                    </span>
                </div>
            </form>
        </div>
     </div>

     <div v-if="borrowUrls.length > 0" class="hasStats row">
        <div class="col-lg-1 col-md-1 col-sm-2"><img src="../assets/logo.svg" class="logo-sm"></div>
        <div class="row col-lg-11 col-md-11 col-sm-10" style="height:100%;vertical-align: bottom;">
            <form class="col-lg-12" v-on:submit.prevent="getUserPrediction">
                <div class = "input-group predict-user-group">
                    <b-form-input v-model="threadUrl" type="text" placeholder="Enter /r/borrow post URL" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
                    <span class="input-group-btn">
                       <b-btn type="submit" variant="primary" class="predict-submit"><span class="hidden-md-up"><icon name="search"></icon></span><span class="hidden-sm-down">Predict</span></b-btn>
                    </span>
                </div>
            </form>
        </div>
    </div>
        
    <UserStatCards :RedditBorrowUrls="{borrowUrls}" />
  </div>
</template>

<script>

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
    UserStatCards
  },
  methods: {
    getLink (user) {
      return 'https://www.reddit.com/u/' + user
    },
    getUserPrediction () {
      this.borrowUrls.push(this.threadUrl)
      this.threadUrl = ''
    }
  }
}
</script>

<style scoped>



.container{
  padding: 40px;
}

.header{
  font-family: 'Nunito Sans', sans-serif;
  font-weight: 700;
}

#make-predict{
  min-height: 100vh;

}

.noStats{
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.predict-user-group{
  vertical-align:middle;
}

.predict-user-box{
  font-family: 'Nunito Sans', sans-serif;
  font-weight: 700;
  border-radius:0px;
  border-color: white white #E0E0E0 white;
  margin-right: 0.75em;
  padding: 0 0.5em;
}

.predict-user-box:focus{
  border-color: white white red white;
}

button{
  font-family: 'Nunito Sans', sans-serif;
  font-weight: 900;
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

</style scoped>

