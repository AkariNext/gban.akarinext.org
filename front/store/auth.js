export const state = () => ({
  loggedIn: false,
})

export const mutations = {
  login(AuthState) {
    AuthState.loggedIn.push({
      loggedIn: false,
    })
  },
  toggle(AuthState) {
    AuthState.loggedIn = !AuthState.loggedIn
  },
}
