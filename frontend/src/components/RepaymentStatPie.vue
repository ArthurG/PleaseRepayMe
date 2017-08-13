<script>
import { Pie } from 'vue-chartjs'

export default Pie.extend({
  props: ['userProb'],
  mounted () {
    this.render()
  },
  watch: {
    userProb: function () {
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
        animation: {
          duration: 1500
        }
      })
    }
  }
})
</script>
