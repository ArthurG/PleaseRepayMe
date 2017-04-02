<template>
  <footer class="container">
    <i class="fa fa-facebook-official fa-2x"></i>
    <i class="fa fa-twitter fa-2x"></i>
    <i class="fa fa-envelope fa-2x"></i>
    <p>Privacy | Terms of use</p>
    <p>Copyright 2017</p>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.container{
  border: 2px solid red;
  text-align: left;
  background-color: #a1a1a1;
}

i{
  color: white;
  padding: 0.1em;
  margin: 0.1em 0;
}

p{
  font-size:0.6em;
  padding: 0px;
  margin: 0px;

}


</style>
