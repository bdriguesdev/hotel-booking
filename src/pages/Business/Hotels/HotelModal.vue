<template>
    <div class="hotel__modal" @click="closeModal">
        <div class="hotel__modal__content">
            <nav class="hotel__nav">
                <ul>
                    <li>Hotel</li>
                </ul>
                <svg v-on:click="$emit('modal')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form class="hotel__form" v-on:submit.prevent="handleSubmit">
                <div class="hotel__inputs__container">
                    <label for="secondName">
                        PHOTO
                        <div class="hotel__photo" :style="hotel.photos[0]? { backgroundImage: `url('http://127.0.0.1:8000${hotel.photos[0].photo}')` }: {}">
                            <input @change="changeImg" type="file" id="hotelPhotoInput" style="display:none">
                            <div @click='triggerInputFile' class="hotel__photo__btn">
                                <p>Select</p>
                            </div>
                        </div>
                    </label>
                    <label for="secondName">
                        BOOKINGS SCHEDULE
                        <Calendar />
                    </label>
                    <label for="rooms">
                        Rooms
                        <div class="hotel__rooms__btn" v-on:click="viewHotelRooms" v-on:mouseenter="roomsBtnAnimation">
                            View rooms
                            <div class="hotel__btn__container">
                                <div class="hotel__btn--effect">
                                    <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                                    <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                                </div>
                            </div>
                        </div>
                    </label>
                </div>
                <button class="hotel__modal__btn" v-on:click="hotelBtnAnimation" v-on:mouseenter="hotelBtnAnimation">
                    Save
                    <div class="hotel__modal__btn__container">
                        <div class="hotel__modal__btn--effect">
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                            <img src="../../../assets/Button_arrow_two.svg" alt="Register button icon" />
                        </div>
                    </div>
                </button>
            </form>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Calendar from './Calendar';

export default {
    name: 'HotelModal',
    components: {
        Calendar
    },
    data() {
        return {
            isHotelBtnAnimationInProgress: false,
            isRoomsBtnAnimationInProgress: false,
            file: null
        }
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.hotel__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        handleSubmit() {
            this.hotelBtnAnimation();
            this.$store.dispatch('changeHotelPhoto', { photo: this.file });
        },
        changeImg() {
            const input = document.getElementById('hotelPhotoInput');
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                
                reader.onload = e => {
                    const imgContainer = document.querySelector('.hotel__photo');
                    imgContainer.style.backgroundImage = `url('${e.target.result}')`;
                }
                
                reader.readAsDataURL(input.files[0]);
                this.file = input.files[0];
            }
        },
        triggerInputFile() {
            document.getElementById('hotelPhotoInput').click();
        },
        closeModal(evt) {
            if(evt.target.className === 'hotel__modal') {
                this.$emit('modal');
            }
        },
        hotelBtnAnimation() {
            if(!this.isHotelBtnAnimationInProgress) {
                this.isHotelBtnAnimationInProgress = true;
                const button = document.querySelector('.hotel__modal__btn .hotel__modal__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isHotelBtnAnimationInProgress = false;
                }, 500);
            }
        },
        roomsBtnAnimation() {
            if(!this.isRoomsBtnAnimationInProgress) {
                this.isRoomsBtnAnimationInProgress = true;
                const button = document.querySelector('.hotel__rooms__btn .hotel__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isRoomsBtnAnimationInProgress = false;
                }, 500);
            }
        },
        viewHotelRooms() {
            this.roomsBtnAnimation();
            this.$router.push({ path: '/business/hotel/rooms/' });
        }
    },
    computed: {
        ...mapGetters([
            'hotel'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';

    .hotel__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .hotel__modal__content {
            background-color: $primary-color;
            width: 670px;
            margin: 0 auto;
            margin-top: 10vh;

            .hotel__nav {
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

                svg {
                    position: absolute;
                    right: 12px;
                    top: 12px;  
                    cursor: pointer;

                    path {
                        transition: 200ms ease-in-out;
                    }
                }
                
                svg:hover path {
                    stroke: $secondary-color-one;
                }
            }

            .hotel__form {
                padding-top: 28px;
                padding-bottom: 36px;  
                padding-left: 44px;  
                padding-right: 44px;  

                .hotel__inputs__container {
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
    
                        .hotel__photo {
                            background-image: url('../../../assets/Room_card_one.jpg');
                            background-size: cover;
                            background-position: center;
                            width: 275px;
                            height: 270px;
                            box-shadow: 0 0 10px rgba(0,0,0,0.08);
                            position: relative;

                            .hotel__photo__btn {
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

                            .hotel__photo__btn::after {
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

                .hotel__rooms__btn {
                    font-family: $primary-font;
                    background-color: $secondary-color-two;
                    text-transform: none;
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
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.20);
                    cursor: pointer;

                    .hotel__btn__container {
                        overflow: hidden;
                        width: 21px;
                        margin-left: 10px;

                        .hotel__btn--effect {
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

                .hotel__rooms__btn::after {
                    content: 'View rooms';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 22px;
                    color: $shadow-color;
                }
            }

            .hotel__modal__btn {
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

                .hotel__modal__btn__container {
                    overflow: hidden;
                    width: 21px;
                    margin-left: 10px;

                    .hotel__modal__btn--effect {
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

            .hotel__modal__btn::after {
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
</style>