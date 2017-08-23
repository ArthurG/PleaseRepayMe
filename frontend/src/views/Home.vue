<template>
    <div class="hello">
      <HomeContent></HomeContent>
      <BotNav></BotNav>
      <Legal></Legal>
      <Modals></Modals>
    </div>
</template>

<script>
  import HomeContent from './../components/HomeContent'
  import BotNav from './../components/BotNav'
  import Legal from './../components/Legal'
  import Modals from './../components/Modals'

  export default {
    name: 'HomeView',
    components: {
      HomeContent,
      BotNav,
      Legal,
      Modals
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
