<template>
    <section class="join__container">
        <div class="join__main-title">
            <span class="join__number--container">
                <div class="join__number--border"></div>
                <span class="join__number">3</span>
            </span>
            <div class="join__main-title__text">
                <h2>Are you ready to join this <span>community</span>?</h2>
                <div class="join__main-title__line"></div>
            </div>
        </div>
        <div class="join__content">
            <div class="join__image">
                <img src="../../assets/Community_icon.svg" alt="Community icon">
            </div>
            <div class="join__text">
                <h3 class="join__secondary-title">Join an amazing community</h3>
                <p class="join__paragraph">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ac pretium orci. Etiam tincidunt tellus 
                    vel felis ultricies, sed lobortis quam tristique. Pellentesque imperdiet, quam at imperdiet commodo, 
                    magna odio luctus leo, sed finibus odio nunc vitae enim. Phasellus placerat cursus felis, eget venenatis
                     arcu semper sed. Morbi porttitor pulvinar velit vel laoreet.
                </p>
                <button class="join__btn btn btn--red" v-on:click="handleRegister" v-on:mouseenter="registerBtnAnimation">
                    <span>Register now</span>
                    <div class="join__btn--container">
                        <div class="join__btn--effect">
                            <img src="../../assets/Button_arrow_one.svg" alt="Button arrow - animation asset" />
                            <img src="../../assets/Button_arrow_one.svg" alt="Button arrow" />
                        </div>
                    </div>
                </button>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'SectionFour',
    data() {
        return {
            isRegisterBtnAnimationInProgress: false,
            isSectionTitleAnimated: false,
            isSectionTextAnimated: false
        }
    },
    mounted() {
        /* eslint-disable no-console */
        document.addEventListener('scroll', this.titleAnimation);
        document.addEventListener('scroll', this.textAnimation);
    },
    beforeDestroy() {
        document.removeEventListener('scroll', this.titleAnimation);
        document.removeEventListener('scroll', this.textAnimation);
    },
    methods: {
        handleRegister() {
            this.$emit('modal', 'register');
            window.scrollTo(0, 0);
            this.registerBtnAnimation();
        },
        registerBtnAnimation() {
            if(!this.isRegisterBtnAnimationInProgress) {
                this.isRegisterBtnAnimationInProgress = true;
                const registerButton = document.querySelector('.join__btn--effect');
                registerButton.style.animation = 'btn-hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    registerButton.style.animation = '';
                    this.isRegisterBtnAnimationInProgress = false;
                }, 500);
            }
        },
        titleAnimation() {
            const section = document.querySelector('.join__container').getBoundingClientRect();
            // const sectionText = document.querySelector('.join__text').getBoundingClientRect();
            if(section.top <= window.innerHeight * 0.75 && !this.isSectionTitleAnimated) {
               this.isSectionTitleAnimated = true;

                const titleNumber = document.querySelector('.join__number');
                titleNumber.style.top = '-38px';

                const titleNumberBorder = document.querySelector('.join__number--border');
                titleNumberBorder.style.width = '100%';

                const titleTextBorder = document.querySelector('.join__main-title__line');
                const titleNumberBorderWidth = titleTextBorder.getBoundingClientRect().width;
                // const titleNumberBorderMinWidth = titleTextBorder.style.minWidth;
                titleTextBorder.style.width = '0px';
                titleTextBorder.style.minWidth = '0%';
                titleTextBorder.getBoundingClientRect();
                titleTextBorder.style.visibility = 'visible';
                titleTextBorder.style.transition = '800ms ease-in-out';
                titleTextBorder.style.width = titleNumberBorderWidth + 'px';
                // titleTextBorder.style.minWidth = titleNumberBorderMinWidth + 'px';
            }
        },
        textAnimation() {
            const section = document.querySelector('.join__container').getBoundingClientRect();
            if(section.top <= window.innerHeight * 0.75 && !this.isSectionTextAnimated) {
                const sectionText = document.querySelector('.join__text');
                sectionText.style.animation = 'text-appears-animation 1000ms ease-in-out 1';
                sectionText.style.animationFillMode = 'forwards';
            }
        }
    }
}
</script>

