<template>
    <div class="search__slide" >
        <div class="search__slide__imgs">
            <div alt="Slide image one" class="search__img" :style="room.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${room.photos[0].photo}')` }: {}"></div>
            <div alt="Slide image two" class="search__img" :style="room.photos[1]? { backgroundImage: `url('http://127.0.0.1:8000${room.photos[1].photo}')` }: {}"></div>
            <div alt="Slide image three" class="search__img" :style="room.photos[2]? { backgroundImage: `url('http://127.0.0.1:8000${room.photos[2].photo}')` }: {}"></div>
        </div>
        <div class="search__slide__text" @click="changeLink">
            <div class="search__text--part-one">
                <div class="search__text--info">
                    <p>{{ room.hotel.city }}, {{ room.hotel.state }}</p>
                    <h3>{{ room.name }}</h3>
                </div>
                <div class="search__text--reviews">
                    <img src="../../assets/Review_star.svg" alt="Review icon">
                    <p>{{ room.reviews_count }} <span>({{ room.reviews_average }}+)</span></p>
                </div>
            </div>
            <div class="search__text--part-two">    
                <p>{{ room.description }}</p>
                <span>${{ room.price }}</span>
            </div>  
        </div>
        <button class="search__arrow search__arrow--left" v-on:click="handleCardSwipe('left')">
            <div class="search__arrow--effect--container">
                <div class="search__arrow--effect--left">
                    <img src="../../assets/Rooms_cards_arrow_left.svg" alt="Arrow to swipe cards left">
                    <img src="../../assets/Rooms_cards_arrow_left.svg" alt="Arrow left effect asset">
                </div>
            </div>
        </button>
        <button class="search__arrow search__arrow--right" v-on:click="handleCardSwipe('right')">
            <div class="search__arrow--effect--container">
                <div class="search__arrow--effect--right">
                    <img src="../../assets/Rooms_cards_arrow_right.svg" alt="Arrow to swipe cards right">
                    <img src="../../assets/Rooms_cards_arrow_right.svg" alt="Arrow right effect asset">
                </div>
            </div>
        </button>
    </div>
</template>

