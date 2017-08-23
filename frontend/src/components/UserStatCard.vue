<template>
    <div class="row col-lg-12" id="user-cards">
        <div class="col-lg-6" v-for="(user, index) in userDetails" >
            <div class="user-card">
                <div>
                    <div class="user-card-header">
                        {{user.name}} 
                        <a class="thread-link" v-if="user.name" v-bind:href="user.url" target="_blank"> 
                            Link to thread 
                        </a>
                    </div>
                    <div>
                        <div class="borrow-prediction user-card-section">
                            <h5 class="user-card-subheader">Predicted Outcome</h5>
                            <p> 
                                {{user.guessInWords}}
                            </p>
                        </div>

                        <div class="repayment-prediction user-card-section">
                            <h5 class="user-card-subheader">Loan Outcome Probabilities</h5>
                            <repayment-stat-pie :height="150" 
                                                :userProb="user.outcomeLikelihood"
                                                :isFirst="index == 0"/>
                        </div>

                        <div class="borrow-statistics user-card-section">
                            <h5 class="user-card-subheader">/r/borrow Statistics</h5>
                            <borrow-stat-bar :userBorrowData="user.userBorrowData" 
                                             :height="90"
                                             :isFirst="index == 0"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <b-modal id="error-modal" title="Error Retrieving Prediction" :hide-footer="true" @hidden="close">
            <p>
                {{errorMessage}}
            </p>
        </b-modal>
    </div>
</template>

<script>
import BorrowStatBar from './BorrowStatBar'
import RepaymentStatPie from './RepaymentStatPie'
import {mapGetters, mapState} from 'vuex'

export default {
  props: ['RedditBorrowUrls'],
  name: 'UserStatCard',
  methods: {
    close () {
      this.$store.commit('clearError')
    }
  },
  computed: {
    ...mapState({
      inProgress: 'inProgress',
      errorMessage: 'errorMessage'
    }),
    ...mapGetters({
      userDetails: 'userDataRev'
    })
  },
  watch: {
    errorMessage: function () {
      if (this.errorMessage !== '') {
        this.$root.$emit('show::modal', 'error-modal')
      }
    }
  },
  components: {
    BorrowStatBar,
    RepaymentStatPie
  }
}
</script>

<style scoped>

#user-cards .user-card{
  transition:0.5s;
}

#user-cards:hover .user-card{
  opacity: 0.3;
}

#user-cards:hover .user-card:hover{
  opacity: 1;
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

.thread-link{
  font-size: 0.4em;
  color: #9e9e9e;
}

</style scoped>
