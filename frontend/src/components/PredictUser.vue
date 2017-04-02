<template>
  <div class="container">
        <h2 class="header col-lg-12"> Make predictions </h2>
        <div v-bind:class="{ 'col-lg-8': hasResult, 'col-lg-12': !hasResult}">
          <b-card>
            <b-form-input v-model="threadUrl" type="text" placeholder="Please enter the /r/borrow request link" :state="threadUrl.length?'success':'warning'" class="predict-user-box"></b-form-input>
            <b-btn @click="clicked" variant="primary" class="predict-submit">Make Prediction</b-btn>
          </b-card>
        </div>
        <div v-if="hasResult" v-bind:class="{ 'col-lg-4': hasResult }">
        <b-card>
           <h5> <a v-bind:href="getLink(userName)">/u/{{userName}}</a></h5>
           <p>{{userResult}}</p>
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
    clicked () {
      this.userName = 'arthur'
      this.hasResult = true
      this.userResult = this.threadUrl
      // this.getEndpoint()
    },
    getLink (user) {
      console.log('link ' + user)
      return 'https://www.reddit.com/u/' + user
    },
    getEndpoint () {
      this.$http.get('https://jsonplaceholder.typicode.com').then(resp => {
        console.log(resp)
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

</style scoped>

