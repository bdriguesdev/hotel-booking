<template>
    <div class="hotels__create__modal" @click="closeModal">
        <div class="hotels__create__modal__content">
            <nav class="hotels__create__nav">
                <ul>
                    <li>Create</li>
                </ul>
                <svg v-on:click="$emit('modal')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form class="hotels__create__form" @submit.prevent="createHotel">
                <div class="hotels__inputs__container">
                    <label for="hotelName">
                        Hotel name
                        <input type="text" v-model="hotelName"/>
                    </label>
                    <label for="state">
                        State
                        <input type="text" v-model="state"/>
                    </label>
                    <label for="city">
                        City
                        <input type="text" v-model="city"/>
                    </label>
                    <label for="street">
                        Street
                        <input type="text" v-model="street"/>
                    </label>
                    <label for="number">
                        Number
                        <input type="text" v-model="number"/>
                    </label>
                    <label for="complement">
                        Complement
                        <input type="text" v-model="complement"/>
                    </label>
                    <label for="description">
                        Description
                        <textarea v-model="description"></textarea>
                    </label>
                </div>
                <button class="hotels__create__btn" v-on:click="btnAnimation" v-on:mouseenter="btnAnimation">
                    Create now
                    <div class="hotels__btn__container">
                        <div class="hotels__btn--effect">
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                        </div>
                    </div>
                </button>
            </form>
        </div>
    </div>
</template>

<script>

export default {
    name: 'CreateModal',
    data() {
        return {
            isBtnAnimationInProgress: false,
            hotelName: null,
            state: null,
            city: null,
            street: null,
            number: null,
            complement: "",
            description: "",
        }
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.hotels__create__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        createHotel() {
            this.$store.dispatch("createHotel", { hotelName: this.hotelName, state: this.state, city: this.city, street: this.street, number: this.number, complement: this.complement, description: this.description }).hotelsModule;
            this.hotelName = null;
            this.state = null;
            this.city = null;
            this.street = null;
            this.number = null;
            this.complement = "";
            this.description = "";
        },
        closeModal(evt) {
            if(evt.target.className === 'hotels__create__modal') {
                this.$emit('modal');
            }
        },
        btnAnimation() {
            if(!this.isBtnAnimationInProgress) {
                this.isBtnAnimationInProgress = true;
                const button = document.querySelector('.hotels__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isBtnAnimationInProgress = false;
                }, 500);
            }
        }
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .hotels__create__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .hotels__create__modal__content {
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

            .hotels__create__nav {
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
                        color: $secondary-color-one;
                        font-size: 1.25rem;
                        font-weight: 400;   
                        padding-bottom: 10px; 
                        border-bottom: 2px solid $secondary-color-one;
                        transition: 250ms ease-in;
                        cursor: pointer;
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

            .hotels__create__form {
                padding-top: 28px;
                padding-bottom: 36px;  
                padding-left: 44px;  
                padding-right: 44px;  

                .hotels__inputs__container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    @include small-phone {
                        justify-content: center;
                    }
                    
                    label {
                        font-family: $secondary-font;
                        color: $secondary-color-two;
                        font-size: 1rem;
                        text-transform: uppercase;
                        text-align: left;
                        margin: 8px 0px;
                        display: flex;
                        flex-direction: column;
                        align-items: flex-start;
                        @include small-phone {
                            width: 232px;
                        }
                        
                        input {
                            background-color: $input-bg-color;
                            border: none;
                            width: 263px;
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

                        textarea {
                            width: 568px;
                            max-width: 568px;
                            min-width: 568px;
                            height: 88px;
                            outline: none;
                            font-size: 1rem;
                            color: $input-text-color;
                            padding-left: 12px;
                            padding-top: 10px;
                            background-color: $input-bg-color;
                            border: none;
                            box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                            border-bottom: 2px solid $secondary-color-two;
                            @include large-phone {
                                width: 248px;
                                min-width: 248px;
                                max-width: 248px;
                            }
                            @include small-phone {
                                width: 206px;
                                min-width: 206px;
                                max-width: 206px;
                            }
                        }
                    }
                }

                .hotels__create__btn {
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
                    margin: 0 auto;
                    margin-top: 28px;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.20);
                    cursor: pointer;

                    .hotels__btn__container {
                        overflow: hidden;
                        width: 21px;
                        margin-left: 10px;

                        .hotels__btn--effect {
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

                .hotels__create__btn::after {
                    content: 'Create now';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 23px;
                    color: $shadow-color;
                    @include desktop {
                        left: 28px;
                    }
                }
            }
        }
    }
</style>