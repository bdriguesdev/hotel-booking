<template>
    <div class="hotels__filter__modal" @click="closeModal">
        <div class="hotels__filter__modal__content">
            <nav class="hotels__filter__nav">
                <ul>
                    <li>Filters</li>
                </ul>
                <svg v-on:click="$emit('modal')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form class="hotels__filter__form" v-on:click.prevent="">
                <div class="hotels__inputs__container">
                    <label for="name">
                        Hotel name
                        <input type="text" v-model="name"/>
                    </label>
                    <label for="state">
                        State
                        <input type="text" v-model="state"/>
                    </label>
                    <label for="city">
                        City
                        <input type="text" v-model="city"/>
                    </label>
                </div>
                <button class="hotels__filter__btn" v-on:click="filterHotels" v-on:mouseenter="btnAnimation">
                    Filter now
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
import { mapGetters } from 'vuex';

export default {
    name: 'FilterModal',
    data() {
        return {
            isBtnAnimationInProgress: false,
            name: "",
            city: "",
            state: ""
        }
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.hotels__filter__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        closeModal(evt) {
            if(evt.target.className === 'hotels__filter__modal') {
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
        },
        filterHotels() {
            this.btnAnimation();
            const args = {
                nameSearch: this.name !== ""? "True": "False",
                name: this.name,
                citySearch: this.city !== ""? "True": "False",
                city: this.city,
                stateSearch: this.state !== ""? "True": "False",
                state: this.state,
                businessSearch: "True",
                businessId: this.user.id
            };
            this.$store.dispatch('filterHotels', args).hotelsModule;
        }
    },
    computed: {
        ...mapGetters([
            'user'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';

    .hotels__filter__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .hotels__filter__modal__content {
            background-color: $primary-color;
            width: 670px;
            margin: 0 auto;
            margin-top: 10vh;

            .hotels__filter__nav {
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

            .hotels__filter__form {
                padding-top: 28px;
                padding-bottom: 36px;  
                padding-left: 44px;  
                padding-right: 44px;  

                .hotels__inputs__container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    
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
                        
                        input {
                            background-color: $input-bg-color;
                            border: none;
                            width: 263px;
                            padding-left: 12px;
                            height: 42px;
                            border-bottom: 2px solid $secondary-color-two;
                            outline: none;
                            font-size: 1rem;
                            color: $input-text-color;
                            box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                            border-radius: 0;
                        }
    
                    }
                }

                .hotels__filter__btn {
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

                .hotels__filter__btn::after {
                    content: 'Filter now';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 29px;
                    color: $shadow-color;
                }
            }
        }
    }
</style>