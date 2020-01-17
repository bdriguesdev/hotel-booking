<template>
    <div class="booking__filter__modal" @click="closeModal">
        <div class="booking__filter__modal__content">
            <nav class="booking__filter__nav">
                <ul>
                    <li>Filters</li>
                </ul>
                <svg v-on:click="$emit('modal')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form class="booking__filter__form" v-on:click.prevent="">
                <div class="booking__inputs__container">
                    <label class='booking__input__start' for='Start date'>
                        AFTER
                        <span class="input__date__container">{{ transformStartDateToText }}</span>
                        <Calendar :type="'Start'" />
                    </label> 
                    <label class='booking__input__end' for='Start date'>
                        BEFORE
                        <span class="input__date__container">{{ transformEndDateToText }}</span>
                        <Calendar :type="'End'" />
                    </label> 
                    <label for="city">
                        City
                        <input type="text" v-model="city"/>
                    </label>
                    <label for="state">
                        State
                        <input type="text" v-model="state"/>
                    </label>
                    <label for="priceRange">
                        Price range
                        <div class="booking__input--range">
                            <input type="text" placeholder="min" v-model="minPrice">
                            <input type="text" placeholder="max" v-model="maxPrice"> 
                        </div>
                    </label>
                    <label class='booking__reviews__container' for="review">
                        Review Rating
                        <div class="booking__reviews__rating">
                            <img src="../../../assets/Review_star.svg" alt="Review rating star">
                            <img src="../../../assets/Review_star.svg" alt="Review rating star">
                            <img src="../../../assets/Review_star.svg" alt="Review rating star">
                            <img src="../../../assets/Review_star.svg" alt="Review rating star">
                            <img src="../../../assets/Review_star.svg" alt="Review rating star">
                        </div>
                    </label>
                </div>
                <button class="booking__filter__btn" v-on:click="handleFilter" v-on:mouseenter="btnAnimation">
                    Filter now
                    <div class="booking__btn__container">
                        <div class="booking__btn--effect">
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

import Calendar from './Calendar';

export default {
    name: 'FilterModal',
    components: {
        Calendar
    },
    data() {
        return {
            isBtnAnimationInProgress: false,
            city: '',
            state: '',
            minPrice: '',
            maxPrice: ''
        }
    },
    created() {
        this.$store.dispatch('changeBookingStart', null);
        this.$store.dispatch('changeBookingEnd', null);
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.booking__filter__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        handleFilter() {
            this.btnAnimation();
            const args = {
                startAt: this.bookingStart,
                endAt: this.bookingEnd,
                city: this.city,
                state: this.state,
                minPrice: this.minPrice,
                maxPrice: this.maxPrice
            };
            this.$store.dispatch('getBookings', args);
        },
        closeModal(evt) {
            if(evt.target.className === 'booking__filter__modal') {
                this.$emit('modal');
            }
        },
        btnAnimation() {
            if(!this.isBtnAnimationInProgress) {
                this.isBtnAnimationInProgress = true;
                const button = document.querySelector('.booking__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isBtnAnimationInProgress = false;
                }, 500);
            }
        }
    },
    computed: {
        
        ...mapGetters([
            'bookingStart',
            'bookingEnd'
        ]),
        transformStartDateToText() {
            const date = this.bookingStart;
            if(date) {
                const year = date.getFullYear();
                const month = date.getMonth() + 1;
                const day = date.getDate();

                return `${day}/${month}/${year}`;
            } else {
                return '--/--/----'
            }

        },
        transformEndDateToText() {
            const date = this.bookingEnd;
            if(date) {
                const year = date.getFullYear();
                const month = date.getMonth() + 1;
                const day = date.getDate();

                return `${day}/${month}/${year}`;
            } else {
                return '--/--/----'
            }

        }
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .booking__filter__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .booking__filter__modal__content {
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

            .booking__filter__nav {
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

            .booking__filter__form {
                padding-top: 28px;
                padding-bottom: 36px;  
                padding-left: 44px;  
                padding-right: 44px;  

                .booking__inputs__container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    @include large-phone {
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
                        
                        .booking__input--range {
                            width: 275px;
                            height: 46px;
                            position: relative;
                            display: flex;
                            justify-content: space-between;
                            @include small-phone {
                                width: 232px;
                            }

                            input {
                                width: 110px;
                                @include small-phone {
                                    width: 80px;
                                }
                            }
                        }

                        .booking__reviews__rating {
                            width: 275px;
                            margin-top: 10px;

                            img {
                                width: 29px;
                                height: 29px;
                            }

                            img:nth-child(n + 2) {
                                margin: 0 5px;
                            }

                            img:last-child {
                                margin: 0;
                            }
                        }
                    }

                    .input__date__container {
                        margin-bottom: 20px;
                        display: block;
                        width: 114px;
                        height: 44px;
                        background-color: $secondary-color-two;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                        font-family: $primary-font;
                        color: $primary-color;
                        font-weight: 500;
                        font-size: 1.063rem;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                }

                .booking__filter__btn {
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

                    .booking__btn__container {
                        overflow: hidden;
                        width: 21px;
                        margin-left: 10px;

                        .booking__btn--effect {
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

                .booking__filter__btn::after {
                    content: 'Filter now';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 29px;
                    color: $shadow-color;
                    @include desktop {
                        left: 34px;
                    }
                }
            }
        }
    }
</style>