<template>
  <div class="container" id="about">
    <div class="phone col-lg-4 col-md-6">
      <img src="../assets/reddit.png" class="reddit-screen">
    </div>
    <div class="ad-detail col-lg-8 col-md-6">
      <div class="ad-detail-text">
        <h1>Borrow Project</h1>
        <p><a href="#" class="learn-more">Learn More</a>How do we bring credit scores to the 21st century?</p>
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
  border: 1px solid red;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 20px;
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
  color: white;
  background-color: black;
}


</style>
