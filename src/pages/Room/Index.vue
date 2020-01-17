<template>
    <div class="room__container">
        <Header v-on="$listeners" />
        <main v-if="roomLoading === false" class="room__content">
            <div class="room__slide">
                <div class="room__imgs__container">
                    <div :style="room.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${room.photos[0].photo}')` }: {}" alt="Room image" class="room__slide__main-img"></div>
                    <div alt="Room image" class="room__slide__main-img"></div>
                    <div alt="Room image" class="room__slide__main-img"></div>
                </div>
                <button class="room__slide__arrow room__slide__arrow--left" v-on:click='changeSlideCard("left")'>
                    <div class="room__slide__arrow--container">
                        <div class="room__slide__arrow--effect">
                            <img src="../../assets/Slide_arrow_left.svg" alt="Slide left arrow" />
                            <img src="../../assets/Slide_arrow_left.svg" alt="Slide left arrow" />
                        </div>
                    </div>
                </button>
                <button class="room__slide__arrow room__slide__arrow--right" v-on:click='changeSlideCard("right")'>
                    <div class="room__slide__arrow--container">
                        <div class="room__slide__arrow--effect">
                            <img src="../../assets/Slide_arrow_one.svg" alt="Slide right arrow" />
                            <img src="../../assets/Slide_arrow_one.svg" alt="Slide right arrow" />
                        </div>
                    </div>
                </button>
            </div>
            <div class="room__slide__time"></div>
            <div class="room__information">
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
                <div class="room__description">
                    <div class="room__title">
                        <div class="room__title__left">
                            <img src="../../assets/Room_description_icon.svg" alt="Room description icon" class="room__description--icon">
                            <div class="room__title__info">
                                <p>{{ room.hotel.city }}, {{ room.hotel.state }}</p>
                                <h2>{{ room.name }}</h2>
                            </div>
                        </div>
                        <div class="room__title__right">
                            <div class="room__people">
                                <img src="../../assets/Room_people_icon.svg" alt="People icon" class="room__description__people--icon">
                                <span>2</span>
                            </div>
                            <span class="room__price">${{ room.price }}</span>
                            <span class="room__title--division"></span>
                            <button class="btn room__booking--btn" v-on:click="bookingModal('button')" v-on:mouseenter="bookingBtnAnimation">
                                <span>Book now</span>
                                <div class="room__booking--btn--container">
                                    <div class="room__booking--btn--effect">
                                        <img src="../../assets/Button_arrow_one.svg" alt="Button arrow - animation asset" />
                                        <img src="../../assets/Button_arrow_one.svg" alt="Button arrow" />
                                    </div>
                                </div>
                            </button>
                        </div>
                    </div>
                    <p class="room__description__text">
                        {{ room.description }}
                    </p>
                </div>
                <div class="room__amenities">
                    <div class="room__title">
                        <img src="../../assets/Room_amenities_icon.svg" alt="Room amenities icon" class="room__amenities--icon">
                        <h2>Amenities</h2>
                    </div>
                    <ul>
                        <li><img src="../../assets/Room_amenities_list_icon.svg" alt="Amenities list icon" class="room__amenities__list--icon">Lorem Ipsum</li>
                        <li><img src="../../assets/Room_amenities_list_icon.svg" alt="Amenities list icon" class="room__amenities__list--icon">Lorem Ipsum</li>
                        <li><img src="../../assets/Room_amenities_list_icon.svg" alt="Amenities list icon" class="room__amenities__list--icon">Lorem Ipsum</li>
                        <li><img src="../../assets/Room_amenities_list_icon.svg" alt="Amenities list icon" class="room__amenities__list--icon">Lorem Ipsum</li>
                    </ul>
                </div>
                <div class="room__hotel">
                    <div class="room__title">
                        <img @click="changeLink" src="../../assets/Room_hotel_icon.svg" alt="Room hotel icon" class="room__hotel--icon">
                        <h2 @click="changeLink" >Hotel</h2>
                    </div>
                    <p class="room__hotel__text">
                        {{ room.hotel.description }}
                    </p>
                </div>
                <div class="room__reviews">
                    <div class="room__title">
                        <img src="../../assets/Room_reviews_icon.svg" alt="Room reviews icon" class="room__reviews--icon">
                        <h2>Reviews</h2>
                    </div>
                    <div v-if="reviews && bookingLoading === false">
                        <Review v-for="(review, index) in reviews" :key="index" :review="review" />
                        <div v-if="reviews.length === 0" class="no-results">
                            This room doesn't have any review.
                        </div>
                    </div>
                    <div v-else-if="bookingLoading" class="lds-ellipsis" :style="{ marginTop: '20px' }"><div></div><div></div><div></div><div></div></div>
                </div>
            </div>
        </main>
        <div v-else class="lds-ellipsis" :style="{ marginTop: '40vh' }"><div></div><div></div><div></div><div></div></div>
        <BookingModal  v-if="isBookingModalOpened" v-on:modal="bookingModal" :room="room" />
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Header from '../../components/Header';
import Review from '../../components/Review';
import BookingModal from './BookingModal/Index';

