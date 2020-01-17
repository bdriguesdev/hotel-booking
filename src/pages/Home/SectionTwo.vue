<template>
    <section class="rooms-cards">
        <div class="rooms-cards__title">
            <span class="rooms-cards__number--container">
                <div class="rooms-cards__number--border"></div>
                <span class="rooms-cards__number">1</span>
            </span>
            <div class="rooms-cards__text">
                <h2>Check out some popular <span>rooms</span></h2>
                <div class="rooms-cards__line"></div>
            </div>
        </div>
        <div class="rooms-cards__overflow">
            <div v-if="roomLoading === false" class="rooms-cards__cards">
                <div @click='changeLink(room.id)' v-for="(room, index) in rooms" :key="index" class="rooms-cards__card">
                    <div class="rooms-cards__image" :style="room.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${room.photos[0].photo}')` }: {}"></div>
                    <div class="rooms-cards__information">
                        <div class="rooms-cards__information--first-line">
                            <div class="rooms-cards__main">
                                <p class="rooms-cards__location">{{ room.hotel.city }}, {{ room.hotel.state }}</p>
                                <h3 class="rooms-cards__name">{{ room.name }}</h3>
                            </div>
                            <div class="rooms-cards__reviews">
                                <img src="../../assets/Review_star.svg" alt="Review Star - Icon">
                                <h4 class="rooms-cards__reviews-avg">{{ room.reviews_average }} <span>({{ room.reviews_count }}+)</span> </h4>
                            </div>  
                        </div>
                        <div class="rooms-cards__information--second-line">
                            <p class="rooms-cards__description">
                                {{ room.description }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
            <button class="room-cards__arrow room-cards__arrow--left" v-on:click="handleCardSwipe('left')">
                <div class="room-cards__arrow--effect--container">
                    <div class="room-cards__arrow--effect--left">
                        <img src="../../assets/Rooms_cards_arrow_left.svg" alt="Arrow to swipe cards left">
                        <img src="../../assets/Rooms_cards_arrow_left.svg" alt="Arrow left effect asset">
                    </div>
                </div>
            </button>
            <button class="room-cards__arrow room-cards__arrow--right" v-on:click="handleCardSwipe('right')">
                <div class="room-cards__arrow--effect--container">
                    <div class="room-cards__arrow--effect--right">
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
    name: 'SectionTwo',
    data() {
        return {
            sectionWidth: null,
            card: 4,
            isArrowAnimatioInProgress: false,
            isSectionTitleAnimated: false
        }
    },
    beforeCreate() {
        this.$store.dispatch('changeLoading', true).roomModules;
    },
    created() {
        this.$store.dispatch('getMostPopularRooms').then(() => {
            const sectionTwo = document.querySelector('.rooms-cards').getBoundingClientRect();
            this.sectionWidth = sectionTwo.width;
        });
    },
    mounted() {
        // const sectionTwo = document.querySelector('.rooms-cards').getBoundingClientRect();
        // this.sectionWidth = sectionTwo.width;
        window.addEventListener('resize', this.resize);
        document.addEventListener('scroll', this.titleAnimation);
    },
    beforeDestroy() {
        document.removeEventListener('scroll', this.titleAnimation);
        window.removeEventListener('resize', this.resize);
    },
    methods: {
        changeLink(roomId) {
            this.$router.push({ path: `/room/${roomId}/` });
        },
        handleCardSwipe(direction) {
            if(!this.isArrowAnimatioInProgress) {
                if(direction === 'left' && this.card < 4 && this.card >= 1) {
                    const roomCardsContainer = document.querySelector('.rooms-cards__cards');
                    const roomCard = document.querySelector('.rooms-cards__card');
                    const distanceToMove = (roomCard.offsetLeft * 2) + roomCard.getBoundingClientRect().width;
                    const arrow = document.querySelector('.room-cards__arrow--effect--left');

                    //btn effect
                    this.isArrowAnimatioInProgress = true;
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
                    const roomCardsContainer = document.querySelector('.rooms-cards__cards');
                    const roomCard = document.querySelector('.rooms-cards__card');
                    const distanceToMove = (roomCard.offsetLeft * 2) + roomCard.getBoundingClientRect().width;
                    const arrow = document.querySelector('.room-cards__arrow--effect--right');

                    //btn effect
                    this.isArrowAnimatioInProgress = true;
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
            const section = document.querySelector('.rooms-cards').getBoundingClientRect();
            if(section.top <= window.innerHeight * 0.75 && !this.isSectionTitleAnimated) {
                this.isSectionTitleAnimated = true;

                const titleNumber = document.querySelector('.rooms-cards__number');
                titleNumber.style.top = '-38px';

                const titleNumberBorder = document.querySelector('.rooms-cards__number--border');
                titleNumberBorder.style.width = '100%';

                const titleTextBorder = document.querySelector('.rooms-cards__line');
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
            const sectionTwo = document.querySelector('.rooms-cards').getBoundingClientRect();
            this.sectionWidth = sectionTwo.width;
        }
    },
    computed: {
        ...mapGetters([
            'rooms',
            'roomLoading'
        ])
    },  
    watch: {
        sectionWidth(newValue) {
            const roomCardsContainer = document.querySelector('.rooms-cards__cards');
            const roomCard = document.querySelector('.rooms-cards__card');
            
            const leftValue = ((roomCardsContainer.getBoundingClientRect().width - newValue) + newValue / 2) - (roomCard.offsetLeft + roomCard.getBoundingClientRect().width / 2);
            const cardPosition = (4 - this.card) * (roomCard.offsetLeft * 2 + roomCard.getBoundingClientRect().width);
            roomCardsContainer.style.left = -leftValue + cardPosition + 'px';
        },
        card(newValue, oldValue) {
            if(newValue === 1) {
                const rightArrow = document.querySelector('.room-cards__arrow--right');
                rightArrow.style.opacity = 0;
                rightArrow.style.cursor = 'auto';
                setTimeout(() => {
                    rightArrow.style.visibility = 'hidden';
                }, 250);
            } else if(newValue === 4) {
                const leftArrow = document.querySelector('.room-cards__arrow--left');
                leftArrow.style.opacity = 0;
                leftArrow.style.cursor = 'auto';
                setTimeout(() => {
                    leftArrow.style.visibility = 'hidden';
                }, 250);
            }

            if(oldValue === 1) {
                const rightArrow = document.querySelector('.room-cards__arrow--right');
                rightArrow.style.visibility = 'visible';
                rightArrow.style.cursor = 'pointer';
                rightArrow.style.opacity = 1;
            } else if(oldValue === 4) {
                const leftArrow = document.querySelector('.room-cards__arrow--left');
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
    @import '../../scss/mixins.scss';

    .rooms-cards {
        max-width: 1900px;
        width: 100%;
        margin: 0 auto;
        margin-top: 50px;
        position: relative;

        .rooms-cards__title {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 45px;
            margin-left: 5%;
            @include large-phone {
                flex-direction: column;
            }

            .rooms-cards__number--container {
                width: 87px;
                height: 87px;
                background-color: $secondary-color-two;
                overflow: hidden;
                position: relative;

                .rooms-cards__number--border {
                    background-color: $secondary-color-one;
                    height: 3px;
                    width: 0;
                    transition: 800ms ease-in-out;
                    transition-delay: 600ms;
                }

                .rooms-cards__number {
                    font-size: 9.375rem;
                    color: $primary-color;
                    font-weight: 700;
                    position: absolute;
                    left: -13px;
                    top: -150px;
                    transition: 800ms ease-in-out;
                }
            }

            .rooms-cards__text {
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
                    @include large-phone {
                        font-size: 1.7rem;
                    }

                    span {
                        color: $secondary-color-two;
                        font-size: 1.875rem;
                        font-weight: 300;
                        font-family: $secondary-font;
                        @include large-phone {
                            font-size: 1.7rem;
                        }
                    }
                }

                .rooms-cards__line {
                    min-width: 80%;
                    visibility: hidden;
                    width: 367px;
                    max-width: 95%;
                    height: 3px;
                    background-color: $secondary-color-two;
                }
            }
        }

        .rooms-cards__overflow {
            position: relative;
            overflow: hidden;
            padding: 20px 0;

            .rooms-cards__cards {
                position: relative;
                display: flex;
                margin: 0 auto;
                width: 2360px;
                @include medium-phone {
                    width: 1640px;
                }
                @include small-phone {
                    width: 1200px;
                }

                .rooms-cards__card {
                    width: 450px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.2);
                    margin: 0 70px;
                    background-color: $primary-color;
                    cursor: pointer;
                    @include medium-phone {
                        width: 350px;
                        margin: 0 30px;
                    }
                    @include small-phone {
                        width: 260px;
                        margin: 0 20px;
                    }

                    .rooms-cards__image {
                        background-image: url('../../assets/Room_card_one.jpg');
                        background-size: 100%;
                        background-position: center; 
                        background-color: lightgray;
                        width: 100%;
                        height: 255px;
                        transition: 300ms ease-in-out;
                        @include medium-phone {
                            height: 230px;
                        }
                        @include small-phone {
                            height: 170px;
                        }
                    }

                    .rooms-cards__information {

                        .rooms-cards__information--first-line {
                            display: flex;
                            justify-content: space-between;
                            align-items: flex-start;
                            margin: 20px 20px;
                            margin-bottom: 0px;

                            .rooms-cards__main {
                                
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

                            .rooms-cards__reviews {
                                display: flex;
                                justify-content: flex-end;
                                align-items: center;

                                .rooms-cards__reviews-avg {
                                    margin: 0;
                                    color: $secondary-color-two;
                                    margin-top: 3px;
                                    margin-left: 3px;
                                    color: $secondary-color-two;
                                    font-size: 1.063rem;
                                    font-weight: 400;

                                    span {
                                        color: $secondary-color-two;
                                        font-size: 1.063rem;
                                        font-weight: 300;
                                    }
                                }
                            }
                        }

                        .rooms-cards__information--second-line {
                            margin: 0 20px;
                            margin-top: 10px;
                            padding-bottom: 20px;

                            .rooms-cards__description {
                                margin: 0;
                                color: $light-gray-text-color;
                                text-align: left;
                                font-size: 1.063rem;
                                font-weight: 300;
                                height: 40px;
                                overflow-y: hidden;
                                @include desktop {
                                    height: 37px;
                                }
                            }
                        }
                    }
                }
                
                .rooms-cards__card:hover .rooms-cards__image {
                    background-size: 150%;
                    background-position: center;
                }
            }

            .room-cards__arrow {
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

                .room-cards__arrow--effect--container {
                    overflow: hidden;
                    width: 39px;

                    .room-cards__arrow--effect--right {
                        display: flex;
                        position: relative;
                        left: -140px;

                        img:nth-child(2) {
                            margin-left: 100px;
                        }
                    }

                    .room-cards__arrow--effect--left {
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

            .room-cards__arrow--left {
                top: 50%;
                left: 5%;
                transform: translateY(-50%);
                visibility: hidden;
                cursor: auto;
            }

            .room-cards__arrow--right {
                top: 50%;
                right: 5%;
                transform: translateY(-50%);
            }
        }
    }
</style>