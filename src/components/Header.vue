<template>
    <header>
        <div @click="homeLink" class="logo">
            <img src="../assets/Logo_Roboto.svg" alt="Roboto Logo">
            <h1>Roboto</h1>
        </div>
        <nav v-if="width > 850">
            <ul>
                <li @click="homeLink" v-on:mouseover="handleHover(0)" v-on:mouseout='handleMouseOut'>home</li>
                <li @click="$emit('modal', 'search')" v-on:mouseover="handleHover(1)" v-on:mouseout='handleMouseOut'>search</li>
                <li v-if="!token" @click="$emit('modal', 'login')" v-on:mouseover="handleHover(2)" v-on:mouseout='handleMouseOut'>login</li>
                <li>
                    <button v-if="!token" class='btn' @click="$emit('modal', 'register')">register</button>
                    <button v-else class='btn' @mouseenter="profileDropDown" @mouseleave="profileDropDown">
                        profile
                        <div v-if="isProfileDropDownOpened && userType === 'Client'" class="profile__dropdown">
                            <ul>
                                <li @click="$emit('modal', 'profile')">settings</li>
                                <li @click="navigate({path: '/client/bookings'})">bookings</li>
                                <li @click="logout">logout</li>
                            </ul>
                            <div class="profile__dropdown__hover"></div>
                        </div>
                        <div v-if="isProfileDropDownOpened && userType === 'Business'" class="profile__dropdown">
                            <ul>
                                <li @click="$emit('modal', 'profile')">settings</li>
                                <li @click="navigate({path: '/business/hotels'})">hotels</li>
                                <li @click="logout">logout</li>
                            </ul>
                            <div class="profile__dropdown__hover"></div>
                        </div>
                    </button>
                </li>
            </ul>
            <div class="nav--hover nav--hover--effect"></div>
        </nav>
        <div v-else @click="openResponsiveMenu" class="menu">
            <div class="menu__line"></div>
            <div class="menu__line"></div>
            <div class="menu__line"></div>
        </div>
    </header>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: 'Header',
    data() {
        return {
            width: null,
            isProfileDropDownOpened: false
        }
    },
    mounted() {
        this.changeWidth();
        window.addEventListener('resize', this.changeWidth);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.changeWidth);
    },
    methods: {
        openResponsiveMenu() {
            this.$emit('menu', 'open');
        },
        changeWidth() {
            this.width = window.innerWidth;
        },
        homeLink() {
            const path = '/' 
            if(this.$route.path !== path) this.$router.push({ path });
            else {
                this.$router.push({ path: '/abcd' });
                setTimeout(() => {
                    this.$router.push({ path });
                }, 1);
            }
        },
        logout() {
            this.$store.dispatch('logout').authModule;
            this.isProfileDropDownOpened = false;
            this.$router.push({ path: '/' });
        },
        navigate(path) {
            if(this.$route.path !== path.path) this.$router.push(path);
            else {
                this.$router.push({ path: '/abcd' });
                setTimeout(() => {
                    this.$router.push(path);
                }, 1);
            }
        },
        handleHover(liNum) {
            const navElements = document.querySelectorAll('nav ul li');
            const hoverEffectElement = document.querySelector('nav .nav--hover');
            const liPositions = navElements[liNum].getBoundingClientRect();
            const newWidth = liPositions.width + 15;

            hoverEffectElement.style.left = liPositions.right - newWidth + 5 + 'px';
            hoverEffectElement.style.width = newWidth + 'px';
            hoverEffectElement.style.height = liPositions.height + 3 + 'px';
            hoverEffectElement.style.transform = 'scaleX(1)';
        },
        handleMouseOut() {
            const hoverEffectElement = document.querySelector('nav .nav--hover');
            hoverEffectElement.style.transform = 'scaleX(0)';
        },
        profileDropDown() {
            this.isProfileDropDownOpened = !this.isProfileDropDownOpened;
        }
    },
    computed: {
        ...mapGetters([
            'token',
            'userType'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../scss/variables.scss';
    @import '../scss/mixins.scss';

    header {
        max-width: 1800px;
        width: 90%;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 15px;

        .logo {
            display: flex;
            align-items: center;
            cursor: pointer;

            h1 {
                margin: 0;
                font-weight: 400;
                font-size: 1.75rem;
                margin-left: 11px;
            }
        }

        nav {
            ul {
                list-style-type: none;
                padding: 0;
                color: $secondary-color-two;
                display: flex;
                align-items: center;

                li {
                margin-right: 35px;
                z-index: 2;
                font-size: 1.063rem;
                font-weight: 400;
                cursor: pointer;

                    button {
                        position: relative;
                        color: $secondary-color-two;
                        border: 2px solid $secondary-color-two;
                        background-color: transparent;
                        width: 87px;
                        height: 33px;
                        transition: 250ms ease-in-out;
                        cursor: pointer;
                        font-weight: 400;
                        font-size: 1.063rem;

                        .profile__dropdown {
                            position: absolute;
                            top: 31px;
                            left: -2px;
                            background-color: $primary-color;
                            box-shadow: 0 0 10px rgba(0,0,0,0.15);

                            ul {
                                display: flex;
                                flex-direction: column;
                                align-items: flex-start;
                                list-style: none;

                                li {
                                    padding: 10px 0;
                                    padding-left: 20px;
                                    background-color: $primary-color;
                                    text-align: left;
                                    width: 100%;
                                }

                                li:hover {
                                    background-color: $secondary-color-two;
                                }
                            }

                            .profile__dropdown__hover {
                                background-color: black;
                                position: absolute;
                                top: 37px;
                                z-index: 1;
                                transform: scaleX(0);
                                transform-origin: left;
                            }
                        }
                    }

                    button:hover {
                        color: $primary-color;
                        background-color: black;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }
                }

                li:nth-child(4) {
                    margin-right: 0;
                }

                li:hover {
                    color: white;
                }
            }

            .nav--hover {
                background-color: black;
                position: absolute;
                top: 37px;
                z-index: 1;
                transform: scaleX(0);
                transform-origin: left;
            }

            .nav--hover--effect {
                transition: 250ms ease-in-out;
            }
        }

        .menu {
            cursor: pointer;

            .menu__line {
                margin: 4px 0;
                width: 25px;
                height: 3px;
                border-radius: 10px;
                background-color: black;
            }

            .first {
                animation: first 150ms 1 normal ease-in-out forwards;    
                transform-origin: right;
            }
            .first--reverse {
                animation: first 150ms 1 reverse ease-in-out forwards;    
                transform-origin: right;
            }
            @keyframes first {
                0% {
                    transform: scaleX(1);
                }
                100% {
                    transform: scaleX(0);
                }
            }
            .second {
                animation: second 100ms 200ms 1 normal ease-in-out forwards; 
            }
            .second--reverse {
                animation: second 100ms 200ms 1 reverse ease-in-out forwards; 
            }
            @keyframes second {
                0% {
                    transform: scaleX(1);
                }
                100% {
                    transform: scaleX(0);
                }
            }
            .third {
                animation: third 150ms 1 normal ease-in-out forwards; 
                transform-origin: left;
            }
            .third--reverse {
                animation: third 150ms 1 reverse ease-in-out forwards; 
                transform-origin: left;
            }
            @keyframes third {
                0% {
                    transform: scaleX(1);
                }
                100% {
                    transform: scaleX(0);
                }
            }
        }
    }
</style>