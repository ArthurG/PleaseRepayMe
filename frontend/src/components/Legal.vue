<template>
    <div>
      <b-modal id="modal-read-tos" title="Welcome!"
        no-close-on-backdrop
        ok-only
        no-close-on-esc>
         <h5> By proceeding to use this website, I agree to be bound by the 
              <a v-on:click="openTos"> Terms of Service </a>
         </h5>
      </b-modal>

      <b-modal id="modal-tos" class="legal" title="Terms of Service" :hide-footer=true >
         <div class="legal">
           <p> {{sec1Para}} </p>
           <h4> {{sec2Heading}} </h4>
           <h6> {{sec2Subheading}} </h6>
           <ul>
             <li>{{sec2Bullet1}}</li>
             <li>{{sec2Bullet2}}</li>
             <li>{{sec2Bullet3}}</li>
           </ul>
           <h4> {{sec3Heading}} </h4>
           <p> {{sec3Para}} </p>
           <h4> {{sec4Heading}} </h4>
           <p> {{sec4Para}} </p>
           <p> {{sec4Para2}} </p>
           <ul>
             <li>{{sec4Bullet1}}</li>
             <li>{{sec4Bullet2}}</li>
             <li>{{sec4Bullet3}}</li>
             <li>{{sec4Bullet4}}</li>
             <li>{{sec4Bullet5}}</li>
             <li>{{sec4Bullet6}}</li>
           </ul>
           <h4> {{sec5Head}} </h4>
           <p> {{sec5Para}} </p>
           <h4> {{sec6Head}} </h4>
           <p> {{sec6Para}} </p>
           <h4> {{sec7Head}} </h4>
           <p> {{sec7Para1}} </p>
           <p> {{sec7Para2}} </p>
           <p> {{sec7Para3}} </p>
           <p> {{sec7Para4}} </p>
         </div>
      </b-modal>
    </div>
</template>

