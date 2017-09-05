<template>
  <div class="wrapper">
    <footer class="container">
    <h2 class="bot-header"> PleaseRepay.me - Data-driven lending</h2>
    <p class="bot-content">
        <span class="bot-links">
            <a v-on:click="openAbout"> About </a> | 
            <a v-on:click="openTos"> Terms of Service </a>
        </span>
        <br/>
        <span class="tos-agreement">
            By using this site, I agree to be bound by the Term of Service
         </span>
    </p>

    <p class="bot-icons">

        <a href="https://github.com/guoarthur/PleaseRepayMe"><icon name="github"></icon> </a>

        <a v-on:click="openPending"><icon name="envelope"></icon></a>
    </p>
    <p class="bot-copy">
        Copyright 2017, Made with <span class="highlight"><3</span>
    </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'BotNav',
  methods: {
    openTos () {
      this.$root.$emit('show::modal', 'modal-tos')
    },
    openAbout () {
      this.$root.$emit('show::modal', 'modal-about')
    },
    openPending () {
      this.$root.$emit('show::modal', 'modal-coming-soon')
    }
  }
}
</script>

<style scoped>
.wrapper{
  background-color: #9e9e9e;
  color: #f5f5f5;
  padding: 1em;
}

.bot-header{
  margin: 1em;
}

.bot-content{
  margin: 1em;
}

.bot-links{
  font-size:1.35em;
}

.tos-agreement{
  font-size: 0.75em;
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
