<script>
import { Pie, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default Pie.extend({
  mixins: [reactiveProp],
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
        maintainAspectRatio: false,
        responsive: true
      })
    }
  }
})
</script>