export default {
    name: 'Room',
    components: {
        Header,
        Review,
        BookingModal
    },
    data() {
        return {
            isSlideAnimationInProgress: false,
            isBookingBtnAnimationInProgress: false,
            card: 1,
            maxCard: 3,
            isBookingModalOpened: false
        }
    },
    beforeCreate() {
        this.$store.dispatch('changeRoomLoading', true);
        this.$store.dispatch('changeBookingLoading', true);
    },
    created() {
        this.$store.dispatch('getRoom', { roomId: this.$route.params.id }).roomModules;
    },
    methods: {
        changeLink() {
            this.$router.push({ path: `/hotel/${this.room.hotel.id}/` });
        },
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
            const arrow = document.querySelector(`.room__slide__arrow--${arrowDirection} .room__slide__arrow--effect`);
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
        },
        bookingBtnAnimation() {
            if(!this.isBookingBtnAnimationInProgress) {
                const button = document.querySelector('.room__booking--btn--effect');

                this.isBookingBtnAnimationInProgress = true;
                button.style.animation = "booking-btn-animation 500ms ease-in-out 1";
                setTimeout(() => {
                    this.isBookingBtnAnimationInProgress = false;
                    button.style.animation = '';
                }, 500);
            }
        },
        bookingModal(element) {
            if(element === 'button') this.bookingBtnAnimation();
            this.isBookingModalOpened = !this.isBookingModalOpened;
            window.scroll(0, 0); 
        }
    },
    computed: {
        ...mapGetters([
            'room',
            'roomLoading',
            'reviews',
            'bookingLoading'
        ])
    },
    watch: {
        card(newValue, oldValue) {
            const roomSlideContainer = document.querySelector('.room__imgs__container');
            const slidesTracks = document.querySelectorAll('.slide__track svg circle');

            this.modifySlideTrack(slidesTracks[newValue - 1], slidesTracks[oldValue - 1]);
            roomSlideContainer.style.left = -((this.card - 1) * 100) + '%';
        }
    }
}
</script>

