<template>
  <div class="wrapper">
  <div class="container" id="stats">
    <h2 class="col-lg-12">Statistics</h2>

    <div class="col-sm-6 col-lg-4">
        <div class="card card-inverse card-primary">
          <div class="card-block pb-0">
            <h4 class="mb-0">{{accuracy}}</h4>
            <p>Prediction Accuracy</p>
          </div>
          <card-line1-chart-example class="chart-wrapper px-1" style="height:70px;" height="70"/>
        </div>
    </div><!--/.col acc-->

    <div class="col-sm-6 col-lg-4">
        <div class="card card-inverse card-primary">
          <div class="card-block pb-0">
            <h4 class="mb-0">{{precision}}</h4>
            <p>Precision</p>
          </div>
          <card-line1-chart-example class="chart-wrapper px-1" style="height:70px;" height="70"/>
        </div>
    </div><!--/.col acc-->

     <div class="col-sm-6 col-lg-4">
        <div class="card card-inverse card-primary">
          <div class="card-block pb-0">
            <h4 class="mb-0">{{recall}}</h4>
            <p>Recall</p>
          </div>
          <card-line1-chart-example class="chart-wrapper px-1" style="height:70px;" height="70"/>
        </div>
    </div><!--/.col acc-->




  </div>

    </div>
</template>

<script>

import CardLine1ChartExample from './CardLine1ChartExample'

export default {
  name: 'DashBoard',
  data () {
    return {
      accuracy: -1,
      precision: -1,
      recall: -1
    }
  },
  components: {
    CardLine1ChartExample
  },
  methods: {
    getStatistics () {
      this.$http.get('http://localhost:5000/statistics').then(resp => {
        console.log(resp.body)
        this.accuracy = resp.body.accuracy
        this.precision = resp.body.precision
        this.recall = resp.body.recall
      }, err => {
        console.log(err)
      })
    }
  },
  mounted () {
    this.getStatistics()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h2{
  color: white;
}

.container{
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 20px;
}

.wrapper{
    background: black;
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
