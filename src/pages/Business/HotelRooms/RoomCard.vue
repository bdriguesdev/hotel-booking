<template>
    <div class="room__card" @click="openRoomModal">
        <div class="room__card__img" :style="room.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${room.photos[0].photo}')` }: {}"></div>
        <div class="room__card__info">
            <div class="room__info__first-line">
                <div class="room__info__location">
                    <span>{{ room.hotel.city }}, {{ room.hotel.state }}</span>
                    <h3>{{ room.name }}</h3>
                </div>
                <div class="room__reviews">
                    <img src='../../../assets/Review_star.svg' alt="Review star">
                    <p>{{ room.reviews_average }}<span>({{ room.reviews_count }})</span></p>
                </div>
            </div>
            <div class="room__info__second-line">
                <span>${{ room.price }}</span>
            </div>
        </div>
    </div>
</template>

<script>
// import { mapGetters } from 'vuex';

export default {
    name: 'RoomCard',
    props: [
        'room'
    ],
    methods: {
        openRoomModal() {
            this.$emit('modal');
            this.$store.dispatch('changeRoom', this.room);
        }
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .room__card {
        box-shadow: 0 0 15px rgba(0,0,0,0.08);
        cursor: pointer;

        .room__card__img {
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

        .room__card__info {
            background-color: $primary-color;
            padding: 15px;

            .room__info__first-line {
                display: flex;
                justify-content: space-between;

                .room__info__location {
                    display: flex;
                    flex-direction: column;
                    align-items: flex-start;

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

                .room__reviews {
                    display: flex;
                    align-items: flex-start;

                    p {
                        margin: 0;
                        margin-top: 4px;
                        margin-left: 5px;
                        color: $secondary-color-two;
                        font-size: 0.9375rem;
                        font-weight: 400;

                        span {
                            color: $secondary-color-two;
                            font-size: 0.9375rem;
                            font-weight: 300;
                        }
                    }
                }
            }

            .room__info__second-line {
                display: flex;
                justify-content: flex-end;

                span {
                    color: $secondary-color-two;
                    font-size: 1.125rem;
                    font-weight: 300;
                }
            }
        }
    }

    .room__card:hover .room__card__img {
        background-size: 150%;
        background-position: center;
    }
</style>