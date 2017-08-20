import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userData: [],
    inProgress: false,
    errorMessage: ''
  },
  mutations: {
    makeQuery (state) {
      state.inProgress = true
    },
    failQuery (state, {errorMessage}) {
      state.inProgress = false
      state.errorMessage = errorMessage
    },
    clearError (state) {
      state.errorMessage = ''
    },
    addUserData (state, {newData}) {
      state.inProgress = false
      state.userData.push(newData)
    }
  },
  getters: {
    userDataRev: state => state.userData.slice().reverse(),
    showSplashScreen: state => state.userData.length === 0 && !state.inProgress
  },
  actions: {
    retrievePrediction (context, {threadUrl}) {
      context.commit('makeQuery')
      Vue.http.get('http://localhost:5000/predict?thread_url=' + threadUrl).then(resp => {
        let item = {}
        item.url = threadUrl
        item.name = '/u/' + resp.body.user
        item.outcomeLikelihood = resp.body.prediction.map(function (x) {
          return x * 100
        })
        item.guess = resp.body.guess
        switch (item.guess) {
          case '0':
            item.guessInWords = 'Default'
            break
          case '1':
            item.guessInWords = 'Repaid'
            break
          case '2':
            item.guessInWords = 'No Lender Found'
            break
          default:
            item.guessInWords = 'Error: No guess found'
        }
        item.userBorrowData = [resp.body.num_req, resp.body.num_borrow]
        context.commit('addUserData', {newData: item})
      }, (resp) => {
        context.commit('failQuery', {errorMessage: resp.body.error})
      })
    }
  },
  strict: true
})
