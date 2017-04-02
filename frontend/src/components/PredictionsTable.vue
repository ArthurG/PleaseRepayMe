<template>

<div id="PredictionsTable">
  <div class="justify-content-centermy-1 row">

    <b-form-fieldset horizontal label="Rows per page" class="col-6" :label-size="6">
      <b-form-select :options="[{text:5,value:5},{text:10,value:10},{text:15,value:15}]" v-model="perPage">
      </b-form-select>
    </b-form-fieldset>

    <b-form-fieldset horizontal label="Filter" class="col-6" :label-size="2">
      <b-form-input v-model="filter" placeholder="Type to Search"></b-form-input>
    </b-form-fieldset>
  </div>

  <!-- Main table element -->
  <b-table striped hover :items="items" :fields="fields" :current-page="currentPage" :per-page="perPage" :filter="filter">
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
    <b-pagination size="md" :total-rows="this.items.length" :per-page="perPage" v-model="currentPage" />
  </div>
</div>

</template>

<script>
export default {
  name: 'PredictionsTable',
  data () {
    return {
      'items': [
        {
          'agree_comment_url': 'true',
          'borrower_name': 'arthur',
          'date_requested': 'Sat, 01 Apr 2017 12:18:37 GMT',
          'lender_comment_url': 'google.ca',
          'lender_name': 'andrew',
          'original_thread_url': 'youtube.com',
          'repayment_probability': 1.235,
          'settle_thread_url': 'gsgdfhsdf.ca',
          'status': 1,
          'transaction_id': 1
        },
        {
          'agree_comment_url': 'true',
          'borrower_name': 'arthur',
          'date_requested': 'Sat, 01 Apr 2017 12:18:37 GMT',
          'lender_comment_url': 'google.ca',
          'lender_name': 'andrew',
          'original_thread_url': 'youtube.com',
          'repayment_probability': null,
          'settle_thread_url': 'gsgdfhsdf.ca',
          'status': 1,
          'transaction_id': 2
        },
        {
          'agree_comment_url': 'true',
          'borrower_name': 'arthur',
          'date_requested': 'Sat, 01 Apr 2017 12:18:37 GMT',
          'lender_comment_url': 'google.ca',
          'lender_name': 'andrew',
          'original_thread_url': 'youtube.com',
          'repayment_probability': null,
          'settle_thread_url': 'gsgdfhsdf.ca',
          'status': 1,
          'transaction_id': 3
        },
        {
          'agree_comment_url': 'true',
          'borrower_name': 'arthur',
          'date_requested': 'Sat, 01 Apr 2017 12:18:37 GMT',
          'lender_comment_url': 'google.ca',
          'lender_name': 'andrew',
          'original_thread_url': 'youtube.com',
          'repayment_probability': null,
          'settle_thread_url': 'gsgdfhsdf.ca',
          'status': 1,
          'transaction_id': 4
        },
        {
          'agree_comment_url': 'true',
          'borrower_name': 'arthur',
          'date_requested': 'Sat, 01 Apr 2017 12:18:37 GMT',
          'lender_comment_url': 'google.ca',
          'lender_name': 'andrew',
          'original_thread_url': 'youtube.com',
          'repayment_probability': null,
          'settle_thread_url': 'gsgdfhsdf.ca',
          'status': 1,
          'transaction_id': 5
        }
      ],
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
  computed: {
    compItems: function () {
      this.items
    }
  },
  methods: {
    details (item) {
      alert(JSON.stringify(item))
    }
  }
}
</script>