<style lang='scss'>
    @import '../../scss/variables.scss';
    @import '../../scss/mixins.scss';

    .room__content {
        width: 90%;
        max-width: 1070px;
        margin: 0 auto;
        margin-top: 100px;
        
        .room__slide {
            display: flex;
            position: relative;
            overflow: hidden;

            .room__imgs__container {
                position: relative;
                left: 0;
                display: flex;
                min-width: 300%;
                transition: 500ms ease-in-out;

                .room__slide__main-img {
                    height: 540px;
                    width: 100%;
                    background-image: url("../../assets/Room_card_one.jpg");
                    background-size: cover;
                    background-position: center;
                }
            }

            .room__slide__arrow {
                position: absolute;
                background-color: $secondary-color-one;
                width: 81px;
                height: 53px;
                border: none;
                cursor: pointer;

                .room__slide__arrow--container {
                    width: 50px;
                    margin: 0 auto;
                    overflow: hidden;
                    
                    .room__slide__arrow--effect {
                        display: flex;
                        justify-content: space-between;
                        width: 300%;
                    }
                }
            }

            .room__slide__arrow--left {
                left: 0;
                top: 50%;
                transform: translateY(-50%);

                .room__slide__arrow--effect {
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

            

            .room__slide__arrow--right {
                right: 0;
                top: 50%;
                transform: translateY(-50%);

                .room__slide__arrow--effect {
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

        .room__slide__time {
            height: 3px;
            width: 100%;
            background-color: $secondary-color-one;
        }

        .room__information {
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

        .room__description {
            padding-bottom: 25px;
            border-bottom: 1px solid $divisor-color;

            .room__title {
                display: flex;
                justify-content: space-between;
                align-items: flex-end;
                margin-bottom: 25px;
                flex-wrap: wrap;
                @include large-phone {
                    flex-direction: column;
                    align-items: flex-start;
                }

                .room__title__left {
                    display: flex;

                    .room__title__info {
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
                            text-align: left;
                        }
                    }
                }

                .room__title__right {
                    display: flex;
                    align-self: center;
                    align-items: center;
                    flex-wrap: wrap;
                    @include large-phone {
                        margin-top: 25px;
                        flex-direction: row-reverse;
                        align-self: flex-start;
                    }
                    @include small-phone {
                        align-self: center;
                        justify-content: center;
                    }
                    
                    .room__people {
                        margin-right: 20px;
                        display: flex;
                        align-items: center;
                        @include small-phone {
                            margin-right: 0;
                        }

                        span {
                            color: $secondary-color-two;
                            font-family: $secondary-font;
                            font-size: 1.25rem;
                            font-weight: 300;
                            margin-left: 5px;
                            margin-top: 4px;
                        }
                    } 

                    .room__price {
                        color: $secondary-color-two;
                        font-size: 1.563rem;
                        font-weight: 400;
                        margin-right: 20px;
                    }

                    .room__title--division {
                        width: 1px;
                        background-color: $divisor-color;
                        height: 40px;
                        margin-right: 20px;
                        @include large-phone {
                            margin-left: 25px;
                        }
                        @include medium-phone {
                            display: none;
                        }
                    }

                    .room__booking--btn {
                        background-color: $secondary-color-one;
                        border: 2px solid $secondary-color-one;
                        display: inline-block;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        width: 195px;
                        height: 50px;
                        box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
                        cursor: pointer;
                        opacity: 0;
                        animation: btn-appears-animation 1000ms ease-in-out 1;
                        animation-fill-mode: forwards;
                        animation-delay: 150ms;
                        @include tablet {
                            width: 145px;
                        }
                        @include medium-phone {
                            margin-right: 10px;
                        }
                        @include small-phone {
                            margin-top: 10px;
                        }   

                        span {
                            margin-right: 5px;
                            font-size: 1.25rem;
                            color: $primary-color;
                            position: relative;
                            z-index: 2;
                            @include tablet {
                                font-size: 1.1rem;
                            }
                        }

                        span:after {
                            content: 'Book now';
                            position: absolute;
                            color: $shadow-color;
                            width: 100%;
                            top: 1px;
                            left: -2px;
                            z-index: -1;
                        }

                        .room__booking--btn--container {
                            margin-left: 5px;
                            overflow: hidden;
                            width: 21px;

                            .room__booking--btn--effect {
                                position: relative;
                                left: -200%;
                                width: 300%;
                                display: flex;
                                justify-content: space-between;
                                height: 100%;
                            }

                            @keyframes booking-btn-animation {
                                100% {
                                    left: -1px;
                                }
                            }

                        }

                    }
                }
            }            

            .room__description__text {
                margin: 0 10px;
                text-align: left;
                text-indent: 30px;
                line-height: 160%;
                color: $gray-text-color;
                font-size: 1.063rem;
                font-weight: 300;
            }
        }

        .room__title {
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

        .room__amenities {
            margin-top: 25px;
            padding-bottom: 25px;
            border-bottom: 1px solid $divisor-color;

            ul {
                list-style: none;
                padding: 0;
                margin: 0;
                display: flex;
                margin: 0 10px;
                flex-wrap: wrap;

                li {
                    font-size: 1.063rem;
                    color: $gray-text-color;
                    font-weight: 300;
                    margin: 0 10px;
                    
                    img {
                        margin-right: 5px;
                    }
                }
            }
        }

        .room__hotel {
            margin-top: 25px;
            padding-bottom: 25px;
            border-bottom: 1px solid $divisor-color;

            .room__title {
                h2 {
                    cursor: pointer;
                }

                img {
                    cursor: pointer;
                }
            }

            .room__hotel__text {
                margin: 0;
                margin: 0 10px;
                text-align: left;
                text-indent: 30px;
                line-height: 160%;
                color: $gray-text-color;
                font-size: 1.063rem;
                font-weight: 300;
            }
        }

        .room__reviews {
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