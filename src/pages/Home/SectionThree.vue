<template>
    <section class="hotels-cards">
        <div class="hotels-cards__title">
            <span class="hotels-cards__number--container">
                <div class="hotels-cards__number--border"></div>
                <span class="hotels-cards__number">2</span>
            </span>
            <div class="hotels-cards__text">
                <h2>Check out some popular <span>hotels</span></h2>
                <div class="hotels-cards__line"></div>
            </div>
        </div>
        <div class="hotels-cards__overflow">
            <div v-if="hotelLoading === false" class="hotels-cards__cards">
                <div @click="changeLink(hotel.id)" v-for="(hotel, index) in hotels" :key='index' class="hotels-cards__card">
                    <div class="hotels-cards__image" :style="hotel.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${hotel.photos[0].photo}')` }: {}"></div>
                    <div class="hotels-cards__information">
                        <div class="hotels-cards__information--first-line">
                            <div class="hotels-cards__main">
                                <p class="hotels-cards__location">{{ hotel.city }}, {{ hotel.state }}</p>
                                <h3 class="hotels-cards__name">{{ hotel.name }}</h3>
                            </div> 
                        </div>
                        <div class="hotels-cards__information--second-line">
                            <p class="hotels-cards__description">
                                {{ hotel.description }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
            <button class="hotel-cards__arrow hotel-cards__arrow--left" v-on:click="handleCardSwipe('left')">
                <div class="hotel-cards__arrow--effect--container">
                    <div class="hotel-cards__arrow--effect--left">
                        <img src="../../assets/Rooms_cards_arrow_left.svg" alt="Arrow to swipe cards left">
                        <img src="../../assets/Rooms_cards_arrow_left.svg" alt="Arrow left effect asset">
                    </div>
                </div>
            </button>
            <button class="hotel-cards__arrow hotel-cards__arrow--right" v-on:click="handleCardSwipe('right')">
                <div class="hotel-cards__arrow--effect--container">
                    <div class="hotel-cards__arrow--effect--right">
                        <img src="../../assets/Rooms_cards_arrow_right.svg" alt="Arrow to swipe cards right">
                        <img src="../../assets/Rooms_cards_arrow_right.svg" alt="Arrow right effect asset">
                    </div>
                </div>
            </button>
        </div>
    </section>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: 'SectionThree',
    data() {
        return {
            sectionWidth: null,
            card: 1,
            isArrowAnimatioInProgress: false,
            isSectionTitleAnimated: false
        }
    },
    beforeCreate() {
        this.$store.dispatch('changeLoading', true).hotelsModule;
    },
    created() {
        this.$store.dispatch('getMostPopularHotels').then(() => {
            const sectionTwo = document.querySelector('.hotels-cards').getBoundingClientRect();
            this.sectionWidth = sectionTwo.width;
        });
    },
    mounted() {
        window.addEventListener('resize', this.resize);
        document.addEventListener('scroll', this.titleAnimation);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.resize);
        document.removeEventListener('scroll', this.titleAnimation);
    },
    methods: {
        changeLink(hotelId) {
            this.$router.push({ path: `/hotel/${hotelId}/` });
        },
        handleCardSwipe(direction) {
            if(!this.isArrowAnimatioInProgress) {
                if(direction === 'left' && this.card < 4 && this.card >= 1) {
                    const roomCardsContainer = document.querySelector('.hotels-cards__cards');
                    const roomCard = document.querySelector('.hotels-cards__card');
                    const distanceToMove = (roomCard.offsetLeft * 2) + roomCard.getBoundingClientRect().width;
                    const arrow = document.querySelector('.hotel-cards__arrow--effect--left');

                    this.isArrowAnimatioInProgress = true;

                    //btn effect
                    arrow.style.animation = 'arrow-left 500ms ease-in-out 1';

                    this.card++;
                    //Here the left is negative so I'm "adding" these two variables
                    roomCardsContainer.style.transition = "500ms ease-in-out";
                    roomCardsContainer.style.left = parseFloat(roomCardsContainer.style.left.split('px')[0]) - distanceToMove + 'px';
                    setTimeout(() => {
                        roomCardsContainer.style.transition = "";
                        arrow.style.animation = '';
                        this.isArrowAnimatioInProgress = false;
                    }, 500)
                } else if(direction === 'right' && this.card > 1 && this.card <= 4) {
                    const roomCardsContainer = document.querySelector('.hotels-cards__cards');
                    const roomCard = document.querySelector('.hotels-cards__card');
                    const distanceToMove = (roomCard.offsetLeft * 2) + roomCard.getBoundingClientRect().width;
                    const arrow = document.querySelector('.hotel-cards__arrow--effect--right');

                    this.isArrowAnimatioInProgress = true;

                    //btn effect
                    arrow.style.animation = 'arrow-right 500ms ease-in-out 1';

                    this.card--;
                    roomCardsContainer.style.transition = "500ms ease-in-out";
                    roomCardsContainer.style.left = parseFloat(roomCardsContainer.style.left.split('px')[0]) + distanceToMove + 'px';   
                    setTimeout(() => {
                        roomCardsContainer.style.transition = "";
                        arrow.style.animation = '';
                        this.isArrowAnimatioInProgress = false;
                    }, 500)
                }
            }
        },
        titleAnimation() {
            const section = document.querySelector('.hotels-cards').getBoundingClientRect();
            if(section.top <= window.innerHeight * 0.75 && !this.isSectionTitleAnimated) {
                this.isSectionTitleAnimated = true;

                const titleNumber = document.querySelector('.hotels-cards__number');
                titleNumber.style.top = '-41px';

                const titleNumberBorder = document.querySelector('.hotels-cards__number--border');
                titleNumberBorder.style.width = '100%';

                const titleTextBorder = document.querySelector('.hotels-cards__line');
                const titleNumberBorderWidth = titleTextBorder.getBoundingClientRect().width;
                const titleNumberBorderMinWidth = titleTextBorder.style.minWidth;
                titleTextBorder.style.width = '0px';
                titleTextBorder.style.minWidth = '0%';
                titleTextBorder.style.visibility = 'visible';
                titleTextBorder.getBoundingClientRect();
                titleTextBorder.style.transition = '800ms ease-in-out';
                titleTextBorder.style.width = titleNumberBorderWidth + 'px';
                titleTextBorder.style.minWidth = titleNumberBorderMinWidth + 'px';
            }
        },
        resize() {
            const sectionTwo = document.querySelector('.hotels-cards').getBoundingClientRect();
            this.sectionWidth = sectionTwo.width;
        }
    },
    computed: {
        ...mapGetters([
            'hotels',
            'hotelLoading'
        ])
    },
    watch: {
        sectionWidth(newValue) {
            const roomCardsContainer = document.querySelector('.hotels-cards__cards');
            const roomCard = document.querySelector('.hotels-cards__card');
            const leftValue = ((roomCardsContainer.getBoundingClientRect().width - newValue) + newValue / 2) - (roomCard.offsetLeft + roomCard.getBoundingClientRect().width / 2);
            const cardPosition = (4 - this.card) * (roomCard.offsetLeft * 2 + roomCard.getBoundingClientRect().width);
            roomCardsContainer.style.left = -leftValue + cardPosition + 'px';
        },
        card(newValue, oldValue) {
            if(newValue === 1) {
                const rightArrow = document.querySelector('.hotel-cards__arrow--right');
                rightArrow.style.opacity = 0;
                rightArrow.style.cursor = 'auto';
                setTimeout(() => {
                    rightArrow.style.visibility = 'hidden';
                }, 250);
            } else if(newValue === 4) {
                const leftArrow = document.querySelector('.hotel-cards__arrow--left');
                leftArrow.style.opacity = 0;
                leftArrow.style.cursor = 'auto';
                setTimeout(() => {
                    leftArrow.style.visibility = 'hidden';
                }, 250);
            }

            if(oldValue === 1) {
                const rightArrow = document.querySelector('.hotel-cards__arrow--right');
                rightArrow.style.visibility = 'visible';
                rightArrow.style.cursor = 'pointer';
                rightArrow.style.opacity = 1;
            } else if(oldValue === 4) {
                const leftArrow = document.querySelector('.hotel-cards__arrow--left');
                leftArrow.style.visibility = 'visible';
                leftArrow.style.cursor = 'pointer';
                leftArrow.style.opacity = 1;
            }
        }
    }
}
</script>

