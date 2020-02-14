<template>
    <div class="hotel__container">
        <Header v-on="$listeners" />
        <main v-if="hotelLoading === false" class="hotel__content">
            <div class="hotel__slide">
                <div class="hotel__imgs__container">
                    <div alt="Hotel image" :style="hotel.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${hotel.photos[0].photo}')` }: {}" class="hotel__slide__main-img"></div>
                    <div alt="Hotel image" class="hotel__slide__main-img"></div>
                    <div alt="Hotel image" class="hotel__slide__main-img"></div>
                </div>
                <button class="hotel__slide__arrow hotel__slide__arrow--left" v-on:click='changeSlideCard("left")'>
                    <div class="hotel__slide__arrow--container">
                        <div class="hotel__slide__arrow--effect">
                            <img src="../../assets/Slide_arrow_left.svg" alt="Slide left arrow" />
                            <img src="../../assets/Slide_arrow_left.svg" alt="Slide left arrow" />
                        </div>
                    </div>
                </button>
                <button class="hotel__slide__arrow hotel__slide__arrow--right" v-on:click='changeSlideCard("right")'>
                    <div class="hotel__slide__arrow--container">
                        <div class="hotel__slide__arrow--effect">
                            <img src="../../assets/Slide_arrow_one.svg" alt="Slide right arrow" />
                            <img src="../../assets/Slide_arrow_one.svg" alt="Slide right arrow" />
                        </div>
                    </div>
                </button>
            </div>
            <div class="hotel__slide__time"></div>
            <div class="hotel__information">
                <div class="slide__track">
                    <svg v-on:click="changeSlideTrack(1)" width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="6.5" cy="6.5" r="5.5" fill="#FF1E1E" stroke="#FF1E1E" stroke-width="2"/>
                    </svg>
                    <svg v-on:click="changeSlideTrack(2)" width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="6.5" cy="6.5" r="5.5" fill="none" stroke="black" stroke-width="2"/>
                    </svg>
                    <svg v-on:click="changeSlideTrack(3)" width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="6.5" cy="6.5" r="5.5" fill="none" stroke="black" stroke-width="2"/>
                    </svg>
                </div>
                <div class="hotel__description">
                    <div class="hotel__title">
                        <div class="hotel__title__left">
                            <img src="../../assets/Room_hotel_icon.svg" alt="Hotel description icon" class="hotel__description--icon">
                            <div class="hotel__title__info">
                                <p>{{ hotel.city }}, {{ hotel.state }}</p>
                                <h2>{{ hotel.name }}</h2>
                            </div>
                        </div>
                    </div>
                    <p class="hotel__description__text">
                        {{ hotel.description }}
                    </p>
                </div>
                <div class="hotel__rooms">
                    <div class="hotel__title">
                        <img src="../../assets/Room_description_icon.svg" alt="Hotel icon" class="hotel__hotel--icon">
                        <h2>Rooms</h2>
                    </div>
                    <div v-if="hotelRooms && roomLoading === false" class="hotel__rooms__container">
                        <div v-if="hotelRooms.length > 0"> 
                            <RoomCard v-for="(room, index) in hotelRooms" :key="index" :room="room" />
                        </div>
                        <div v-else class="no-results">
                            This hotel doesn't have any review.
                        </div>
                    </div>
                    <div v-else class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
                </div>
                <div class="hotel__reviews">
                    <div class="hotel__title">
                        <img src="../../assets/Room_reviews_icon.svg" alt="Hotel reviews icon" class="hotel__reviews--icon">
                        <h2>Lastest room reviews</h2>
                    </div>
                    <div v-if="reviews && bookingLoading === false" >
                        <Review v-for="(review, index) in reviews" :key="index" :review="review" />
                        <div v-if="reviews.length === 0" class="no-results">
                            This hotel doesn't have any review.
                        </div>
                    </div>
                    <div v-else-if="bookingLoading" class="lds-ellipsis" :style="{ marginTop: '20px' }"><div></div><div></div><div></div><div></div></div>
                </div>
            </div>
        </main>
        <div v-else class="lds-ellipsis" :style="{ marginTop: '40vh' }"><div></div><div></div><div></div><div></div></div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Header from '../../components/Header';
import RoomCard from './RoomCard';
import Review from '../../components/Review';

export default {
    name: 'Hotel',
    components: {
        Header,
        RoomCard,
        Review
    },
    data() {
        return {
            isSlideAnimationInProgress: false,
            card: 1,
            maxCard: 3
        }
    },
    beforeCreate() {
        this.$store.dispatch('changeLoading', true).hotelsModule;
        this.$store.dispatch('changeBookingLoading', true);
    },
    created() {
        this.$store.dispatch('getHotel', { hotelId: this.$route.params.id }).hotelsModule;
        this.$store.dispatch('getAllRoomsFromOneHotel').roomsModule;
    },
    methods: {
        changeSlideCard(direction) {
            if(!this.isSlideAnimationInProgress) {
                this.slideArrowAnimation(direction);
                if(direction === 'left') {

                    this.isSlideAnimationInProgress = true;
                    if(this.card === 1) {
                        this.card = this.maxCard;
                    } else {
                        this.card--;
                    }

                } else {
                    this.isSlideAnimationInProgress = true;
                    if(this.card === this.maxCard) {
                        this.card = 1;
                    } else {
                        this.card++;
                    }

                }
                setTimeout(() => {
                    this.isSlideAnimationInProgress = false;
                }, 500);
            }
        },
        slideArrowAnimation(arrowDirection) {
            const arrow = document.querySelector(`.hotel__slide__arrow--${arrowDirection} .hotel__slide__arrow--effect`);
            arrow.style.animation = `arrow-${arrowDirection}-animation 500ms ease-in-out 1`;
            setTimeout(() => {
                arrow.style.animation = '';
            }, 500);
        },
        changeSlideTrack(value) {
            this.card = value;
        },
        modifySlideTrack(active, deactive) {
            active.style.fill = '#FF1E1E';
            active.style.stroke = '#FF1E1E';
            deactive.style.fill = 'none';
            deactive.style.stroke = 'black';
        }
    },
    computed: {

        ...mapGetters([
            'hotel',
            'hotelLoading',
            'hotelRooms',
            'roomLoading',
            'bookingLoading',
            'reviews'
        ])
    },
    watch: {
        card(newValue, oldValue) {
            const hotelSlideContainer = document.querySelector('.hotel__imgs__container');
            const slidesTracks = document.querySelectorAll('.slide__track svg circle');

            this.modifySlideTrack(slidesTracks[newValue - 1], slidesTracks[oldValue - 1]);
            hotelSlideContainer.style.left = -((this.card - 1) * 100) + '%';
        }
    }
}
</script>

