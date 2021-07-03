<template>
  <v-parallax
    dark
    src="https://cdn.discordapp.com/attachments/615108234650320928/792733186743992360/unknown.png"
    style="height: 100%"
    jumbotron
  >
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12">
        <h1 class="text-h4 font-weight-thin mb-4">AkariNext</h1>
        <h4 class="subheading">ww</h4>
      </v-col>
    </v-row>
  </v-parallax>
</template>

<script>
export default {
  mounted() {
    const token = this.$route.query.token
    localStorage.token = token
    const loggedIn = this.$store.state.auth.loggedIn
    this.$store.commit('auth/activate', loggedIn)
    const axios = this.$axios
    this.$axios
      .get('https://api.gban.akarinext.org/v1/authenticated', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(function (response) {
        if (response.data === 'True') {
          axios
            .get('https://api.gban.akarinext.org/v1/profile', {
              headers: {
                Authorization: `Bearer ${token}`,
              },
            })
            .then(function (response) {
              localStorage.profile = JSON.stringify(response.data)
            })
        }
      })
  },
}
</script>

<style>
.v-parallax__image {
  transform: translate(-50%) !important;
}
</style>
