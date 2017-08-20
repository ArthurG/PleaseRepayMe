<template>
  <div>
     <div v-if="showSplashScreen">
        <span class="col-lg-12">
            <img src="../assets/Logo.png" class="logo-big">
        </span>
        <h2 class="header col-lg-12"> 
            Predict /r/borrow Loan Repayment 
        </h2>
        <div class="row">
            <form class="col-lg-12" v-on:submit.prevent="getUserPrediction">
                <div class = "input-group predict-user-group">
                    <b-form-input v-model="threadUrl" type="text" placeholder="Enter /r/borrow post URL" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
                    <span class="input-group-btn">
                       <b-btn type="submit"  variant="primary" class="predict-submit">
                           <span class="hidden-md-up">
                               <icon name="search"></icon>
                           </span>
                           <span class="hidden-sm-down">
                              Predict
                           </span>
                       </b-btn>
                    </span>
                </div>
            </form>
        </div>
     </div>

     <div v-else class="hasStats row top-nav-bar">
        <div class="col-lg-1 col-md-1 col-sm-2">
            <img src="../assets/Logo.png" class="logo-sm">
        </div>
        <div class="row col-lg-11 col-md-11 col-sm-10">
            <form class="col-lg-12" v-on:submit.prevent="getUserPrediction">
                <div class = "input-group predict-user-group">
                    <b-form-input v-model="threadUrl" type="text" placeholder="Enter /r/borrow post URL" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
                    <span class="input-group-btn">
                       <b-btn type="submit" variant="primary" class="predict-submit">
                          <div v-if="inProgress">
                             <pulse-loader :color="color"></pulse-loader>
                          </div>
                          <div v-else>
                             <span class="hidden-md-up">
                                <icon name="search"></icon>
                             </span>
                             <span class="hidden-sm-down">
                                Predict
                             </span>
                          </div>
                       </b-btn>
                    </span>
                </div>
            </form>
        </div>
    </div>
  </div>
</template>

<script>
import {mapState, mapGetters} from 'vuex'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'PredictUser',
  data: function () {
    return {
      threadUrl: ''
    }
  },
  methods: {
    getUserPrediction () {
      if (!this.inProgress) {
        let url = this.threadUrl
        this.threadUrl = ''
        this.$store.dispatch('retrievePrediction', {threadUrl: url})
      }
    }
  },
  computed: {
    ...mapGetters({
      showSplashScreen: 'showSplashScreen'
    }),
    ...mapState({
      userData: 'userData',
      inProgress: 'inProgress'
    })
  },
  components: {
    PulseLoader
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

.top-nav-bar{
  margin: 0.5em;

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

.logo-big{
  width: auto;
  height: 10em;
  margin: 3em;
}

.logo-sm{
  width: auto;
  height: 3em;
}
</style>
