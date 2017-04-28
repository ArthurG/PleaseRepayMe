<script>
import { Bar } from 'vue-chartjs'

const brandPrimary = '#20a8d8'

export default Bar.extend({
  props: ['userBorrowData'],
  mounted () {
    console.log(this.userBorrowData)
    this.renderChart({
      labels: ['REQ count', 'REQ Fulfilled', 'Repaid count'],
      datasets: [
        {
          backgroundColor: brandPrimary,
          borderColor: 'rgba(255,255,255,.55)',
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
          display: true,
          ticks: {
            fontColor: '#CCC'
          }
        }],
        yAxes: [{
          display: true,
          ticks: {
            display: true,
            fontColor: '#CCC'
          }
        }]
      },
      elements: {
        line: {
          borderWidth: 1
        },
        point: {
          radius: 4,
          hitRadius: 10,
          hoverRadius: 4
        }
      }
    })
  }
})
</script>
