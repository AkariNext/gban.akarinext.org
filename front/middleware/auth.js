export default function ({ store, redirect, route }) {
  const user = store.state.auth.loggedIn
  if (!user && route.name === 'index') {
    redirect('/welcome')
  }
}
