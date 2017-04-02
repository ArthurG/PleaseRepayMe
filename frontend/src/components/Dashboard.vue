<template>
  <div class="container" id="about">
    <h1 class="col-lg-12">Statistics</h1>

    <div class="col-sm-6 col-lg-6">
        <div class="card card-inverse card-primary">
          <div class="card-block pb-0">
            <h4 class="mb-0">9.823</h4>
            <p>Prediction Accuracy</p>
          </div>
          <card-line1-chart-example class="chart-wrapper px-1" style="height:70px;" height="70"/>
        </div>
      </div><!--/.col-->


      </div>
    </div>

  </div>
</template>

<script>

import CardLine1ChartExample from './CardLine1ChartExample'

export default {
  name: 'DashBoard',
  components: {
    CardLine1ChartExample
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.container{
  border: 1px solid black;
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
