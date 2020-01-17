<template>
  <div id="app">
    <router-view v-on:modal="modal" ></router-view>
    <ClientProfileModal v-if="userType === 'Client' && token && isProfileModalOpen" v-on:modal="modal" />
    <BusinessProfileModal v-if="userType === 'Business' && token && isProfileModalOpen" v-on:modal="modal" />
    <RegisterModal v-on:modal="modal" v-if="isRegisterModalOpen && !token" />
    <LoginModal v-on:modal="modal" v-if="isLoginModalOpen && !token" />
    <SearchModal v-on:modal="modal" v-if="isSearchModalOpen" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import RegisterModal from './components/RegisterModal/RegisterModal';
import LoginModal from './components/LoginModal';
import SearchModal from './components/SearchModal/SearchModal';
import ClientProfileModal from './pages/Client/Profile/Index';
import BusinessProfileModal from './pages/Business/Profile/Index';

export default {
  /* eslint-disable no-console */
  name: 'app',
  components: {
    RegisterModal,
    LoginModal,
    SearchModal,
    ClientProfileModal,
    BusinessProfileModal
  },
  data() {
    return {
      isRegisterModalOpen: false,
      isLoginModalOpen: false,
      isSearchModalOpen: false,
      isProfileModalOpen: false
    }
  },
  computed: {
    ...mapGetters([
      'token',
      'userType'
    ])
  },
  methods: {
    modal(modalType) {
      if(modalType === 'register') {
        this.isRegisterModalOpen = !this.isRegisterModalOpen;
      } else if (modalType === 'login') {
        this.isLoginModalOpen = !this.isLoginModalOpen;
      } else if (modalType === 'search') {
        this.isSearchModalOpen = !this.isSearchModalOpen;
      } else if (modalType === 'profile') {
        this.isProfileModalOpen = !this.isProfileModalOpen;
      }
    }
  }
}
</script>

<style lang="scss">
  @import './scss/variables.scss';
  html {
    font-size: 16px;
  }

  body {
    margin: 0;
    font-family: $primary-font;
  }

  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .btn {
    font-family: $primary-font;
  }
</style>
