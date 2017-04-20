<template>
  <div class="background-wrapper">
  <div class="container" id="about">
    <div class="ad-detail col-lg-8 col-md-6">
      <div class="ad-detail-text">
        <h1>Borrow Project</h1>
        <p> Reddit history to make lending decisions</p>
        <p><a href="#" class="learn-more">Learn More </a> How do we bring credit scores to the 21st century?</p>
      </div>
    </div>

  </div>
  </div>
</template>

<script>
export default {
  name: 'MainBanner'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.container{
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 20px;
}

.background-wrapper{
  background-image: url("../assets/jumbotron-img.jpg");
  background-repeat:no-repeat;
  background-position: center;
  background-size: contain;
  background-color: black;
}

#about{
  height: 500px;
}

.reddit-screen{
  flex: 1;
  width: 100%;
}
.ad-detail{
  text-align: left;
  padding: auto;
  display: flex;
  display: -webkit-flex;
  display: -ms-flexbox;
  align-items: center;
}

.learn-more{
  color: grey;
  background-color: white;
}

.ad-detail-text{
  color: white;
}


</style>
