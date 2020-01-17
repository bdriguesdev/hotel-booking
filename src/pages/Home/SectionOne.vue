<template>
    <section class='introductory'>
        <div class="introductory__text">
            <!-- <div class="introductory__text--container"> -->
                <h2 class="introductory__text--white">Looking for a nice hotel to book?</h2>
            <!-- </div> -->
            <h2 class="introductory__text--white">Or for a place to advertise your hotel?</h2>
            <h2 class="introductory__text--black">You have found the right place!</h2>
            <button class="btn introductory__btn btn--red" v-on:click="handleRegister" v-on:mouseenter="registerBtnAnimation">
                <span>Register now</span>
                <div class="introductory__btn--container">
                    <div class="introductory__btn--effect">
                        <img src="../../assets/Button_arrow_one.svg" alt="Button arrow - animation asset" />
                        <img src="../../assets/Button_arrow_one.svg" alt="Button arrow" />
                    </div>
                </div>
            </button>
        </div>
        <div class="introductory__slide">
            <div class="slide__images">
                <div class="slide__image--one"></div>
                <div class="slide__image--two"></div>
                <div class="slide__image--three"></div>
            </div>
            <div class="slide__information">
                <div class="slide__progression">
                    <div class="slide__progression--bar"></div>
                </div>
                <div class="slide__text">
                    <div class="slide__text--one">
                        <h3 class="slide__number">1<span class="slide__number--red">.</span></h3>
                        <h4 class="slide__name">Name of the hotel</h4>
                        <p class="slide__location">location</p>
                    </div>
                    <div class="slide__text--two">
                        <h3 class="slide__number">2<span class="slide__number--red">.</span></h3>
                        <h4 class="slide__name">Name of the hotel</h4>
                        <p class="slide__location">location</p>
                    </div>
                    <div class="slide__text--three">
                        <h3 class="slide__number">3<span class="slide__number--red">.</span></h3>
                        <h4 class="slide__name">Name of the hotel</h4>
                        <p class="slide__location">location</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="slide__information--box-shadow" hidden='true'></div>
        <button class="slide__arrow" v-on:click='handleClick'>
            <div class="slide__arrow--container">
                <div class="slide__arrow--effect">
                    <img src="../../assets/Slide_arrow_one.svg" alt="Slide arrow" />
                    <img src="../../assets/Slide_arrow_one.svg" alt="Slide arrow" />
                </div>
            </div>
        </button>
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
    </section>
</template>

