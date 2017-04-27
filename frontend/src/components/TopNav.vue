<template>
  <div id="top-banner">
  <b-navbar toggleable type="inverse" variant="success">

  <b-nav-toggle target="nav_collapse"></b-nav-toggle>

  <b-link class="navbar-brand" to="#">
  <span>Borrowr</span>
  </b-link>

  <b-collapse is-nav id="nav_collapse">

  <b-nav is-nav-bar class="ml-auto">
  <router-link to="/"><b-nav-item right-alignment><icon name="github"></icon></b-nav-item></router-link>
  <router-link to="/"><b-nav-item right-alignment><icon name="envelope-o"></icon></b-nav-item></router-link>
  </b-nav>

  </b-collapse>
  </b-navbar>
  </div>

</template>

<script>
export default {
  name: 'TopNav'
}
</script>

<style scoped>
.fa-icon{
  width: auto;
  height: 2.0em;
  color: white;
}

</style>

