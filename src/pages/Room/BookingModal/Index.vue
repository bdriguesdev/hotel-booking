<template>
    <div class="booking__modal" @click="closeModal">
        <div class="booking__modal__content">
            <nav class="booking__nav">
                <ul>
                    <li>Booking</li>
                </ul>
                <svg v-on:click="$emit('modal')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form class="booking__form" v-on:click.prevent="">
                <div class="booking__inputs__container">
                    <label class='booking__input__start' for='Start date'>
                        Starts at
                        <span class="input__date__container">{{ transformStartDateToText }}</span>
                        <Calendar :type="'Start'" />
                    </label> 
                    <label class='booking__input__end' for='Start date'>
                        Ends at
                        <span class="input__date__container">{{ transformEndDateToText }}</span>
                        <Calendar :type="'End'" />
                    </label> 
                </div>
                <div class="booking__price">
                    <div class='booking__total-price' for="Total price">
                        <span class='booking__price__title'>Total price</span> 
                        <div class="booking__price__info">
                            <span class="booking__price__text">Price per night</span>
                            <div class="booking__price-line"></div>
                            <span class="booking__price-per-night">${{ room.price }}</span>
                        </div>
                        <div class="booking__price__info">
                            <span class="booking__price__text">Nights booked</span>
                            <div class="booking__price-line"></div>
                            <span class="booking__nights">x{{ transformDateToNights }}</span>
                        </div>
                        <div class="booking__price__total">
                            ${{ transformDateToNights * room.price }}
                        </div>
                    </div>
                    <div class="booking__discount">
                        <span>Discount coupon</span>
                        <input type="text" />
                    </div>
                </div>
                <button class="booking__btn" v-on:click="handleBooking" v-on:mouseenter="btnAnimation">
                    Book now
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
import Calendar from './Calendar.vue';
import { mapGetters } from 'vuex';

export default {
    name: 'BookingModal',
    data() {
        return {
            isBtnAnimationInProgress: false,
            startAt: null,
            endAt: null
        }
    },
    props: [
        'room'
    ],
    components: {
        Calendar
    },
    created() {
        this.$store.dispatch('changeBookingStart', null);
        this.$store.dispatch('changeBookingEnd', null);
    },
    mounted() {
        const modal = document.querySelector('.booking__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        changeStartAt(date) {
            this.startAt = date;
        },
        changeEndAt(date) {
            this.endAt = date;
        },
        handleBooking() {
            this.btnAnimation();
            const args = {
                roomId: this.room.id,
                coupon: ''
            };
            this.$store.dispatch('createBooking', args);
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
        },
        closeModal(evt) {
            if(evt.target.className === 'booking__modal') {
                this.$emit('modal');
            }
        }
    },
    computed: {
        ...mapGetters([
            'bookingStart',
            'bookingEnd'
        ]),
        transformDateToNights() {
            if(!this.bookingStart || !this.bookingEnd ) {
                return '0';
            } else {
                //1 day = 86400000 ms
                return (this.bookingEnd - this.bookingStart) / 86400000;
            }
        },
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

    .booking__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .booking__modal__content {
            background-color: $primary-color;
            width: 710px;
            margin: 0 auto;
            margin-top: 10vh;

            .booking__nav {
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

            .booking__form {
                padding-top: 28px;
                padding-bottom: 36px;  
                padding-left: 44px;  
                padding-right: 44px;  

                .booking__inputs__container {
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

                .booking__price {

                    .booking__total-price {
                        display: flex;
                        flex-direction: column;
                        align-items: flex-start;

                        .booking__price__title {
                            color: $secondary-color-two;
                            font-family: $secondary-font;
                            font-weight: 300;
                            font-size: 1rem;
                            text-transform: uppercase;
                            margin: 10px 0;
                        }

                        .booking__price__info {
                            display: flex;
                            justify-content: space-between;
                            align-items: center;
                            width: 100%;
                            position: relative;
                            overflow: hidden;

                            span {
                                margin: 3px 0;
                                margin-left: 15px;
                            }

                            .booking__price__text {
                                background-color: $primary-color;
                                position: relative;
                                z-index: 1;
                                min-width: 130px;
                                color: $secondary-color-two;
                                font-weight: 300;
                                font-size: 1rem;
                                text-align: left;
                            }

                            .booking__price-line {
                                position: absolute;
                                left: 0;
                                z-index: 0;
                                height: 1px;
                                width: 100%;
                                margin: 0 auto;
                                background-color: $divisor-color;
                                margin-left: 20px;
                            }

                            .booking__price-per-night {
                                background-color: $primary-color;
                                position: relative;
                                z-index: 1;
                                min-width: 70px;
                                text-align: right;
                                color: $secondary-color-two;
                                font-weight: 400;
                                font-size: 1rem;
                            }

                            .booking__nights {
                                background-color: $primary-color;
                                position: relative;
                                z-index: 1;
                                min-width: 70px;
                                text-align: right;
                                color: $secondary-color-two;
                                font-weight: 300;
                                font-size: 1rem;
                            }
                        }

                        .booking__price__total {
                            color: $secondary-color-two;
                            font-weight: 500;
                            font-size: 1.125rem;
                            width: 100%;
                            text-align: right;
                            margin-top: 3px;
                        }
                        
                    }
                    
                    .booking__discount {
                        display: flex;
                        flex-direction: column;

                        span {
                            text-align: left;
                            margin-bottom: 5px;
                            font-family: $secondary-font;
                            color: $secondary-color-two;
                            font-size: 1rem;
                            text-transform: uppercase;
                            text-align: left;
                        }

                        input {
                            width: 140px;
                            height: 35px;
                            background-color: $input-bg-color;
                            border: none;
                            border-bottom: 2px solid $secondary-color-two;
                            outline: none;
                            padding: 0 10px;
                            font-size: 1rem;
                            color: $input-text-color;
                            box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                            border-radius: 0;
                        }
                    }
                }
                
                .booking__btn {
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

                .booking__btn::after {
                    content: 'Book now';
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