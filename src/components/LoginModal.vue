<template>
    <div class="login__modal" @click="closeModal">
        <div class="login__modal__content">
            <nav class="login__nav">
                <ul>
                    <li>Login</li>
                </ul>
                <svg v-on:click="$emit('modal', 'login')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form class="login__form" @submit.prevent="login">
                <label for="userType">
                    User type
                    <div class="login__radio__container">
                        <span><input class="login__radio" type="radio" value='Client' v-model="userType"> Client</span>
                        <span><input class="login__radio" type="radio" value='Business' v-model="userType"> Business</span>
                    </div>
                </label>
                <label for="email">
                    Email
                    <input type="email" id="login__email" v-model="email"/>
                </label> 
                <label for="password">
                    Password
                    <input type="password" id="login__password" v-model="password"/>
                </label>
                <button class="login__btn" v-on:click="btnAnimation" v-on:mouseenter="btnAnimation">
                    Log in
                    <div class="login__btn__container">
                        <div class="login__btn--effect">
                            <img src="../assets/Button_arrow_two.svg" alt="Register button icon" />
                            <img src="../assets/Button_arrow_two.svg" alt="Register button icon" />
                        </div>
                    </div>
                </button>
            </form>
        </div>
    </div>
</template>

<script>
import validate from 'validate.js';
import { mapGetters } from 'vuex';

export default {
    //need to use the nav to select between client/business
    name: 'LoginModal',
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.login__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    data() {
        return {
            email: null,
            password: null,
            isLoginBtnAnimationInProgress: false,
            userType: null
        }
    },
    methods: {
        login() {
            this.$store.dispatch("login", { userEmail: this.email, userPassword: this.password, userType: this.userType }).authModule;
            this.email = '';
            this.password = '';
        },
        closeModal(evt) {
            if(evt.target.className === 'login__modal') {
                this.$emit('modal', 'login');
            }
        },
        btnAnimation() {
            if(!this.isLoginBtnAnimationInProgress) {
                this.isLoginBtnAnimationInProgress = true;
                const button = document.querySelector('.login__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isLoginBtnAnimationInProgress = false;
                }, 500);
            }
        }
    },
    computed: {
        ...mapGetters([
            'token'
        ])
    },
    watch: {
        email(newValue) {
            const loginInput = document.getElementById('login__email');
            const validationResult = validate.single(newValue, { presence: true, email: true });
            if(!validationResult) {  
                loginInput.style.borderColor = '#FF1E1E';
            } else {
                loginInput.style.borderColor = '#000000';
            }
        },
        password(newValue) {
            const passwordInput = document.getElementById('login__password');
            const validationResult = validate.single(newValue, { presence: true, length: { minimum: 8, maximum: 55 } });
            if(!validationResult) {
                passwordInput.style.borderColor = '#FF1E1E';
            } else {
                passwordInput.style.borderColor = '#000000';
            }
        }
    }
}
</script>

<style lang='scss'>
    @import '../scss/variables.scss';
    @import '../scss/mixins.scss';

    .login__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .login__modal__content {
            background-color: $primary-color;
            width: 383px;
            margin: 0 auto;
            margin-top: 10vh;
            @include large-phone {
                width: 350px;
            }
            @include small-phone {
                width: 280px;
            }

            .login__nav {
                background-color: $secondary-color-two;
                display: flex;
                justify-content: center;
                position: relative;

                ul {
                    list-style: none;
                    margin: 0;
                    display: flex;
                    padding: 0;
                    padding-top: 20px;

                    li {
                        font-size: 1.25rem;
                        font-weight: 400;   
                        padding-bottom: 10px; 
                        transition: 250ms ease-in;
                        cursor: pointer;
                        border-bottom: 2px solid $secondary-color-one;
                        color: $secondary-color-one;
                    }
                }

                svg {
                    position: absolute;
                    right: 12px;
                    top: 12px;  
                    cursor: pointer;

                    path {
                        transition: 200ms ease-in-out;
                    }
                }
                
                svg:hover path {
                    stroke: $secondary-color-one;
                }
            }

            .login__form {
                padding-top: 28px;
                padding-bottom: 36px;    
                display: flex;
                flex-direction: column;
                align-items: center;

                label {
                    font-family: $secondary-font;
                    color: $secondary-color-two;
                    font-size: 1rem;
                    font-weight: 300;
                    text-transform: uppercase;
                    display: block;
                    text-align: left;
                    width: 261px;
                    margin: 8px 15px;
                    @include small-phone {
                        width: 232px;
                    }

                    input[type=email], input[type=password] {
                        background-color: $input-bg-color;
                        border: none;
                        width: 249px;
                        padding-left: 12px;
                        height: 42px;
                        border-bottom: 2px solid $secondary-color-two;
                        outline: none;
                        font-size: 1rem;
                        color: $input-text-color;
                        box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                        border-radius: 0;
                        transition: 250ms ease-in-out;
                        @include small-phone {
                            width: 220px;
                        }
                    }

                    .login__radio__container {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-around;

                        span {
                            font-family: $secondary-font;
                            color: $secondary-color-two;
                            font-size: 1rem;
                            font-weight: 300;
                            margin-top: 8px;
                        }
                    }

                }
                
                .login__btn {
                    font-family: $primary-font;
                    background-color: $secondary-color-one;
                    border: none;
                    color: $primary-color;
                    width: 167px;
                    height: 44px;
                    font-size: 1.063rem;
                    font-weight: 700;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    position: relative;
                    z-index: 1;
                    margin-top: 28px;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.20);
                    cursor: pointer;

                    .login__btn__container {
                        overflow: hidden;
                        width: 21px;
                        margin-left: 10px;

                        .login__btn--effect {
                            position: relative;
                            left: -200%;
                            width: 300%;
                            display: flex;
                            justify-content: space-between;
                            height: 100%;
                        }

                        @keyframes hover-animation {
                            100% {
                                left: -1px;
                            }
                        }
                    }
                }

                .login__btn::after {
                    content: 'Log in';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 43px;
                    color: $shadow-color;
                    @include desktop {
                        left: 46px;
                    }
                }
            }
        }
    }
</style>