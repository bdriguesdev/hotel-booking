<template>
    <div class="search__modal" @click="closeModal">
        <div class="search__modal__content">
            <nav class="search__nav">
                <ul>
                    <li v-on:click="changeOption('rooms')" >Rooms</li>
                    <li v-on:click="changeOption('hotels')" >Hotels</li>
                </ul>
                <svg v-on:click="$emit('modal', 'search')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <Rooms v-on="$listeners" v-if="roomsActive" />
            <Hotels v-on="$listeners" v-else />
        </div>
    </div>
</template>

<script>
import Rooms from './Rooms';
import Hotels from './Hotels';

export default {
    //need to use the nav to select between client/business
    name: 'SearchModal',
    components: {
        Rooms,
        Hotels
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.search__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    data() {
        return {
            roomsActive: true,
            hotelsActive: false,
            firstName: null,
            lastName: null,
            email: null,
            birthday: null,
            password: null,
            repeatedPassword: null
        }
    },
    methods: {
        changeOption(option) {
            const options = document.querySelectorAll('.search__nav ul li');

            if(option === 'rooms') {
                this.roomsActive = true;
                this.hotelsActive = false;
                options[1].style.color = '#FFFFFF';
                options[1].style.borderColor = '#000000';
                options[0].style.color = '#FF1E1E';
                options[0].style.borderColor = '#FF1E1E';
            } else {
                this.roomsActive = false;
                this.hotelsActive = true;
                options[0].style.color = '#FFFFFF';
                options[0].style.borderColor = '#000000';
                options[1].style.color = '#FF1E1E';
                options[1].style.borderColor = '#FF1E1E';
            }
        },
        closeModal(evt) {
            if(evt.target.className === 'search__modal') {
                this.$emit('modal', 'search');
            }
        }
    }
}
</script>

<style lang='scss'>
    @import '../../scss/variables.scss';
    @import '../../scss/mixins.scss';

    .search__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .search__modal__content {
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

            .search__nav {
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
                        color: $primary-color;
                        font-size: 1.25rem;
                        font-weight: 400;   
                        padding-bottom: 10px; 
                        border-bottom: 2px solid $secondary-color-two;
                        transition: 250ms ease-in;
                        cursor: pointer;
                    }

                    li:nth-child(1) {
                        margin-right: 10px;
                        border-bottom: 2px solid $secondary-color-one;
                        color: $secondary-color-one;
                    }

                    li:nth-child(2) {
                        margin-left: 10px;
                    }

                    li:hover {
                        border-color: $primary-color;
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
        }
    }
</style>