<style lang='scss'>
    @import '../../scss/variables.scss';

    .hotels-cards {
        max-width: 1900px;
        width: 100%;
        margin: 0 auto;
        margin-top: 100px;
        position: relative;

        .hotels-cards__title {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 45px;
            margin-right: 5%;

            .hotels-cards__number--container {
                width: 87px;
                height: 87px;
                background-color: $secondary-color-two;
                overflow: hidden;
                position: relative;

                .hotels-cards__number--border {
                    background-color: $secondary-color-one;
                    height: 3px;
                    width: 0;
                    transition: 800ms ease-in-out;
                    transition-delay: 600ms;
                }

                .hotels-cards__number {
                    font-size: 9.375rem;
                    color: $primary-color;
                    font-weight: 700;
                    position: absolute;
                    left: -13px;
                    top: -150px;
                    position: blue;
                    transition: 800ms ease-in-out;
                }
            }

            .hotels-cards__text {
                display: flex;
                flex-direction: column;
                justify-content: flex-end;
                
                h2 {
                    margin: 0;
                    color: $secondary-color-two;
                    text-align: left;
                    margin-left: 10px;
                    font-size: 1.875rem;
                    font-weight: 400;

                    span {
                        color: $secondary-color-two;
                        font-size: 1.875rem;
                        font-weight: 300;
                        font-family: $secondary-font;
                    }
                }

                .hotels-cards__line {
                    min-width: 80%;
                    visibility: hidden;
                    width: 367px;
                    height: 3px;
                    background-color: $secondary-color-two;
                }
            }
        }

        .hotels-cards__overflow {
            position: relative;
            overflow: hidden;
            padding: 20px 0;

            .hotels-cards__cards {
                position: relative;
                display: flex;
                margin: 0 auto;
                width: 2360px;

                .hotels-cards__card {
                    width: 450px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.2);
                    margin: 0 70px;
                    background-color: $primary-color;
                    cursor: pointer;

                    .hotels-cards__image {
                        background-image: url('../../assets/Room_card_one.jpg');
                        background-size: 100%;
                        background-position: center; 
                        background-color: lightgray;
                        width: 100%;
                        height: 255px;
                        transition: 300ms ease-in-out;
                    }

                    .hotels-cards__information {

                        .hotels-cards__information--first-line {
                            display: flex;
                            justify-content: space-between;
                            align-items: flex-start;
                            margin: 20px 20px;
                            margin-bottom: 0px;

                            .hotels-cards__main {
                                
                                p {
                                    margin: 0;
                                    color: $secondary-color-one;
                                    text-align: left;
                                    text-transform: uppercase;
                                    font-size: 0.875rem;
                                    font-weight: 300;
                                }

                                h3 {
                                    margin: 0;
                                    color: $secondary-color-two;
                                    font-size: 1.25rem;
                                    font-weight: 400;
                                    text-align: left;
                                }
                            }
                        }

                        .hotels-cards__information--second-line {
                            margin: 0 20px;
                            margin-top: 10px;
                            padding-bottom: 20px;

                            .hotels-cards__description {
                                margin: 0;
                                color: $light-gray-text-color;
                                text-align: left;
                                font-size: 1.063rem;
                                font-weight: 300;
                                height: 40px;
                                overflow-y: hidden;
                            }
                        }
                    }
                }

                .hotels-cards__card:hover .hotels-cards__image {
                    background-size: 150%;
                    background-position: center;
                }
            }

            .hotel-cards__arrow {
                background-color: $secondary-color-one;
                border: none;
                width: 63px;
                height: 41px;
                position: absolute;
                cursor: pointer;
                box-shadow: 0 0 10px rgba(0,0,0,0.15);
                display: flex;
                justify-content: center;
                align-items: center;
                transition: 250ms ease-in-out;

                .hotel-cards__arrow--effect--container {
                    overflow: hidden;
                    width: 39px;

                    .hotel-cards__arrow--effect--right {
                        display: flex;
                        position: relative;
                        left: -140px;

                        img:nth-child(2) {
                            margin-left: 100px;
                        }
                    }

                    .hotel-cards__arrow--effect--left {
                        display: flex;
                        position: relative;
                        left: 0px;

                        img:nth-child(2) {
                            margin-left: 100px;
                        }
                    }

                    @keyframes arrow-right {
                        100% {
                            left: 0;
                        }
                    }

                    @keyframes arrow-left {
                        100% {
                            left: -140px;
                        }
                    }
                }
                
            }

            .hotel-cards__arrow--left {
                top: 50%;
                left: 5%;
                transform: translateY(-50%);
            }

            .hotel-cards__arrow--right {
                top: 50%;
                right: 5%;
                transform: translateY(-50%);
                visibility: hidden;
                cursor: auto;
            }
        }
    }
</style>