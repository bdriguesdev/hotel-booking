<template>
    <article class="hotel__room__card" @click="$router.push({ path: `/room/${room.id}/` })">
        <div class="room__card__img"></div>
        <div class="room__card__information">
            <div class="room__card__text">
                <span>{{ room.hotel.city }}, {{ room.hotel.state }}</span>
                <h3>{{ room.name }}</h3>
            </div>
            <div class="room__card__review">
                <img src="../../assets/Review_star.svg" alt="Review star icon">
                <span>4.5<span>(99+)</span></span>
            </div>
        </div>
    </article>
</template>

<script>
export default {
    name: 'RoomCard',
    props: [
        'room'
    ]
}
</script>

<style lang='scss'>
    @import '../../scss/variables.scss';

    .hotel__room__card {
        margin: 10px;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
        cursor: pointer;

        .room__card__img {
            background-image: url('../../assets/Room_card_one.jpg');
            background-size: 100%;
            background-position: center;
            width: 100%;
            height: 160px;
            transition: 300ms ease-in-out;
        }

        .room__card__information {
            background-color: $primary-color;
            display: flex;
            justify-content: space-between;
            padding: 15px;

            .room__card__text {
                display: flex;
                flex-direction: column;
                justify-content: flex-start;

                span {
                    text-align: left;
                    color: $secondary-color-one;
                    font-weight: 300;
                    font-size: 0.8125rem;
                    text-transform: uppercase;
                }

                h3 {
                    margin: 0;
                    color: $secondary-color-two;
                    font-weight: 300;
                    font-size: 1.125rem;
                }
            }

            .room__card__review {
                display: flex;
                align-items: flex-start;

                img {
                    width: 19px;
                    height: 19px;
                    margin-right: 3px;
                }

                span {
                    margin-top: 2px;
                    font-size: 0.875rem;
                    color: $secondary-color-two;
                    font-weight: 400;

                    span {
                        font-weight: 300;
                    }
                }
            }
        }
    }

    .hotel__room__card:hover .room__card__img {
        background-size: 150%;
        background-position: center;
    }
</style>