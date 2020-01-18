<template>
  <div id="app">
    <router-view @menu="openCloseMenu" v-on:modal="modal" ></router-view>
    <ClientProfileModal v-if="userType === 'Client' && token && isProfileModalOpen" v-on:modal="modal" />
    <BusinessProfileModal v-if="userType === 'Business' && token && isProfileModalOpen" v-on:modal="modal" />
    <RegisterModal v-on:modal="modal" v-if="isRegisterModalOpen && !token" />
    <LoginModal v-on:modal="modal" v-if="isLoginModalOpen && !token" />
    <SearchModal v-on:modal="modal" v-if="isSearchModalOpen" />
    <ResponsiveMenu @menu="openCloseMenu" v-on:modal="modal" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import RegisterModal from './components/RegisterModal/RegisterModal';
import LoginModal from './components/LoginModal';
import SearchModal from './components/SearchModal/SearchModal';
import ClientProfileModal from './pages/Client/Profile/Index';
import BusinessProfileModal from './pages/Business/Profile/Index';
import ResponsiveMenu from './components/ResponsiveMenu';

export default {
  /* eslint-disable no-console */
  name: 'app',
  components: {
    RegisterModal,
    LoginModal,
    SearchModal,
    ClientProfileModal,
    BusinessProfileModal,
    ResponsiveMenu
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
    openCloseMenu(type) {
      const menuNav = document.querySelector('.responsive-nav');
      const menuOpenLines = document.querySelectorAll('header .menu .menu__line');
      if(type === 'close') {
          menuNav.classList.toggle('nav--close-animation');
          setTimeout(() => {
            menuNav.style.right = "-200px";
            menuNav.classList.remove('nav--close-animation');
            menuOpenLines[0].classList.toggle('first--reverse');
            menuOpenLines[1].classList.toggle('second--reverse');
            menuOpenLines[2].classList.toggle('third--reverse');
            setTimeout(() => {
              menuOpenLines[0].style.transform = 'scaleX(1)';
              menuOpenLines[1].style.transform = 'scaleX(1)';
              menuOpenLines[2].style.transform = 'scaleX(1)';
              menuOpenLines[0].classList.remove('first--reverse');
              menuOpenLines[1].classList.remove('second--reverse');
              menuOpenLines[2].classList.remove('third--reverse');
            }, 450);
          }, 300);
      } else if(type === 'open') {
        menuOpenLines[0].classList.toggle('first');
        menuOpenLines[1].classList.toggle('second');
        menuOpenLines[2].classList.toggle('third');
        setTimeout(() => {
          menuNav.classList.toggle('nav--open-animation');
          setTimeout(() => {
            menuOpenLines[0].style.transform = 'scaleX(0)';
            menuOpenLines[1].style.transform = 'scaleX(0)';
            menuOpenLines[2].style.transform = 'scaleX(0)';
            menuOpenLines[0].classList.remove('first');
            menuOpenLines[1].classList.remove('second');
            menuOpenLines[2].classList.remove('third');
            menuNav.style.right = "0px";
            menuNav.classList.remove('nav--open-animation');
          }, 300);
        }, 450);
      }
    },
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
  @import './scss/mixins.scss';

  html {
    font-size: 16px;
    @include desktop {
      font-size: 14px;
    }
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