<script>
export default {
  name: 'Legal',
  data () {
    return {
      sec1Para: 'The Terms of Service is a contract between you (“you”, “the company”, “user”) and “PleaseRepay.me”. By any operations, and/or use of the services and/or application will constitute an “acceptance of Terms and Agreement” and an agreement to, and understand of, the Terms of Service.',
      sec2Heading: 'Definitions',
      sec2Subheading: 'Services',
      sec2Bullet1: 'Meaning the provision of services as requested by the user by using any parts and/or abilities of the services/application provided by “PleaseRepay.me".',
      sec2Bullet2: 'Any actions, requests, and/or commands interacting with the application “PleaseRepay.me”',
      sec2Bullet3: 'Meaning all of the above, including new updates, enhancements, features, and additions to any part of the application/service will also be part of this agreement.',
      sec3Heading: 'Description of Services',
      sec3Para: 'PleaseRepay.me is a website intended to make predictions on loan repayment on reddit.com/r/borrow. Using various attributes on a given user’s profile, PleaseRepay.me performs some mathematical calculations to create probabilities on the outcomes of a loan. PleaseRepay.me is intended as an educational tool, and is not intended to replace the due-diligence required when lending out money.',
      sec4Heading: 'Limitations on the use of the Services',
      sec4Para: 'Unless given written and specified permission by the creator’s of “PleaseRepay.me”, the user agrees that this software cannot be reused or commercialised for any third party. The user/you may not modify, copy, distribute, transmit, display, perform, reproduce, publish, license, create derivative works from, transfer, or sell any information, software, products, or services obtained from the Services. The User also understands that “PleaseRepay.me” requires the User to be utilising the software, within the legal limits of the law of the jurisdiction the User is within when using the software.',
      sec4Para2: 'The User agrees that none of these Services will be used improperly, or to harm others. By way of example, and not as limitation, you agree when using the services, you will not:',
      sec4Bullet1: 'Defame, abuse, harass, stalk, threaten, or otherwise violate the legal rights (such as rights of privacy, and discrimination) of others.',
      sec4Bullet2: 'Publish, post, upload, distribute, or disseminate any inappropriate, profane, defamatory, obscene, indecent, or unlawful material nor information which pertains to the Services provided or other Users of the Service.',
      sec4Bullet3: 'Use any material or information, including images or photographs, which are made available through the Services in any manner that infringes any copyright, trademark, patent, trade secret, or other proprietary right of any party.',
      sec4Bullet4: 'Upload any type of computer file that contain viruses, Trojan horses, worms, time bombs, cancelbots, corrupted files, or any other similar software or programs that may damage the operation of another\'s computer or property of another.',
      sec4Bullet5: 'Violate any applicable laws or regulations.',
      sec4Bullet6: 'Use, download or otherwise copy, or provide (whether or not for a fee) to a person or entity any directory of users of the Services or other user or usage information or any portion thereof.',
      sec5Head: 'Privacy and Protection of Information/Responsibility for Data',
      sec5Para: '“PleaseRepay.me” tries to ensure the privacy and protection of information to the best of its ability/capabilities and will do what is reasonably in the Company’s power to ensure data security.. “PleaseRepay.me” stores information to continually improve and add onto the service, and it is accepted by the User that the data can/will be stored for the development of the service. In no event shall “PleaseRepay.me” and/or its suppliers be liable for any special, indirect or consequential damages, or any damages whatsoever resulting from loss of use, data or profits, whether in an action of contract negligence or other tortious action, arising out of, or in connection any matter in regards to privacy, storage of data, and/or responsibility of data.',
      sec6Head: 'Acceptable Use of the Services',
      sec6Para: 'As a condition to the use of the Service, the User, will not use the service which is unlawful or prohibited by any terms of this Terms of Service. The User agrees not to use the Service in any manner which could damage, disable, overburden, or impair any Microsoft server, or the network(s) connected to any Microsoft server, or interfere with any other party’s use and enjoyment of any Services. The User agrees not to gain unauthorised access to any Services, other person(s) data and/or any access which is not intended for public access by the proprietor of “PleaseRepay.me”.',
      sec7Head: 'Liability of the Service',
      sec7Para1: '“PleaseRepay.me” will have third-party links on their website, these links are not condoned by the company nor does the company have any control over these websites and the User understands that any third-party websites and services are not in their purview nor does “PleaseRepay.me” accept any liability for any third-party materials.',
      sec7Para2: 'In no event shall “PleaseRepay.me” and/or its suppliers be liable for any special, indirect or consequential damages, or any damages whatsoever resulting from loss of use, data or profits, whether in an action of contract negligence or other tortious action, arising out of, or in connection with the use or performance of software, documents, provision or failure to provide services or information available from the services',
      sec7Para3: 'The User understands that “PleaseRepay.me”, to the extent not prohibited by the law, will be not liable for personal injury, or any incidental, special, indirect, direct, or consequential damages whatsoever, including and without limitation, damages for loss of profits, loss of data, business interruption, or any other commercial damages or losses, arising out of or related to your use, or inability to use the Services provided by “PleaseRepay.me” however caused, regardless of the theory of liability (Contract, Tort, or otherwise) and even if “PleaseRepay.me” has been advised of the possibility of such damages. In no event shall the total liability of “PleaseRepay.me” of all, and any damages exceed the amount of five US dollars ($5.00 USD).',
      sec7Para4: 'The User understands that they relinquish all wrongdoing and liability, criminal and civil, regardless if the User utilises the Services in a way contrary to the jurisdiction the software is being used within.'
    }
  },
  mounted () {
    this.showTosDialogIfRequired()
  },
  methods: {
    showTosDialogIfRequired: function () {
      if (this.$cookie.get('showed-tos')) {
        console.log('TOS last shown on ')
        console.log(this.$cookie.get('showed-tos'))
      } else {
        this.$root.$emit('show::modal', 'modal-read-tos')
        this.$cookie.set('showed-tos', Date.now(), {expires: '1Y'})
        console.log('Showing tos')
      }
    },
    openTos: function () {
      this.$root.$emit('show::modal', 'modal-tos')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.legal{
  color: black;
  font-size: 100%;
  text-align: left;
  margin: 0.3em 1em;
}

</style>

<style>
  #modal-tos>.modal-dialog {
    max-width: 1400px !important;
    width: 95%;
  }
</style>
