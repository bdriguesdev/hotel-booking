<template>
    <div class="room__review">
        <div class="room__review__first-part">
            <div class="room__review__avatar" :style="review.client.photo? { backgroundImage: `url('http://127.0.0.1:8000${review.client.photo}')` }: {}"></div>
            <div class="room__review__info">
                <h3 class="room__review__user">{{ review.client.first_name }} {{ review.client.last_name }}</h3>
                <span class="room__review__date">{{ endDate() }}</span>
                <div class="room__review_stars">
                    <ReviewStarIcon v-for="(num, index) in new Array(review.value)" :key="index + 10" :color="'#FFDD65'" />
                    <ReviewStarIcon v-for="(num, index) in new Array(5 - review.value)" :key="index" :color="'#FEF5D7'" />
                </div>
            </div>
        </div>
        <div class="room__review__second-part">
            <img src='../assets/Room_review_comment_effect.svg' alt="Review comment effect">
            <p class="room__review__comment">
                {{ review.description }}
            </p>
        </div>
    </div>
</template>

<script>
import ReviewStarIcon from './ReviewStarIcon';

export default {
    name: 'Review',
    components: {
        ReviewStarIcon
    },
    props: [
        'review'
    ],
    methods: {
        endDate() {
            const date = this.review.booking.end.split('T')[0].split("-");
            return `${date[2]}/${date[1]}/${date[0]}`;
        }
    }
}
</script>

<style lang='scss'>
    @import '../scss/variables.scss';
    @import '../scss/mixins.scss';

    .room__review {
        padding: 0;
        margin: 0 10px;

        .room__review__first-part {
            display: flex;
            justify-content: flex-start;

            .room__review__avatar {
                background-image: url('../assets/Room_review_avatar.jpg');
                background-size: cover;
                background-position: center;
                width: 80px;
                height: 80px;
            }

            .room__review__info {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                margin-left: 10px;

                h3 {
                    margin: 0;
                    font-family: $secondary-font;
                    color: $secondary-color-two;
                    font-weight: 300;
                    font-size: 1.25rem;
                    text-align: left;
                }

                span {
                    margin: 0;
                    font-weight: 400;
                    font-size: 0.875rem;
                    color: $gray-text-color;
                    text-align: left;
                }

                .room__review_stars {
                    margin-top: auto;
                    svg {
                        @include small-phone {
                            width: 18px;
                            height: 15px;
                        }
                    }
                }
            }
        }
        .room__review__second-part {
            margin: 0 10px;
            margin-top: 20px;
            display: flex;
            align-items: flex-start;
            justify-content: flex-end;
            
            .room__review__comment {
                margin: 0;
                text-align: left;
                line-height: 145%;
                color: $gray-text-color;
                font-size: 1.063rem;
                font-weight: 300;
                background-color: $input-bg-color;
                padding: 20px;
                width: 90%;
            }
            img {
                @include small-phone {
                    width: 5%;
                }
            }
        }
    }

    
</style>