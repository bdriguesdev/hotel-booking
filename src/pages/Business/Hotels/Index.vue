<template>
    <div class="business__hotels__container">
        <Header v-on="$listeners" />
        <main class="business__hotels__content">
            <div class="business__hotels__title">
                <span class="business__hotels__number--container">
                    <div class="business__hotels__number--border"></div>
                    <img src="../../../assets/Hotel_icon_white.svg" alt="Hotel icon" class="business__hotels__icon">
                </span>
                <div class="business__hotels__text">
                    <span>Hotels</span>
                    <div class="business__hotels__line"></div>
                </div>
            </div>
            <div class="business__hotels__btns">
                <button class="business__hotels__btn filter-btn" @click="filtersModal('button')" v-on:mouseenter="filtersBtnAnimation">
                    Filters
                    <div class="business__hotels__btn__container">
                        <div class="business__hotels__btn--effect">
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                        </div>
                    </div>
                </button>
                <button class="business__hotels__btn create-btn" @click="createModal('button')" v-on:mouseenter="createBtnAnimation">
                    Create
                    <div class="business__hotels__btn__container">
                        <div class="business__hotels__btn--effect">
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                        </div>
                    </div>
                </button>
            </div>
            <div v-if="hotels !== null" class="business__hotels__cards">
                <HotelCard v-for="(hotel, index) in hotels" :key="index" :hotel="hotel" @modal="hotelModal" />
                <!-- <HotelCard v-if="3+3 > 10" :v-for="(hotel, index) in hotels" :hotel="hotel" :key="index" @modal='hotelModal' /> -->
            </div>
        </main>
        <FilterModal @modal='filtersModal' v-if="isFiltersModalOpened" />
        <CreateModal @modal='createModal' v-if="isCreateModalOpened" />
        <HotelModal @modal='hotelModal' v-if="isHotelModalOpened" />
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Header from '../../../components/Header';
import HotelCard from './HotelCard';
import FilterModal from './FilterModal';
import CreateModal from './CreateModal';
import HotelModal from './HotelModal';

export default {
    name: 'BusinessHotels',
    components: {
        Header,
        HotelCard,
        FilterModal,
        CreateModal,
        HotelModal
    },
    data() {
        return{
            isFiltersBtnAnimationInProgress: false,
            isCreateBtnAnimationInProgress: false,
            isFiltersModalOpened: false,
            isCreateModalOpened: false,
            isHotelModalOpened: false
        }
    },
    created() {
        this.$store.dispatch("getAllUserHotels").hotelsModule;
    },
    mounted() {
        //title animation
        setTimeout(()=> { this.titleAnimation(); }, 1);
    },
    methods: {
        filtersBtnAnimation() {
            if(!this.isFiltersBtnAnimationInProgress) {
                this.isFiltersBtnAnimationInProgress = true;
                const button = document.querySelector('.filter-btn .business__hotels__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isFiltersBtnAnimationInProgress = false;
                }, 500);
            }
        },
        createBtnAnimation() {
            if(!this.isCreateBtnAnimationInProgress) {
                this.isCreateBtnAnimationInProgress = true;
                const button = document.querySelector('.create-btn .business__hotels__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isCreateBtnAnimationInProgress = false;
                }, 500);
            }
        },
        filtersModal(element) {
            if(element === 'button') this.filtersBtnAnimation();
            this.isFiltersModalOpened = !this.isFiltersModalOpened;
        },
        createModal(element) {
            if(element === 'button') this.createBtnAnimation();
            this.isCreateModalOpened = !this.isCreateModalOpened;
        },
        hotelModal(hotel) {
            if(hotel) {
                this.$store.dispatch("setHotelId", { id: hotel.id }).hotelsModule
                this.$store.dispatch("changeHotel", hotel).hotelsModule;
            }
            this.isHotelModalOpened = !this.isHotelModalOpened;
        },
        titleAnimation() {
            const titleNumberBorder = document.querySelector('.business__hotels__number--border');
            const titleTextBorder = document.querySelector('.business__hotels__line');
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
            'hotels'
        ])
    },
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .business__hotels__content {
        max-width: 1800px;
        width: 90%;
        margin: 100px auto;

        .business__hotels__title {
            display: flex;
            justify-content: flex-start;
            @include small-phone {
                flex-direction: column;
            }

            .business__hotels__number--container {
                width: 87px;
                height: 87px;
                background-color: $secondary-color-two;
                overflow: hidden;
                position: relative;

                .business__hotels__number--border {
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

            .business__hotels__text {
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
                    @include large-phone {
                        font-size: 1.7rem;
                    }
                }

                .business__hotels__line {
                    min-width: 80%;
                    visibility: hidden;
                    width: 230px;
                    height: 3px;
                    background-color: $secondary-color-two;
                }
            }
        }

        .business__hotels__btns {
            display: flex;

            .business__hotels__btn {
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

                .business__hotels__btn__container {
                    overflow: hidden;
                    width: 21px;
                    margin-left: 10px;

                    .business__hotels__btn--effect {
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

            .filter-btn::after {
                content: 'Filters';
                position: absolute;
                z-index: -1;
                font-size: 1.063rem;
                top: 13px;
                left: 21px;
                color: $shadow-color;
                @include desktop {
                    left: 24px;
                }
                @include micro-phone {
                    display: none;
                }
            }

            .create-btn {
                margin-left: 20px;
            }

            .create-btn::after {
                content: 'Create';
                position: absolute;
                z-index: -1;
                font-size: 1.063rem;
                top: 13px;
                left: 21px;
                color: $shadow-color;
                @include desktop {
                    left: 23px;
                }
                @include micro-phone {
                    display: none;
                }
            }
        }

        .business__hotels__cards {
            display: grid;
            grid-auto-rows: auto; 
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            grid-gap: 2rem;
            @include small-phone {
                grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            }
        }
    }

</style>