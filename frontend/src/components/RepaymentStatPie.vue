<script>
import { Pie } from 'vue-chartjs'

export default Pie.extend({
  props: ['userProb', 'isFirst'],
  mounted () {
    this.render()
  },
  watch: {
    userProb () {
      this.render()
    }
  },
  methods: {
    render () {
      this.renderChart({
        labels: ['Unpaid', 'Repay', 'No Lender Found'],
        datasets: [
          {
            backgroundColor: ['#FF5722', '#2194F3', '#9e9e9e'],
            data: this.userProb
          }
        ]
      }, {
        maintainAspectRatio: true,
        responsive: true,
        animation: this.isFirst ? { duration: 1500 } : false
      })
    }
  }
})
</script>
