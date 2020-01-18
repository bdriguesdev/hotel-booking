<template>
    <div class="register__modal" @mousedown="closeModal">
        <div class="register__modal__content">
            <nav class="register__nav">
                <ul>
                    <li v-on:click="changeOption('business')" >Business</li>
                    <li v-on:click="changeOption('client')" >Client</li>
                </ul>
                <svg @click="$emit('modal', 'register')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <Business v-if="businessActive" />
            <Client v-else />
        </div>
    </div>
</template>

<script>
import Business from './Business';
import Client from './Client';

export default {
    //need to use the nav to select between client/business
    name: 'RegisterModal',
    components: {
        Business,
        Client
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.register__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    data() {
        return {
            businessActive: true,
            clientActive: false
        }
    },
    methods: {
        changeOption(option) {
            const options = document.querySelectorAll('.register__nav ul li');

            if(option === 'business') {
                this.businessActive = true;
                this.clientActive = false;
                options[1].style.color = '#FFFFFF';
                options[1].style.borderColor = '#000000';
                options[0].style.color = '#FF1E1E';
                options[0].style.borderColor = '#FF1E1E';
            } else {
                this.businessActive = false;
                this.clientActive = true;
                options[0].style.color = '#FFFFFF';
                options[0].style.borderColor = '#000000';
                options[1].style.color = '#FF1E1E';
                options[1].style.borderColor = '#FF1E1E';
            }
        },
        closeModal(evt) {
            if(evt.target.className === 'register__modal') {
                this.$emit('modal', 'register');
            }
        }
    }
}
</script>

<style lang='scss'>
    @import '../../scss/variables.scss';
    @import '../../scss/mixins.scss';

    .register__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .register__modal__content {
            background-color: $primary-color;
            width: 670px;
            margin: 0 auto;
            margin-top: 10vh;
            @include large-phone {
                width: 350px;
            }
            @include small-phone {
                width: 280px;
            }

            .register__nav {
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
                        color: $primary-color;
                        font-size: 1.25rem;
                        font-weight: 400;   
                        padding-bottom: 10px; 
                        border-bottom: 2px solid $secondary-color-two;
                        transition: 250ms ease-in;
                        cursor: pointer;
                    }

                    li:nth-child(1) {
                        margin-right: 10px;
                        border-bottom: 2px solid $secondary-color-one;
                        color: $secondary-color-one;
                    }

                    li:nth-child(2) {
                        margin-left: 10px;
                    }

                    li:hover {
                        border-color: $primary-color;
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

            .register__form {
                padding-top: 28px;
                padding-bottom: 36px;    
                display: flex;
                flex-wrap: wrap;
                justify-content: center;

                label {
                    font-family: $secondary-font;
                    color: $secondary-color-two;
                    font-size: 1rem;
                    text-transform: uppercase;
                    display: block;
                    text-align: left;
                    width: 261px;
                    margin: 8px 15px;
                    @include small-phone {
                        width: 232px;
                    }

                    input {
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
                        @include small-phone {
                            width: 220px;
                        }
                    }

                    input[type=date] {
                        height: 44px;
                    }

                }
                
                .register__btn {
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

                    .register__btn__container {
                        overflow: hidden;
                        width: 21px;
                        margin-left: 10px;

                        .register__btn--effect {
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

                .register__btn::after {
                    content: 'Register now';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 17px;
                    color: $shadow-color;
                    @include desktop {
                        left: 23px;
                    }
                }
            }
        }
    }
</style>