<style lang='scss'>
    @import '../../scss/variables.scss';
    @import '../../scss/mixins.scss';

    .join__container {
        max-width: 1800px;
        width: 90%;
        margin: 0 auto;
        margin-top: 100px;
        position: relative;

        .join__main-title {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 65px;
            margin-right: 5%;
            @include large-phone {
                flex-direction: column;
            }

            .join__number--container {
                width: 87px;
                height: 87px;
                background-color: $secondary-color-two;
                overflow: hidden;
                position: relative;

                .join__number--border {
                    background-color: $secondary-color-one;
                    height: 3px;
                    width: 0;
                    transition: 800ms ease-in-out;
                    transition-delay: 600ms;
                }

                .join__number {
                    font-size: 9.375rem;
                    color: $primary-color;
                    font-weight: 700;
                    position: absolute;
                    left: -13px;
                    top: -150px;
                    transition: 800ms ease-in-out;
                }
            }

            .join__main-title__text {
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

                .join__main-title__line {
                    visibility: hidden;
                    min-width: 80%;
                    width: 367px;
                    max-width: 95%;
                    height: 3px;
                    background-color: $secondary-color-two;
                }
            }
        }

        .join__content {
            display: flex;
            justify-content: center;
            position: relative;

            .join__image {
                background-color: lightgray;
                background-image: url('../../assets/Join_Community_image.jpg');
                width: 821px;
                min-height: 451px;
                background-size: cover;
                background-position: center;
                @include medium-phone {
                    width: 90%;
                    height: 300px;
                }

                img {
                    background-color: $primary-color;
                    padding: 15px;
                    float: left;
                    box-shadow: 0 0 15px rgba(0,0,0,0.1);
                }
            }

            .join__text {
                margin-top: 105px;
                margin-left: -70px;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                flex-grow: 0;
                opacity: 0;
                @include tablet {
                    margin-left: -300px;
                }
                @include medium-phone {
                    position: absolute;
                    right: 0;
                    top: 350px;
                    margin: 0;
                }

                .join__secondary-title {
                    color: $primary-color;
                    font-size: 2.188rem;
                    font-family: $secondary-font;
                    font-weight: 300;
                    margin: 0;
                    background-color: $secondary-color-two;
                    padding: 15px 15px;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                    display: inline-block;
                    margin-bottom: 35px;
                    @include tablet {
                        font-size: 1.7rem;
                    }
                }

                .join__paragraph {
                    color: $light-gray-text-color;
                    font-size: 1.063rem;
                    font-weight: 300;
                    line-height: 150%;
                    margin: 0 auto;
                    background-color: $primary-color;
                    max-width: 505px;
                    padding: 20px;
                    margin-bottom: 35px;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                }

                .join__btn {
                    background-color: $secondary-color-one;
                    border: 2px solid $secondary-color-one;
                    display: inline-block;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 195px;
                    height: 50px;
                    box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
                    margin: 0 auto;
                    cursor: pointer;
                    opacity: 0;
                    animation: btn-appears-animation 1000ms ease-in-out 1;
                    animation-fill-mode: forwards;
                    animation-delay: 150ms;
                    @include tablet {
                        width: 155px;
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
                        content: 'Register now';
                        position: absolute;
                        color: $shadow-color;
                        width: 100%;
                        top: 1px;
                        left: -2px;
                        z-index: -1;
                    }

                    .join__btn--container {
                        margin-left: 5px;
                        overflow: hidden;
                        width: 21px;

                        .join__btn--effect {
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

            @keyframes text-appears-animation {
                100% {
                    opacity: 1;
                }
            }
        }
    }

</style>