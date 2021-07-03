export const state = () => ({
  loggedIn: false,
})

export const mutations = {
  login(AuthState) {
    AuthState.loggedIn.push({
      loggedIn: false,
    })
  },
  activate(AuthState) {
    AuthState.loggedIn = true
  },
  toggle(AuthState) {
    AuthState.loggedIn = !AuthState.loggedIn
  },
}