<script>
export default {
    name: 'SectionOne',
    data() {
        return {
            slide: 1,
            isAnimationInProgress: false,
            slideInterval: null,
            isRegisterBtnAnimationInProgress: false
        }
    },
    mounted() {
        const slideInformation = document.querySelector('.slide__information');
        const slideInformationShadow = document.querySelector('.slide__information--box-shadow');
        const slide = document.querySelector('.introductory__slide');
        slideInformationShadow.style.top = slideInformation.offsetTop + slide.offsetTop + 'px';
        slideInformationShadow.hidden = false;
        /* eslint-disable no-console */
        this.setNewSlideInterval();
    },
    methods: {
        handleRegister() {
            this.$emit('modal', 'register');
            window.scrollTo(0,0);
            this.registerBtnAnimation();
        },
        registerBtnAnimation() {
            if(!this.isRegisterBtnAnimationInProgress) {
                this.isRegisterBtnAnimationInProgress = true;
                const registerButton = document.querySelector('.introductory__btn--effect');
                registerButton.style.animation = 'btn-hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    registerButton.style.animation = '';
                    this.isRegisterBtnAnimationInProgress = false;
                }, 500);
            }
        },
        setNewSlideInterval() {
            const slideProgressionBar = document.querySelector('.slide__progression--bar');
            slideProgressionBar.style.transition = '0ms linear';
            slideProgressionBar.style.width = '0px';
            if(this.slideInterval) {
                clearInterval(this.slideInterval);
            }
            slideProgressionBar.getBoundingClientRect();
            slideProgressionBar.style.transition = '5000ms linear';
            slideProgressionBar.style.width = '100%';
            this.slideInterval = setInterval(() => {
                slideProgressionBar.style.transition = '0ms linear';
                slideProgressionBar.style.width = '0px';
                slideProgressionBar.getBoundingClientRect();
                slideProgressionBar.style.transition = '5000ms linear';
                slideProgressionBar.style.width = '100%';
                this.slide = this.slide + 1 > 3? 1: this.slide + 1;
            }, 5000);
        },
        handleClick() {
            if(!this.isAnimationInProgress) {
                this.isAnimationInProgress = true;
                const slideArrow = document.querySelector('.slide__arrow--effect');
                const newSlide = this.slide + 1;
                if(newSlide > 3) {
                    this.slide = 1;
                } else {
                    this.slide = newSlide
                }
                slideArrow.style.animation = 'slideArrow 1s ease-in-out 0s 1';
                setTimeout(() => {
                    slideArrow.style.animation = '';
                    this.isAnimationInProgress = false;
                }, 1000)
                this.setNewSlideInterval();
                /* eslint-disable no-console */
                // console.log('working'); 
                }
        },
        modifySlideTrack(active, deactive) {
            active.style.fill = '#FF1E1E';
            active.style.stroke = '#FF1E1E';
            deactive.style.fill = 'none';
            deactive.style.stroke = 'black';
        },
        changeSlideTrack(value) {
            this.slide = value;
            this.setNewSlideInterval();
        }
    },
    watch: {
        slide(newValue, oldValue) {
            const slideContainer = document.querySelector('.slide__images');
            const slidesTracks = document.querySelectorAll('.slide__track svg circle');
            const slideInformation = document.querySelector('.slide__text');
            // console.log(slidesTracks);
            if(newValue == 1) {
                slideContainer.style.right = '0';
                slideInformation.style.right = '0';
                this.modifySlideTrack(slidesTracks[0], slidesTracks[oldValue - 1]);
            } else if(newValue == 2) {
                slideContainer.style.right = '100%';
                slideInformation.style.right = '100%';
                this.modifySlideTrack(slidesTracks[1], slidesTracks[oldValue - 1]);
            } else {
                slideContainer.style.right = '200%';
                slideInformation.style.right = '200%';
                this.modifySlideTrack(slidesTracks[2], slidesTracks[oldValue - 1]);
            }
        }
    }
}
</script>