<style lang='scss'>
    @import '../../scss/variables.scss';
    @import '../../scss/mixins.scss';

    .hotel__content {
        width: 90%;
        max-width: 1070px;
        margin: 100px auto;
        
        .hotel__slide {
            display: flex;
            position: relative;
            overflow: hidden;

            .hotel__imgs__container {
                position: relative;
                left: 0;
                display: flex;
                min-width: 300%;
                transition: 500ms ease-in-out;

                .hotel__slide__main-img {
                    height: 540px;
                    width: 100%;
                    background-image: url("../../assets/Room_card_one.jpg");
                    background-size: cover;
                    background-position: center;
                }
            }

            .hotel__slide__arrow {
                position: absolute;
                background-color: $secondary-color-one;
                width: 81px;
                height: 53px;
                border: none;
                cursor: pointer;

                .hotel__slide__arrow--container {
                    width: 50px;
                    margin: 0 auto;
                    overflow: hidden;
                    
                    .hotel__slide__arrow--effect {
                        display: flex;
                        justify-content: space-between;
                        width: 300%;
                    }
                }
            }

            .hotel__slide__arrow--left {
                left: 0;
                top: 50%;
                transform: translateY(-50%);

                .hotel__slide__arrow--effect {
                    position: relative;
                    display: flex;
                    justify-content: space-between;
                    left: 0;
                    width: 300%;
                }
                
                @keyframes arrow-left-animation {
                    100% {
                            left: -200%;
                        }
                }
            }

            

            .hotel__slide__arrow--right {
                right: 0;
                top: 50%;
                transform: translateY(-50%);

                .hotel__slide__arrow--effect {
                    position: relative;
                    display: flex;
                    justify-content: space-between;
                    width: 300%;
                    right: 200%;
                }

                @keyframes arrow-right-animation {
                    100% {
                        right: 0;
                    }
                }
            }
        }

        .hotel__slide__time {
            height: 3px;
            width: 100%;
            background-color: $secondary-color-one;
        }

        .hotel__information {
            box-shadow: 0 0 10px rgba(0,0,0,0.15);
            padding: 40px;
        }

        .slide__track {
            margin: 0 auto;
            margin-bottom: 40px;

            svg:nth-child(2) {
                margin: 0 10px;
            }

            svg {
                cursor: pointer;

                circle {
                    transition: 150ms ease-in-out;
                }
            }
        }

        .hotel__description {
            padding-bottom: 25px;
            border-bottom: 1px solid $divisor-color;

            .hotel__title {
                display: flex;
                justify-content: space-between;
                align-items: flex-end;
                margin-bottom: 25px;

                .hotel__title__left {
                    display: flex;

                    .hotel__title__info {
                        display: flex;
                        flex-direction: column;
                        align-items: flex-start;
                        justify-content: flex-end;
                        margin-left: 12px;

                        p {
                            margin: 0;
                            font-family: $secondary-font;
                            color: $secondary-color-one;
                            font-weight: 100;
                            font-size: 0.875rem;
                            text-transform: uppercase;
                        }

                        h2 {
                            margin: 0;
                            font-family: $secondary-font;
                            color: $secondary-color-two;
                            font-weight: 300;
                            font-size: 1.563rem;
                            text-transform: uppercase;
                        }
                    }
                }
            }            

            .hotel__description__text {
                margin: 0 10px;
                text-align: left;
                text-indent: 30px;
                line-height: 160%;
                color: $gray-text-color;
                font-size: 1.063rem;
                font-weight: 300;
            }
        }

        .hotel__title {
            display: flex;
            align-items: flex-end;
            margin-bottom: 25px;

            h2 {
                margin: 0;
                margin-left: 12px;
                font-family: $secondary-font;
                color: $secondary-color-two;
                font-weight: 300;
                font-size: 1.563rem;
                text-transform: uppercase;
            }
        }

        .hotel__rooms {
            padding: 25px 0;
            border-bottom: 1px solid $divisor-color;

            .hotel__rooms__container {
                display: grid;
                grid-auto-rows: auto; 
                grid-template-columns: repeat(auto-fill, minmax(300px, 0.5fr));
                grid-gap: 2rem;
                @include small-phone {
                    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
                }
            }
        }

        .hotel__reviews {
            margin-top: 25px;

            .no-results {
                font-size: 1.2rem;
                font-weight: 300;
                color: lightgray;
                font-family: $secondary-font;
            }
        }
    }
</style>