<script>
export default {
    /* eslint-disable no-console */
    name: 'RoomSlide',
    data() {
        return {
            card: 2,
            sectionWidth: null,
            arrowAnimationInProgress: false,
            cardNumber: null
        }
    },
    props: [
        'room'
    ],
    mounted() {
        this.cardNumber = this.$vnode.key;
        this.linkCard(2, 1);
    },
    methods: {
        linkCard(newValue, oldValue) {
            const cardImgs = document.querySelectorAll('.search__img');
            const oldImg = cardImgs[(this.cardNumber * 3 + oldValue) - 1];
            const newImg = cardImgs[(this.cardNumber * 3 + newValue) - 1];

            oldImg.style.cursor = 'auto';
            newImg.style.cursor = 'pointer';
            oldImg.removeEventListener('click', this.changeLink);
            newImg.addEventListener('click', this.changeLink);
        },
        changeLink() {
            this.$router.push({ path: `/room/${this.room.id}/` });
        },
        handleCardSwipe(direction) {
            if(!this.arrowAnimationInProgress) {
                const slideContainer = document.querySelectorAll('.search__slide__imgs')[this.cardNumber];
                const slideImg = document.querySelector('.search__img');
                slideContainer.style.transition = '500ms ease-in-out';

                if(direction === 'right' && this.card > 1) {
                    const arrow = document.querySelectorAll('.search__arrow--effect--right')[this.cardNumber];

                    this.card--; 
                    slideContainer.style.left = parseFloat(slideContainer.style.left.split('px')[0]) + (slideImg.offsetLeft * 2 + slideImg.getBoundingClientRect().width) + 'px';
                    //btn effect
                    this.isArrowAnimationInProgress = true;
                    arrow.style.animation = 'arrow-right 500ms ease-in-out 1';
                    //reseting all effects
                    setTimeout(() => {
                        arrow.style.animation = '';
                        this.isArrowAnimationInProgress = false;
                        slideContainer.style.transition = '';
                    }, 500);
                } else if(direction === 'left' && this.card < 3) {
                    const arrow = document.querySelectorAll('.search__arrow--effect--left')[this.cardNumber];

                    this.card++;
                    slideContainer.style.left = slideContainer.style.left.split('px')[0] - (slideImg.offsetLeft * 2 + slideImg.getBoundingClientRect().width) + 'px';
                    //btn effect
                    this.isArrowAnimationInProgress = true;
                    arrow.style.animation = 'arrow-left 500ms ease-in-out 1';
                    //reseting all effects
                    setTimeout(() => {
                        arrow.style.animation = '';
                        this.isArrowAnimationInProgress = false;
                        slideContainer.style.transition = '';
                    }, 500);
                }
            }
        }
    },
    watch: {
        card(newValue, oldValue) {
            const rightArrow = document.querySelectorAll('.search__arrow--right')[this.cardNumber];
            const leftArrow = document.querySelectorAll('.search__arrow--left')[this.cardNumber];
            
            this.linkCard(newValue, oldValue)
            if(newValue === 1) {
                rightArrow.style.opacity = 0;
                rightArrow.style.cursor = 'auto';
                setTimeout(() => {
                    rightArrow.style.visibility = 'hidden';
                }, 250);
            } else if(newValue === 3) {
                leftArrow.style.opacity = 0;
                leftArrow.style.cursor = 'auto';
                setTimeout(() => {
                    leftArrow.style.visibility = 'hidden';
                }, 250);
            }

            if(oldValue === 1) {
                rightArrow.style.visibility = 'visible';
                rightArrow.style.cursor = 'pointer';
                rightArrow.style.opacity = 1;
            } else if(oldValue === 3) {
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

    .search__slide {
        position: relative;
        margin-bottom: 80px;

        .search__slide__imgs {
            display: flex;
            justify-content: center;
            position: relative;
            left: -180px;
            width: 2280px;

            .search__img {
                background-image: url('../../assets/Room_card_one.jpg');
                background-size: 100%;
                background-position: center;
                width: 600px;
                height: 338px;
                margin: 0 80px;
            }
        }

        .search__slide__text {
            margin: 0 auto;
            width: 600px;
            background-color: $primary-color;
            box-shadow: 0 0 10px rgba(0,0,0,0.15);
            transition: none;
            cursor: pointer;

            .search__text--part-one {
                display: flex;
                justify-content: space-between;
                margin: 0 23px;
                padding-top: 23px;
                margin-bottom: 13px;

                .search__text--info {
                    display: flex;
                    flex-direction: column;
                    align-items: flex-start;

                        p {
                        margin: 0;
                        text-transform: uppercase;
                        font-size: 0.875rem;
                        color: $secondary-color-one;
                        font-weight: 300;
                    }

                    h3 {
                        margin: 0;
                        color: $secondary-color-two;
                        font-weight: 400;
                        font-size: 1.25rem;
                    }
                }

                .search__text--reviews {
                    display: flex;
                    align-items: flex-start;

                    p {
                        margin: 0;
                        margin-top: 3px;
                        margin-left: 3px;
                        font-size: 1.063rem;
                        color: $secondary-color-two;
                        font-weight: 400;

                        span {
                            font-weight: 300;
                        }
                    }
                }
                
            }

            .search__text--part-two {
                margin: 0 23px;
                display: flex;
                padding-bottom: 23px;
                justify-content: space-between;
                align-items: flex-end;
            
                p {
                    margin: 0;
                    text-align: left;
                    width: 80%;
                    line-height: 150%;
                    color: $light-gray-text-color;
                    font-size: 1.063rem;
                    font-weight: 300;
                    overflow-y: hidden;
                    height: 50px;
                }

                span {
                    font-weight: 400;
                    color: $secondary-color-two;
                    font-size: 1.25rem;
                }
            }
        }

        .search__arrow {
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

            .search__arrow--effect--container {
                overflow: hidden;
                width: 39px;

                .search__arrow--effect--right {
                    display: flex;
                    position: relative;
                    left: -140px;

                    img:nth-child(2) {
                        margin-left: 100px;
                    }
                }

                .search__arrow--effect--left {
                    display: flex;
                    position: relative;
                    left: 0px;

                    img:nth-child(2) {
                        margin-left: 100px;
                    }
                }

                @keyframes arrow-right {
                    100% {
                        left: 0px;
                    }
                }

                @keyframes arrow-left {
                    100% {
                        left: -140px;
                    }
                }
            }
        }

        .search__arrow--left {
            top: 50%;
            left: 5%;
            transform: translateY(-50%);
            cursor: auto;
        }

        .search__arrow--right {
            top: 50%;
            right: 5%;
            transform: translateY(-50%);
        }
    }

</style>