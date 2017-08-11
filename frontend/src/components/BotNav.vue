<template>

  <div class="wrapper">
    <footer class="container">
    <h2 class="bot-header"> Repaid - Data-based lending</h2>
    <p class="bot-links">About | Privacy | <a v-on:click="openTos"> Terms of Service </a></p>
    <p class="bot-icons"><icon name="github"></icon> <icon name="envelope"></icon></p>
    <p class="bot-copy">Copyright 2017, Made with <span class="highlight"><3</span> in Waterloo, Ontario, Canada</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'BotNav',
  methods: {
    openTos () {
      this.$root.$emit('show::modal', 'modal-tos')
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.wrapper{
  background-color: #9e9e9e;
  color: #f5f5f5;
  padding: 1em;
}

.bot-header{
  margin: 1em;
}

.bot-links{
  font-size:1.15em;
  margin: 1em;
}

.fa-icon{
  width: 1.5em;
  height: 100%;
  margin: 0 0.5em;
}

.bot-copy{
  margin: 1em;
  font-size: 0.75em;
}

.highlight{
  color: #FF5722;
}

</style>
