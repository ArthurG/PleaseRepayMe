<template>
  <div class="hello">
    <TopNav></TopNav>
    <PredictUser></PredictUser>
    <Footer></Footer>
  </div>
</template>

<script>
import TopNav from './../components/TopNav'
import PredictUser from './../components/PredictUser'
import Footer from './../components/Footer'

export default {
  name: 'hello',
  components: {
    TopNav,
    PredictUser,
    Footer
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
