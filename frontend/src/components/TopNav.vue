<template>
  <div id="top-banner">
  <b-navbar toggleable type="inverse" variant="success">

  <b-nav-toggle target="nav_collapse"></b-nav-toggle>

  <b-link class="navbar-brand" to="#">
  <span>BootstrapVue</span>
  </b-link>

  <b-collapse is-nav id="nav_collapse">

  <b-nav is-nav-bar>
  <b-nav-item>Home</b-nav-item>
  <b-nav-item>Stats</b-nav-item>
  <b-nav-item>Past Predictions</b-nav-item>
  <b-nav-item>Make Predictions</b-nav-item>
  <b-nav-item>About</b-nav-item>
  </b-nav>

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

