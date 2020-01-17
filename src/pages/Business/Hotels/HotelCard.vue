<template>
    <div class="hotel__card" @click="$emit('modal', hotel)">
        <div class="hotel__card__img" :style="hotel.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${hotel.photos[0].photo}')` }: {}"></div>
        <div class="hotel__card__info">
            <div class="hotel__info__first-line">
                <div class="hotel__info__location">
                    <span>{{ hotel.city }}, {{ hotel.state }}</span>
                    <h3>{{ hotel.name }}</h3>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HotelCard',
    props: [
        'hotel'
    ],
    mounted() {
        // eslint-disable-next-line
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .hotel__card {
        box-shadow: 0 0 15px rgba(0,0,0,0.08);
        cursor: pointer;

        .hotel__card__img {
            background-image: url('../../../assets/Room_card_one.jpg');
            background-size: 100%;
            background-color: gray;
            background-position: center; 
            width: 100%;
            height: 200px;
            transition: 300ms ease-in-out;
            @include small-phone {
                height: 160px;
            }
        }

        .hotel__card__info {
            background-color: $primary-color;
            padding: 15px;

            .hotel__info__first-line {
                display: flex;
                justify-content: space-between;

                .hotel__info__location {
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
            }
        }
    }

    .hotel__card:hover .hotel__card__img {
        background-size: 150%;
        background-position: center;
    }
</style>