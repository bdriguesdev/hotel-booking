<template>
    <div class="client__profile__modal" @mousedown="closeModal">
        <div class="client__profile__modal__content">
            <nav class="client__profile__nav">
                <ul>
                    <li>Settings</li>
                </ul>
                <svg v-on:click="$emit('modal', 'profile')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <form enctype="multipart/form-data" class="client__profile__form" v-on:submit.prevent="handleSubmit">
                <div class="client__inputs__container">
                    <label class='client__input__start' for='Start date'>
                        Avatar
                        <div class="client__avatar" :style="user.photo? { backgroundImage: `url('http://127.0.0.1:8000${user.photo}')` }: {}">
                            <input @change="changeImg" type="file" id="clientProfileAvatar" style="display:none;" >
                            <div @click="triggerFileInput" class='client__avatar__btn'>
                                <p>Select</p> 
                            </div>
                        </div>
                        
                    </label>
                </div>
                <button class="client__profile__btn" v-on:click="btnAnimation" v-on:mouseenter="btnAnimation">
                    Save
                    <div class="client__btn__container">
                        <div class="client__btn--effect">
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

export default {
    name: 'ClientProfileModal',
    components: {
    },
    data() {
        return {
            isBtnAnimationInProgress: false,
            file: null
        }
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.client__profile__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        handleSubmit() {
            const args = {
                photo: this.file
            };
            this.$store.dispatch('changeProfilePhoto', args);
        },
        changeImg() {
            const input = document.getElementById('clientProfileAvatar');
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                
                reader.onload = e => {
                    const imgContainer = document.querySelector('.client__avatar');
                    imgContainer.style.backgroundImage = `url('${e.target.result}')`;
                }
                
                reader.readAsDataURL(input.files[0]);
                this.file = input.files[0];
            }
        },
        triggerFileInput() {
            document.getElementById('clientProfileAvatar').click();
        },
        closeModal(evt) {
            if(evt.target.className === 'client__profile__modal') {
                this.$emit('modal', 'profile');
            }
        },
        btnAnimation() {
            if(!this.isBtnAnimationInProgress) {
                this.isBtnAnimationInProgress = true;
                const button = document.querySelector('.client__profile__btn .client__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isBtnAnimationInProgress = false;
                }, 500);
            }
        }
    },
    computed: {
        ...mapGetters([
            'user'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../../../scss/variables.scss';
    @import '../../../scss/mixins.scss';

    .client__profile__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .client__profile__modal__content {
            background-color: $primary-color;
            width: 670px;
            margin: 0 auto;
            margin-top: 10vh;
            @include large-phone {
                width: 350px;
            }
            @include small-phone {
                width: 280px;
            }

            .client__profile__nav {
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

            .client__profile__form {
                padding-top: 28px;
                padding-bottom: 36px;  
                padding-left: 44px;  
                padding-right: 44px;  

                .client__inputs__container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    
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

                        .client__avatar {
                            background-image: url('../../../assets/Room_review_avatar.jpg');
                            background-size: cover;
                            background-position: center;
                            width: 250px;
                            height: 250px;
                            position: relative;
                            @include small-phone {
                                width: 200px;
                            }

                            .client__avatar__btn {
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

                            .client__avatar__btn::after {
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
                                @include desktop {
                                    left: 41px;
                                }
                            }
                        }
                    }

                    .input__date__container {
                        margin-bottom: 20px;
                        display: block;
                        width: 114px;
                        height: 44px;
                        background-color: $secondary-color-two;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                        font-family: $primary-font;
                        color: $primary-color;
                        font-weight: 500;
                        font-size: 1.063rem;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                }

                .client__profile__btn {
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

                    .client__btn__container {
                        overflow: hidden;
                        width: 21px;
                        margin-left: 10px;

                        .client__btn--effect {
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

                .client__profile__btn::after {
                    content: 'Save';
                    position: absolute;
                    z-index: -1;
                    font-size: 1.063rem;
                    top: 13px;
                    left: 28px;
                    color: $shadow-color;
                    @include desktop {
                        left: 30px;
                    }
                }
            }
        }
    }
</style>