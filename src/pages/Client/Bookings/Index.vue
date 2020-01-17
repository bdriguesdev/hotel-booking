<template>
    <div class="bookings__container">
        <Header v-on="$listeners" />
        <main class="bookings__content">
            <div class="bookings__title">
                <span class="bookings__number--container">
                    <div class="bookings__number--border"></div>
                    <img src="../../../assets/Bookings_icon.svg" alt="Bookings icon" class="bookings__icon">
                </span>
                <div class="bookings__text">
                    <span>Bookings</span>
                    <div class="bookings__line"></div>
                </div>
            </div>
            <button class="bookings__btn" @click="filtersModal('button')" v-on:mouseenter="btnAnimation">
                Filters
                <div class="bookings__btn__container">
                    <div class="bookings__btn--effect">
                        <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                        <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                    </div>
                </div>
            </button>
            <div v-if="bookingLoading === false" class="bookings__cards">
                <BookingCard @modal="reviewModal" v-for="(booking, index) in bookings" :key="index" :booking="booking" />
            </div>
            <div v-else class="lds-ellipsis" :style="{marginTop: '100px'}"><div></div><div></div><div></div><div></div></div>
        </main>
        <FilterModal @modal='filtersModal' v-if="isFiltersModalOpened" />
        <ReviewModal @modal='reviewModal' v-if="isReviewModalOpened" />
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Header from '../../../components/Header';
import BookingCard from './BookingCard';
import FilterModal from './FilterModal';
import ReviewModal from './ReviewModal/Index';

export default {
    name: 'ClientBookings',
    components: {
        Header,
        BookingCard,
        FilterModal,
        ReviewModal
    },
    data() {
        return{
            isFiltersBtnAnimationInProgress: false,
            isFiltersModalOpened: false,
            isReviewModalOpened: false
        }
    },
    created() {
        this.$store.dispatch('changeBookingLoading', true);
        const args = {
            start: null,
            end: null,
            city: null,
            state: null,
            minPrice: null,
            maxPrice: null
        };
        this.$store.dispatch('getBookings', args);
    },
    mounted() {
        //title animation
        setTimeout(()=> { this.titleAnimation(); }, 1);
    },
    methods: {
        btnAnimation() {
            if(!this.isFiltersBtnAnimationInProgress) {
                this.isFiltersBtnAnimationInProgress = true;
                const button = document.querySelector('.bookings__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isFiltersBtnAnimationInProgress = false;
                }, 500);
            }
        },
        reviewModal() {
            this.isReviewModalOpened = !this.isReviewModalOpened;
        },
        filtersModal(element) {
            if(element === 'button') this.btnAnimation();
            this.isFiltersModalOpened = !this.isFiltersModalOpened;
        },
        titleAnimation() {
            const titleNumberBorder = document.querySelector('.bookings__number--border');
            const titleTextBorder = document.querySelector('.bookings__line');
            const titleNumberBorderWidth = titleTextBorder.getBoundingClientRect().width;
            const titleNumberBorderMinWidth = titleTextBorder.style.minWidth;

            this.isSectionTitleAnimated = true;
            titleNumberBorder.style.width = '100%';
            titleTextBorder.style.width = '0px';
            titleTextBorder.style.minWidth = '0%';
            titleTextBorder.style.visibility = 'visible';
            titleTextBorder.getBoundingClientRect();
            titleTextBorder.style.transition = '800ms ease-in-out';
            titleTextBorder.style.width = titleNumberBorderWidth + 'px';
            titleTextBorder.style.minWidth = titleNumberBorderMinWidth + 'px';
        }
    },
    computed: {
        ...mapGetters([
            'bookingLoading',
            'bookings'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';

    .bookings__content {
        max-width: 1800px;
        width: 90%;
        margin: 0 auto;
        margin-top: 100px;

        .bookings__title {
            display: flex;
            justify-content: flex-start;

            .bookings__number--container {
                width: 87px;
                height: 87px;
                background-color: $secondary-color-two;
                overflow: hidden;
                position: relative;

                .bookings__number--border {
                    background-color: $secondary-color-one;
                    height: 3px;
                    width: 0;
                    transition: 800ms ease-in-out;
                    transition-delay: 600ms;
                }

                img {
                    margin-top: 6px;
                }
            }

            .bookings__text {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                justify-content: flex-end;

                span {
                    color: $secondary-color-two;
                    font-size: 1.875rem;
                    font-weight: 300;
                    font-family: $secondary-font;
                    margin-left: 15px;
                    text-transform: uppercase;
                }

                .bookings__line {
                    min-width: 80%;
                    visibility: hidden;
                    width: 230px;
                    height: 3px;
                    background-color: $secondary-color-two;
                }
            }
        }

        .bookings__btn {
            font-family: $primary-font;
            background-color: $secondary-color-one;
            border: none;
            color: $primary-color;
            width: 124px;
            height: 44px;
            font-size: 1.063rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            z-index: 1;
            margin: 20px 0;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.20);
            cursor: pointer;

            .bookings__btn__container {
                overflow: hidden;
                width: 21px;
                margin-left: 10px;

                .bookings__btn--effect {
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

        .bookings__btn::after {
            content: 'Filters';
            position: absolute;
            z-index: -1;
            font-size: 1.063rem;
            top: 13px;
            left: 21px;
            color: $shadow-color;
        }

        .bookings__cards {
            display: grid;
            grid-auto-rows: auto; 
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            grid-gap: 2rem;
        }
    }

</style>