<style lang='scss'> 
    @import '../../scss/variables.scss';

    .introductory {
        max-width: 1800px;
        width: 90%;
        margin: 0 auto;
        position: relative;
        height: 93vh;

        .introductory__text {
            max-width: 640px;
            background-color: transparent;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding-top: 25vh;
            position: relative;
            z-index: 1;

            .introductory__text--white {
                background-color: $primary-color;
                margin: 0;
                text-align: left;
                display: inline-block;
                padding: 20px 20px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                font-size: 2.188rem;
                font-family: $secondary-font;
                font-weight: 300;
                margin-bottom: 23px;
                opacity: 0;
                animation: white-text 1000ms ease-in-out 1;
                animation-delay: 300ms;
                animation-fill-mode: forwards;
                color: $secondary-color-two;
            }

            @keyframes white-text {
                100% {
                    opacity: 1;
                }
            }

            .introductory__text--black {
                background-color: $secondary-color-two;
                color: $primary-color;
                margin: 0;
                text-align: left;
                display: inline-block;
                padding: 20px 20px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                font-size: 2.188rem;
                font-weight: 700;
                opacity: 0;
                animation: black-text 1000ms ease-in-out 1;
                animation-fill-mode: forwards;
                animation-delay: 350ms;
            }

            @keyframes black-text {
                100% {
                    opacity: 1;
                }
            }

            .introductory__btn {
                background-color: $secondary-color-one;
                border: 2px solid $secondary-color-one;
                display: inline-block;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 195px;
                height: 50px;
                box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
                margin-top: 45px;
                cursor: pointer;
                opacity: 0;
                animation: btn-appears-animation 1000ms ease-in-out 1;
                animation-fill-mode: forwards;
                animation-delay: 150ms;

                span {
                    margin-right: 5px;
                    font-size: 1.25rem;
                    color: $primary-color;
                    position: relative;
                    z-index: 2;
                }

                span:after {
                    content: 'Register now';
                    position: absolute;
                    color: $shadow-color;
                    width: 100%;
                    top: 1px;
                    left: -2px;
                    z-index: -1;
                }

                .introductory__btn--container {
                    margin-left: 5px;
                    overflow: hidden;
                    width: 21px;

                    .introductory__btn--effect {
                        position: relative;
                        left: -202%;
                        width: 300%;
                        display: flex;
                        justify-content: space-between;
                        height: 100%;
                    }

                }

            }

            @keyframes btn-hover-animation {
                100% {
                    left: 0;
                }
            }

            @keyframes btn-appears-animation {
                100% {
                    opacity: 1;
                }
            }
    
        }

        .introductory__slide {
            width: 60vw;
            background-color: lightgray;
            position: absolute;
            z-index: 0;
            right: 5%;
            top: 10vh;
            overflow: hidden;

            .slide__images {
                display: flex;
                position: relative;
                right: 0;
                width: 300%;
                transition: 1000ms ease-in-out;

                .slide__image--one {
                    background-image: url('../../assets/Introductory_slide_one.jpg');
                    background-size: cover;
                    width: 100%;
                    height: 70vh;
                }

                .slide__image--two {
                    background-image: url('../../assets/Introductory_slide_two.jpg');
                    background-size: cover;
                    width: 100%;
                    height: 70vh;
                }

                .slide__image--three {
                    background-image: url('../../assets/Introductory_slide_three.jpg');
                    background-size: cover;
                    width: 100%;
                    height: 70vh;
                }
            }

            .slide__information {
                position: absolute;
                background-color: $primary-color;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.15);
                right: 0;
                bottom: 0;
                width: 225px;
                height: 140px;
                overflow: hidden;

                .slide__progression {
                    height: 3px;
                    width: 100%;
                    background-color: #D8D8D8;

                    .slide__progression--bar {
                        height: 3px;
                        width: 0;
                        background-color: $secondary-color-one;
                        transition: 5000ms linear;
                    }

                }

                .slide__text {
                    display: flex;
                    position: relative;
                    right: 0;
                    width: 300%;
                    height: 100%;
                    transition: 800ms ease-in-out;

                    .slide__text--one,
                    .slide__text--two,
                    .slide__text--three {
                        width: 100%;
                    }

                    .slide__number {
                        margin: 0;
                        text-align: left;
                        font-size: 4.375rem;
                        font-weight: 500;
                        margin-left: 17px;
                        color: $secondary-color-two;

                        .slide__number--red {
                            color: $secondary-color-one;
                            font-size: 4.375rem;
                            font-weight: 500;
                        }
                    }
                    
                    .slide__name {
                        margin: 0;
                        text-align: left;
                        font-size: 1.063rem;
                        font-weight: 400;
                        margin-left: 20px;
                        line-height: 8px;
                        margin-bottom: 10px;
                    }

                    .slide__location {
                        margin: 0;
                        text-align: left;
                        font-size: 1rem;
                        font-weight: 300;
                        margin-left: 20px;
                    }
                }       
            }
        }

        .slide__information--box-shadow {
            position: absolute;
            width: 225px;
            height: 140px;
            z-index: -1;
            right: 5%;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.15);
        }

        .slide__arrow {
            position: absolute;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            justify-content: center;
            align-items: center;
            width: 81px;
            height: 53px;
            background-color: $secondary-color-one;
            border: 2px solid $secondary-color-one;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            z-index: 2;
            cursor: pointer;

            .slide__arrow--container {
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: hidden;
                
                .slide__arrow--effect {
                    position: relative;
                    left: -125px;
                    display: flex;

                    img:nth-child(1) {
                        margin-right: 200px;
                    }
                }

                .slide__arrow--animation {
                    animation: slideArrow 1s ease-in-out 0s 1;
                }

                @keyframes slideArrow {
                    0% {
                        left: -125px;
                    }
                    100% {
                        left: 125px;
                    }
                }
            }

            
        }

        .slide__track {
            position: absolute;
            z-index: 2;
            bottom: 5vh;
            left: 50%;
            transform: translateX(-50%);

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
    }

</style>