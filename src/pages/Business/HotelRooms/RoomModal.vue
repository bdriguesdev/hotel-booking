<template>
    <div class="room__modal" @click="closeModal">
        <div class="room__modal__content">
            <nav class="room__nav">
                <svg v-if="bookingInformationOpen" @click="handleModal" class='arrow__back' width="24" height="16" viewBox="0 0 24 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M23.7071 8.70711C24.0976 8.31658 24.0976 7.68342 23.7071 7.29289L17.3431 0.928932C16.9526 0.538408 16.3195 0.538408 15.9289 0.928932C15.5384 1.31946 15.5384 1.95262 15.9289 2.34315L21.5858 8L15.9289 13.6569C15.5384 14.0474 15.5384 14.6805 15.9289 15.0711C16.3195 15.4616 16.9526 15.4616 17.3431 15.0711L23.7071 8.70711ZM0 9H23V7H0V9Z" fill="white"/>
                </svg>
                <ul>
                    <li>Room</li>
                </ul>
                <svg class="close__modal" v-on:click="$emit('modal')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form class="room__form" v-on:submit.prevent="handleSubmit" :style="roomInformationOpen? {}: { display: 'none' }">
                <div class="room__inputs__container">
                    <label for="secondName">
                        PHOTOS
                        <div class="room__photo" :style="room.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${room.photos[0].photo}')` }: {}">
                            <input @change="changeImg   " type="file" id="roomPhotoInput" style="display:none">
                            <div @click='triggerInputFile' class="room__photo__btn">
                                <p>Select</p>
                            </div>
                        </div>
                    </label>
                    <label for="secondName">
                        BOOKINGS SCHEDULE
                        <Calendar @modal="handleModal" />
                    </label>
                </div>
                <button class="room__modal__btn" v-on:click="roomBtnAnimation" v-on:mouseenter="roomBtnAnimation">
                    Save
                    <div class="room__modal__btn__container">
                        <div class="room__modal__btn--effect">
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                        </div>
                    </div>
                </button>
            </form>
            <div v-if="bookingInformationOpen" class="booking__information">
                <div class="booking__information__first-part">
                    <div class="booking__information__avatar" :style="booking.client.photo? { backgroundImage: `url('http://127.0.0.1:8000${booking.client.photo}')` }: {}" ></div>
                    <div class="booking__information__info">
                        <h3 class="booking__information__user">{{ booking.client.first_name }} {{ booking.client.last_name }}</h3>
                        <span class="booking__information__date">{{ formatDate(booking.start) }} - {{ formatDate(booking.end) }}</span>
                        <span class="booking__information__price">$ {{ booking.total_price }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Calendar from './Calendar';

export default {
    name: 'RoomModal',
    components: {
        Calendar
    },
    data() {
        return {
            isRoomBtnAnimationInProgress: false,
            file: null,
            roomInformationOpen: true,
            bookingInformationOpen: false
        }
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.room__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        handleModal() {
            this.roomInformationOpen = !this.roomInformationOpen;
            this.bookingInformationOpen = !this.bookingInformationOpen;
        },
        formatDate(date) {
            date = date.split('T')[0].split("-");
            return `${date[2]}/${date[1]}/${date[0]}`;
        },
        handleSubmit() {
            this.roomBtnAnimation();
            this.$store.dispatch('changeRoomPhoto', { photo: this.file });
        },
        changeImg() {
            const input = document.getElementById('roomPhotoInput');
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                
                reader.onload = e => {
                    const imgContainer = document.querySelector('.room__photo');
                    imgContainer.style.backgroundImage = `url('${e.target.result}')`;
                }
                
                reader.readAsDataURL(input.files[0]);
                this.file = input.files[0];
            }
        },
        triggerInputFile() {
            document.getElementById('roomPhotoInput').click();
        },
        closeModal(evt) {
            if(evt.target.className === 'room__modal') {
                this.$emit('modal');
            }
        },
        roomBtnAnimation() {
            if(!this.isRoomBtnAnimationInProgress) {
                this.isRoomBtnAnimationInProgress = true;
                const button = document.querySelector('.room__modal__btn .room__modal__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isRoomBtnAnimationInProgress = false;
                }, 500);
            }
        }
    },
    computed: {
        ...mapGetters([
            'room',
            'booking'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';

    .room__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .room__modal__content {
            background-color: $primary-color;
            width: 670px;
            margin: 0 auto;
            margin-top: 10vh;

            .room__nav {
                background-color: $secondary-color-two;
                display: flex;
                justify-content: center;
                position: relative;

                ul {
                    list-style: none;
                    margin: 0;
                    display: flex;
                    padding: 0;
                    padding-top: 20px;

                    li {
                        color: $secondary-color-one;
                        font-size: 1.25rem;
                        font-weight: 400;   
                        padding-bottom: 10px; 
                        border-bottom: 2px solid $secondary-color-one;
                        transition: 250ms ease-in;
                        cursor: pointer;
                    }
                }

                .close__modal {
                    position: absolute;
                    right: 12px;
                    top: 12px;  
                    cursor: pointer;

                    path {
                        transition: 200ms ease-in-out;
                    }
                }
                
                .close__modal:hover path {
                    stroke: $secondary-color-one;
                }

                .arrow__back {
                    position: absolute;
                    left: 12px;
                    top: 12px;
                    transform: rotate(180deg);
                    cursor: pointer;

                    path {
                        transition: 200ms ease-in-out;
                    }
                }

                .arrow__back:hover path {
                    fill: $secondary-color-one;
                }
            }

            .room__form {
                padding-top: 28px;
                padding-bottom: 36px;  
                padding-left: 44px;  
                padding-right: 44px;  

                .room__inputs__container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    
                    label {
                        font-family: $secondary-font;
                        color: $secondary-color-two;
                        font-size: 1rem;
                        text-transform: uppercase;
                        text-align: left;
                        margin: 8px 0px;
                        display: flex;
                        flex-direction: column;
                        align-items: flex-start;
                        justify-content: flex-start;
                        width: 275px;
                        
                        input {
                            background-color: $input-bg-color;
                            border: none;
                            width: 263px;
                            padding-left: 12px;
                            height: 42px;
                            border-bottom: 2px solid $secondary-color-two;
                            outline: none;
                            font-size: 1rem;
                            color: $input-text-color;
                            box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                            border-radius: 0;
                        }
    
                        .room__photo {
                            background-image: url('../../../assets/Room_card_one.jpg');
                            background-size: cover;
                            background-position: center;
                            width: 275px;
                            height: 270px;
                            box-shadow: 0 0 10px rgba(0,0,0,0.08);
                            position: relative;

                            .room__photo__btn {
                                text-transform: none;
                                text-align: center;
                                position: absolute;
                                bottom: 0;
                                right: 50%;
                                transform: translateX(50%);
                                background-color: $secondary-color-one;
                                border: none;
                                color: $primary-color;
                                width: 127px;
                                height: 44px;
                                cursor: pointer;
                                z-index: 2;
                                outline: 0;
                                
                                p {
                                    text-align: center;
                                    font-family: $primary-font;
                                    font-size: 1.063rem;
                                    font-weight: 700;
                                    margin: 0;
                                    position: relative;
                                    top: 50%;
                                    transform: translateY(-50%);
                                }
                            }

                            .room__photo__btn::after {
                                content: 'Select';
                                text-align: center;
                                font-family: $primary-font;
                                font-size: 1.063rem;
                                font-weight: 700;
                                margin: 0;
                                position: absolute;
                                z-index: -1;
                                font-size: 1.063rem;
                                top: 13px;
                                left: 38px;
                                color: $shadow-color;
                            }
                        }

                    }
                }

                 .room__modal__btn {
                    font-family: $primary-font;
                    background-color: $secondary-color-one;
                    border: none;
                    color: $primary-color;
                    width: 127px;
                    height: 44px;
                    font-size: 1.063rem;
                    font-weight: 700;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    position: relative;
                    z-index: 1;
                    margin: 0 auto;
                    margin-top: 28px;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.20);
                    cursor: pointer;

                    .room__modal__btn__container {
                        overflow: hidden;
                        width: 21px;
                        margin-left: 10px;

                        .room__modal__btn--effect {
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

                .room__modal__btn::after {
                    content: 'Save';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 28px;
                    color: $shadow-color;
                }
            }
        }

        .booking__information {
            padding-top: 28px;
            padding-bottom: 36px;  
            padding-left: 44px;  
            padding-right: 44px;  

            .booking__information__first-part {
                display: flex;
                justify-content: flex-start;

                .booking__information__avatar {
                    background-image: url('../../../assets/Room_review_avatar.jpg');
                    background-size: cover;
                    background-position: center;
                    width: 80px;
                    height: 80px;
                }

                .booking__information__info {
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

                    .booking__information__price {
                        margin-top: 5px;
                        font-weight: 300;
                        color: $secondary-color-two;
                    }
                }
            }
        }   
    }
</style>