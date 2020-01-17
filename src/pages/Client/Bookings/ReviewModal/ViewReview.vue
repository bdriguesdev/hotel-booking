<template>
    <div class="room__review__bookings">
        <div class="room__review__first-part">
            <div class="room__review__avatar"></div>
            <div class="room__review__info">
                <h3 class="room__review__user">{{ user.first_name }} {{ user.last_name }}</h3>
                <span class="room__review__date">{{ endDate() }}</span>
                <div class="room__review_stars">
                    <ReviewStarIcon v-for="(num, index) in new Array(booking.review.value)" :key="index + 10" :color="'#FFDD65'" />
                    <ReviewStarIcon v-for="(num, index) in new Array(5 - booking.review.value)" :key="index" :color="'#FEF5D7'" />
                </div>
            </div>
        </div>
        <div class="room__review__second-part">
            <img src='../../../../assets/Room_review_comment_effect.svg' alt="Review comment effect">
            <p class="room__review__comment">
                {{ booking.review.description }}
            </p>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import ReviewStarIcon from './ReviewStarIcon';

export default {
    name: 'ViewReview',
    components: {
        ReviewStarIcon
    },
    methods: {
        endDate() {
            const date = this.booking.end.split('T')[0].split("-");
            return `${date[2]}/${date[1]}/${date[0]}`;
        }
    },
    computed: {
        ...mapGetters([
            'booking',
            'user'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../../../../scss/variables.scss';

    .room__review__bookings {
        padding-top: 28px;
        padding-bottom: 36px;  
        padding-left: 44px;  
        padding-right: 44px;  

        .room__review__first-part {
            display: flex;
            justify-content: flex-start;

            .room__review__avatar {
                background-image: url('../../../../assets/Room_review_avatar.jpg');
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
                }

                span {
                    margin: 0;
                    font-weight: 400;
                    font-size: 0.875rem;
                    color: $gray-text-color;
                }

                .room__review_stars {
                    margin-top: auto;
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
        }
    }   
</style>