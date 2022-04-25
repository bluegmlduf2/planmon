<template>
  <div id="app">
    <router-view />
  </div>
</template>
<script>
/* ============
 * Entry Point
 * ============
 *
 * The entry point of the application.
 */
import firebase from '@/plugins/firebase';

export default {
  /**
   * The name of the application.
   */
  name: 'PLANMON',

  /**
   * Fires when the app has been mounted.
   */
  mounted() {
    firebase.onAuthStateChanged(firebase.auth, (user) => {
      if (user) {
        this.$store.dispatch('autoSignIn', user);
      }
    });
    // If the user is authenticated,
    // fetch the data from the API
    // if (this.$store.state.auth.authenticated) {
    //   this.$store.dispatch('account/find');
    // }
  },
};
</script>
