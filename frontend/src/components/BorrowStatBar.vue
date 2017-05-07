<script>
import { Bar } from 'vue-chartjs'

const brandPrimary = '#2194F3'

export default Bar.extend({
  props: ['userBorrowData'],
  mounted () {
    this.render()
  },
  watch: {
    userBorrowData: function () {
      this.render()
    }
  },
  methods: {
    render () {
      this.renderChart({
        labels: ['REQ count', 'REQ Fulfilled'],
        datasets: [
          {
            backgroundColor: brandPrimary,
            data: this.userBorrowData

          }
        ]
      }, {
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          xAxes: [{
            gridLines: {
              display: false
            },
            ticks: {
              fontColor: '#9e9e9e' // this here
            }
          }],
          yAxes: [{
            gridLines: {
              display: false
            },
            ticks: {
              fontColor: '#9e9e9e' // this here
            }
          }]}
      })
    }
  }
})
</script>
