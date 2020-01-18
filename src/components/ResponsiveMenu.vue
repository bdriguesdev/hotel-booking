<template>
    <nav class="responsive-nav">
        <svg @click="closeMenu" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='black' stroke-width="2"/>
        </svg>
        <ul class="nav__list">
            <li class="link">
                <span @click="pushRouter({ path: '/' })">home</span>
            </li>
            <li class="link">
                <span @click="openModal('search')">search</span>
            </li>
            <li v-if="!token" class="link">
                <span @click="openModal('login')">login</span>
            </li>
            <li v-if="!token" class="link">
                <span @click="openModal('register')" >register</span>
            </li>
            <li v-if="token" class="link">
                <span @click="openCloseDropdown" >profile</span>
                <div v-if="userType === 'Client' && isProfileDropdownOpened" class="profile-options">
                    <span>settings</span>
                    <span @click="pushRouter({ path: '/client/bookings/' })">bookings</span>
                    <span @click="handleLogout">logout</span>
                </div>
                <div v-if="userType === 'Business' && isProfileDropdownOpened" class="profile-options">
                    <span>settings</span>
                    <span @click="pushRouter({ path: '/business/hotels/' })">hotels</span>
                    <span @click="handleLogout">logout</span>
                </div>
            </li>
        </ul>
    </nav>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: 'ResponsiveMenu',
    data() {
        return {
            isProfileDropdownOpened: false
        }
    },
    methods: {
        openCloseDropdown() {
            this.isProfileDropdownOpened = !this.isProfileDropdownOpened;
        },
        handleLogout() {
            this.$store.dispatch('logout').authModule;
            this.$emit('menu', 'close');
            this.isProfileDropdownOpened = false;
            this.$router.push({ path: '/' });
        },
        closeMenu() {
            const exit = document.querySelector('.responsive-nav svg');
            exit.classList.toggle('exit-animation');
            setTimeout(() => {
                exit.classList.remove('exit-animation');
                this.$emit('menu', 'close');
                this.isProfileDropdownOpened = false;
            }, 150);
        },
        pushRouter(path) {
            this.$emit('menu', 'close');
            this.$router.push(path);
            this.isProfileDropdownOpened = false;
        },
        openModal(modal) {
            this.$emit('menu', 'close');
            this.$emit('modal', modal);
            this.isProfileDropdownOpened = false;
        }
    },
    computed: {
        ...mapGetters([
            'userType',
            'token'
        ])
    }
}
</script>

<style lang='scss'>
     @import '../scss/variables.scss';

    .responsive-nav {
        position: fixed;
        z-index: 10;
        top: 0;
        right: -200px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        height: 100vh;
        background-color: white;

        svg {
            margin: 20px 0;
            margin-left: 75px;
            cursor: pointer;
        }

        .exit-animation {
            animation: exit 150ms 1 normal ease-in-out; 
        }

        @keyframes exit {
            0% {
                transform: rotate(0)
            }
            100% {
                transform: rotate(180deg)
            }
        }

        .nav__list {
            list-style: none;
            margin: 0;
            padding: 0;

            .link {

                span {
                    cursor: pointer;
                    display: block;
                    padding: 10px 60px 10px 30px;
                    text-align: left;
                    font-size: 1.15rem;
                    font-weight: 300;
                    font-family: $primary-font;
                    color: $secondary-color-two;
                    transition: background-color 200ms ease-in-out, color 100ms ease-in;
                }

                span:hover {
                    color: white;
                    background-color: black;
                }

                .profile-options {

                    span {
                        cursor: pointer;
                        display: block;
                        text-align: left;
                        padding: 10px 0;
                        padding-left: 45px;
                        width: 100%;
                        font-size: 1.15rem;
                        font-weight: 300;
                        font-family: $primary-font;
                        color: $secondary-color-two;
                        transition: background-color 200ms ease-in-out, color 100ms ease-in;
                    }

                    span:hover {
                        color: white;
                        background-color: black;
                    }
                }
            }
        }
    }

    .nav--open-animation {
        animation: nav-animation 300ms 1 normal ease-in-out forwards;
    }

    .nav--close-animation {
        animation: nav-animation 300ms 1 reverse ease-in-out forwards;    
    }

    @keyframes nav-animation {
        0% {
            right: -200px;
        }
        100% {
            right: 0px;
        }
    }
</style>