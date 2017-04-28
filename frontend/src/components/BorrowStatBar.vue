<script>
import { Bar } from 'vue-chartjs'

const brandPrimary = '#2194F3'

export default Bar.extend({
  props: ['userBorrowData'],
  mounted () {
    console.log(this.userBorrowData)
    this.renderChart({
      labels: ['REQ count', 'REQ Fulfilled', 'Repaid count'],
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
      }
    })
  }
})
</script>
