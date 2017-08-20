<template>
  <div class="container" id="make-predict" v-bind:class="{noStats: showSplashScreen}">
    <PredictUser></PredictUser>
    <UserStatCard></UserStatCard>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import PredictUser from './PredictUser'
import UserStatCard from './UserStatCard'

export default {
  components: {
    PredictUser,
    UserStatCard
  },
  computed: mapGetters([
    'showSplashScreen'
  ])
}
</script>

<style scoped>
#make-predict{
  min-height: 100vh;
}

.noStats{
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
