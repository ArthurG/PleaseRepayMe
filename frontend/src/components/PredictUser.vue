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
        <div v-if="hasResult" v-bind:class="{ 'col-lg-12': hasResult }">
           <b-card>
              <h5> <a v-bind:href="getLink(userName)">/u/{{userName}}</a></h5>
              <p>Repayment Probability: {{userResult}}</p>
           </b-card>
        </div>
  </div>
</template>

<script>
export default {
  name: 'PredictUser',
  data () {
    return {
      hasResult: false,
      threadUrl: '',
      userName: '',
      userResult: ''
    }
  },
  methods: {
    getLink (user) {
      return 'https://www.reddit.com/u/' + user
    },
    getUserPrediction () {
      this.$http.get('http://localhost:5000/predict?thread_url=' + this.threadUrl).then(resp => {
        console.log(resp.body)
        this.userName = resp.body.user
        this.userResult = resp.body.prediction
        this.hasResult = true
      }, err => {
        console.log(err)
      })
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

</style scoped>

