<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-btn icon @click.stop="miniVariant = !miniVariant">
          <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
        </v-btn>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
        <div
          v-if="!miniVariant"
          style="position: fixed; bottom: 0; left: calc(50% - 80px / 2)"
        >
          <v-divider />
          <v-switch v-model="theme" :prepend-icon="themeIcon"></v-switch>
        </div>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-menu v-if="profile" bottom min-width="200px" rounded offset-y>
        <template #activator="{ on }">
          <v-btn icon x-large v-on="on">
            <v-avatar color="brown" size="48">
              <v-img :src="profile.avatar_url" :lazy-src="profile.avatar_url" />
            </v-avatar>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <v-avatar color="brown">
                <v-img
                  :src="profile.avatar_url"
                  :lazy-src="profile.avatar_url"
                />
              </v-avatar>
              <h3>{{ profile.username }}</h3>
              <p class="text-caption mt-1">
                {{ profile.email }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text> Edit Account</v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text @click="disconnect">
                Disconnect</v-btn
              >
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
      <v-btn v-else depressed href="https://api.gban.akarinext.org/v1/login">
        <v-icon>mdi-account-circle</v-icon>
        ログイン
      </v-btn>
    </v-app-bar>
    <v-main style="height: 100%">
      <nuxt />
    </v-main>
    <v-footer padless>
      <v-card
        flat
        tile
        class="blue lighten-2 white--text text-center"
        style="width: 100%"
      >
        <v-card-text />

        <v-card-text class="white--text pt-0"> テスト</v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>AkariNext</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      theme: false,
      profile: null,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire',
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'AkariNext',
    }
  },
  computed: {
    themeIcon() {
      return this.theme ? 'mdi-weather-night' : 'mdi-weather-sunny'
    },
  },
  watch: {
    theme() {
      this.$vuetify.theme.dark = this.theme
      localStorage.theme = this.theme
    },
  },
  beforeCreate() {
    const theme = localStorage.theme === 'true'
    this.$vuetify.theme.dark = theme
    this.theme = theme
    if (localStorage.token && localStorage.profile) {
      this.profile = JSON.parse(localStorage.profile)
    }
  },
  methods: {
    disconnect() {
      localStorage.clear()
    },
  },
}
</script>
