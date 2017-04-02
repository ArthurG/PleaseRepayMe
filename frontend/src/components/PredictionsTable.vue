<template>
  <div class="container" id="PredictionsTable">
      <h2 class="header col-lg-12"> Past predictions </h2>
      <div class="justify-content-centermy-1 row col-12">
        <b-form-fieldset horizontal label="Rows per page" class="col-md-6 col-sm-12" :label-size="6">
          <b-form-select :options="[{text:5,value:5},{text:10,value:10},{text:15,value:15}]" v-model="perPage">
          </b-form-select>
        </b-form-fieldset>

        <b-form-fieldset horizontal label="Filter" class="col-md-6 col-sm-12" :label-size="2">
          <b-form-input v-model="filter" placeholder="Type to Search"></b-form-input>
        </b-form-fieldset>
        <b-btn class="refresh-btn">Hi</b-btn>
      </div>

      <!-- Main table element -->
      <b-table striped hover :items="transactions" :fields="fields" :current-page="currentPage" :per-page="perPage" :filter="filter">
         <template slot="borrower_name" scope="item">
            <a v-bind:href="item.item.original_thread_url">{{item.item.borrower_name}}</a>
         </template>
         <template slot="lender_name" scope="item">
            <a v-bind:href="item.item.lender_comment_url">{{item.item.lender_name}}</a>
         </template>
         <template slot="status" scope="item">
            <a v-bind:href="item.item.settle_thread_url">{{item.item.status}}</a>
         </template>
      </b-table>

      <div class="justify-content-center row my-1">
        <b-pagination size="md" :total-rows="this.transactions.length" :per-page="perPage" v-model="currentPage" />
      </div>
  </div>
</template>

<script>
export default {
  name: 'PredictionsTable',
  data () {
    return {
      'transactions': [],
      fields: {
        transaction_id: {
          label: 'id',
          sortable: true
        },
        borrower_name: {
          label: 'Borrower Name',
          sortable: true
        },
        lender_name: {
          label: 'Lender Name'
        },
        date_requested: {
          label: 'Date Requested',
          sortable: true
        },
        repayment_probability: {
          label: 'Repayment Probability',
          sortable: true
        },
        status: {
          label: 'Status',
          sortable: true
        }
      },
      currentPage: 1,
      perPage: 10,
      filter: null
    }
  },
  methods: {
    getTransactions () {
      this.$http.get('http://localhost:5000/transactions').then(resp => {
        this.transactions = resp.body.transactions
      }, err => {
        console.log(err)
      })
    }
  },
  mounted () {
    this.getTransactions()
  }

}
</script>

<style scoped>

.container{
  border: 4px solid purple;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  padding: 20px;
}

.phone{
  flex: 1;
  height: 100%;
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

.refresh-btn{
    float: right;
}


</style>
}

