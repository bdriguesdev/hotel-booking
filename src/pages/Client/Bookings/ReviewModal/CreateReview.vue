<template>
    <form class="review-create__form" @submit.prevent="handleCreate">
        <div class="review-create__inputs__container">
            <label for="description">
                Description
                <textarea v-model="description"></textarea>
            </label>
            <label class='booking__reviews__container' for="review">
                Review Rating
                <div class="booking__reviews__rating">
                    <ReviewStarIcon @reviewValue="changeReviewValue" num="1" :color="'#FEF5D7'" />
                    <ReviewStarIcon @reviewValue="changeReviewValue" num="2" :color="'#FEF5D7'" />
                    <ReviewStarIcon @reviewValue="changeReviewValue" num="3" :color="'#FEF5D7'" />
                    <ReviewStarIcon @reviewValue="changeReviewValue" num="4" :color="'#FEF5D7'" />
                    <ReviewStarIcon @reviewValue="changeReviewValue" num="5" :color="'#FEF5D7'" />
                </div>
            </label>
        </div>
        <button class="review-create__btn" v-on:mouseenter="btnAnimation">
            Create now
            <div class="review-create__btn__container">
                <div class="review-create__btn--effect">
                    <img src="../../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                    <img src="../../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                </div>
            </div>
        </button>
    </form>
</template>

<script>
import ReviewStarIcon from './ReviewStarIcon';
/* eslint-disable no-console */
export default {
    name: 'CreateReview',
    components: {
        ReviewStarIcon
    },
    data() {
        return {
            isBtnAnimationInProgress: false,
            description: "",
            reviewValue: null
        }
    },
    methods: {
        handleCreate() {
            this.btnAnimation;
            const args = {
                description: this.description,
                value: this.reviewValue
            }
            this.$store.dispatch('createReview', args);
        },
        changeReviewValue(value) {
            this.reviewValue = value;
        },
        btnAnimation() {
            if(!this.isBtnAnimationInProgress) {
                this.isBtnAnimationInProgress = true;
                const button = document.querySelector('.review-create__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isBtnAnimationInProgress = false;
                }, 500);
            }
        }
    }
}
</script>

<style lang='scss'>
    @import '../../../../scss/variables.scss';
    @import '../../../../scss/mixins.scss';

    .review-create__form {
        padding-top: 28px;
        padding-bottom: 36px;  
        padding-left: 44px;  
        padding-right: 44px;  

        .review-create__inputs__container {
            display: flex;
            flex-wrap: wrap;

            label {
                font-family: $secondary-font;
                color: $secondary-color-two;
                font-size: 1rem;
                text-transform: uppercase;
                display: block;
                text-align: left;
                width: 261px;
                margin: 8px 0px;

                input {
                    background-color: $input-bg-color;
                    border: none;
                    width: 249px;
                    padding-left: 12px;
                    height: 42px;
                    border-bottom: 2px solid $secondary-color-two;
                    outline: none;
                    font-size: 1rem;
                    color: $input-text-color;
                    box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                    border-radius: 0;
                    display: block;
                }

                textarea {
                    width: 568px;
                    max-width: 568px;
                    min-width: 568px;
                    height: 88px;
                    outline: none;
                    font-size: 1rem;
                    color: $input-text-color;
                    padding-left: 12px;
                    padding-top: 10px;
                    background-color: $input-bg-color;
                    border: none;
                    box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                    border-bottom: 2px solid $secondary-color-two;
                    @include large-phone {
                        width: 261px;
                        max-width: 261px;
                        min-width: 261px;
                    }
                    @include small-phone {
                        width: 181px;
                        max-width: 181px;
                        min-width: 181px;
                    }
                }

                .booking__reviews__rating {
                    width: 275px;
                    @include small-phone {
                        width: 195px;
                    }

                    svg {
                        width: 29px;
                        height: 29px;
                    }

                    svg:nth-child(n + 2) {
                        margin: 0 5px;
                    }

                    svg:last-child {
                        margin: 0;
                    }
                }

            }

            label:nth-child(1) {
                width: 568px;
                margin-right: auto;
            }
        }
        
        .review-create__btn {
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
            margin-top: 28px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.20);
            cursor: pointer;
            margin: 0 auto;
            margin-top: 28px;

            .review-create__btn__container {
                overflow: hidden;
                width: 21px;
                margin-left: 10px;

                .review-create__btn--effect {
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

        .review-create__btn::after {
            content: 'Create now';
            position: absolute;
            z-index: -1;
            font-size: 1.063rem;
            top: 13px;
            left: 23px;
            color: $shadow-color;
            @include desktop {
                left: 29px;
            }
        }
    }
        
</style>