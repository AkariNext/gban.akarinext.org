export const state = () => ({
  loggedIn: false,
})

export const mutations = {
  login(AuthState) {
    AuthState.loggedIn.push({
      loggedIn: false,
    })
  },
  toggle(AuthState, odo) {
    AuthState.loggedIn = !AuthState.loggedIn
  },
}
