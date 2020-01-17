<template>
    <div class="booking__card">
        <div class="booking__card__img"></div>
        <div class="booking__card__info">
            <div class="card__info__first-line">
                <div class="card__info__location" @click="$router.push({ path: `/room/${booking.room.id}/`})">
                    <span>{{ booking.room.hotel.city }}, {{ booking.room.hotel.state }}</span>
                    <h3>{{ booking.room.name }}</h3>
                </div>
                <div v-if="!booking.review" class="card__info__review" @click="emitModalEvent">
                    <ReviewStarIcon :color="'#FEF5D7'" />
                    <ReviewStarIcon :color="'#FEF5D7'" />
                    <ReviewStarIcon :color="'#FEF5D7'" />
                    <ReviewStarIcon :color="'#FEF5D7'" />
                    <ReviewStarIcon :color="'#FEF5D7'" />
                </div>
                <div v-else class="card__info__review" @click="emitModalEvent">
                    <ReviewStarIcon v-for="(num, index) in new Array(booking.review.value)" :key="index + 10" :color="'#FFDD65'" />
                    <ReviewStarIcon v-for="(num, index) in new Array(5 - booking.review.value)" :key="index" :color="'#FEF5D7'" />
                </div>
            </div>
            <div class="card__info__second-line">
                <div class="card__dates">
                    <img src="../../../assets/Booking_dates_icon.svg" alt="Date icon" class='card__dates__icon'>
                    <p>{{ startDate }}</p>
                    <img src="../../../assets/Booking_mini_arrow.svg" alt="Arrow right" class='card__dates__arrow'>
                    <p>{{ endDate }}</p>
                </div>
                <span class="card__total-price">${{ booking.total_price }}</span>
            </div>
        </div>
    </div>
</template>

<script>
import ReviewStarIcon from './ReviewStarIcon.vue';

export default {
    name: 'BookingCard',
    components: {
        ReviewStarIcon
    },
    props: [
        'booking'
    ],
    methods: {
        emitModalEvent() {
            this.$store.dispatch('changeBooking', this.booking);
            this.$emit('modal');
        }
    },
    computed: {
        startDate() {
            //split('T') 2020-01-09T 00:14:26.568900Z => split('-') 2020 01 09 => return 09 01 2020  
            const date = this.booking.start.split('T')[0].split("-");
            return `${date[2]}/${date[1]}/${date[0]}`;
        },
        endDate() {
            const date = this.booking.end.split('T')[0].split("-");
            return `${date[2]}/${date[1]}/${date[0]}`;
        }
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .booking__card {
        box-shadow: 0 0 15px rgba(0,0,0,0.08);

        .booking__card__img {
            background-image: url('../../../assets/Room_card_one.jpg');
            background-size: 100%;
            background-position: center; 
            width: 100%;
            height: 200px;
            transition: 300ms ease-in-out;
            @include small-phone {
                height: 160px;
            }
        }

        .booking__card__info {
            background-color: $primary-color;
            padding: 15px;

            .card__info__first-line {
                display: flex;
                justify-content: space-between;

                .card__info__location {
                    display: flex;
                    flex-direction: column;
                    align-items: flex-start;
                    cursor: pointer;

                    span {
                        text-transform: uppercase;
                        font-size: 0.8125rem;
                        color: $secondary-color-one;
                        font-weight: 300;
                        font-family: $primary-font;
                    }

                    h3 {
                        margin: 0;
                        color: $secondary-color-two;
                        font-weight: 300;
                        font-size: 1.125rem;
                    }
                }

                .card__info__review {
                    display: flex;
                    cursor: pointer;
                    height: 18px;
                    
                    img {
                        width: 18px;
                        height: 18px;
                    }
                }
            }

            .card__info__second-line {
                display: flex;
                justify-content: space-between;
                margin-top: 18px;

                .card__dates {
                    display: flex;
                    justify-content: flex-start;
                    align-items: center;

                    .card__dates__icon {
                        margin-right: 6px;
                    }

                    .card__dates__arrow {
                        margin: 0 8px;
                    }

                    p {
                        margin: 0;
                        margin-top: 2px;
                        color: $gray-text-color;
                        font-size: 0.875rem;
                        font-weight: 300;
                    }
                }

                .card__total-price {
                    color: $secondary-color-two;
                    font-size: 1.125rem;
                    font-weight: 300;
                }
            }
        }
    }

    .booking__card:hover .booking__card__img {
        background-size: 150%;
    }
</style>