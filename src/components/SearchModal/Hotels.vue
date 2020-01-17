<template>
    <form class="search__form" @submit.prevent="handleSearch">
        <div class="search__inputs__container">
            <label for="name">
                Hotel name
                <input type="text" v-model="name"/>
            </label>
            <label for="city">
                City
                <input type="text" v-model="city"/>
            </label>
            <label for="state">
                State
                <input type="text" v-model="state"/>
            </label>
        </div>
        <button class="search__btn" v-on:click="btnAnimation" v-on:mouseenter="btnAnimation">
            Search now
            <div class="search__btn__container">
                <div class="search__btn--effect">
                    <img src="../../assets/Button_arrow_two.svg" alt="Register button icon" />
                    <img src="../../assets/Button_arrow_two.svg" alt="Register button icon" />
                </div>
            </div>
        </button>
    </form>
</template>

<script>
export default {
    name: 'Hotels',
    data() {
        return {
            name: '',
            state: '',
            city: ''
        }
    },
    methods: {
        handleSearch() {
            const args = {
                name: this.name,
                state: this.state,
                city: this.city
            };
            this.$store.dispatch('searchHotels', args).then(() => {
                const path = '/search/';
                if(this.$route.path !== path) this.$router.push({ path });
                this.$emit('modal', 'search');
            });
        },
        btnAnimation() {
            if(!this.isBtnAnimationInProgress) {
                this.isBtnAnimationInProgress = true;
                const button = document.querySelector('.search__btn--effect');
                button.style.animation = 'hover-animation 500ms ease-in-out 1';
                setTimeout(() => {
                    button.style.animation = '';
                    this.isBtnAnimationInProgress = false;
                }, 500);
            }
        }
    }
}
</script>

<style lang="scss">
    @import '../../scss/variables.scss';

    .search__form {
        padding-top: 28px;
        padding-bottom: 36px;    
        display: flex;
        flex-wrap: wrap;
        justify-content: center;

        .search__inputs__container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;

            label {
                font-family: $secondary-font;
                color: $secondary-color-two;
                font-size: 1rem;
                text-transform: uppercase;
                display: block;
                text-align: left;
                width: 261px;
                margin: 8px 15px;

                input {
                    background-color: $input-bg-color;
                    border: none;
                    width: 249px;
                    padding-left: 12px;
                    height: 42px;
                    border-bottom: 2px solid $secondary-color-two;
                    outline: none;
                    font-size: 1rem;
                    color: $input-text-color;
                    box-shadow: inset 0px 0px 10px rgba(0,0,0,0.05);
                    border-radius: 0;
                }

                input[type=date] {
                    height: 44px;
                }

                .search__input--range {
                    width: 261px;
                    height: 46px;
                    position: relative;

                    .input__search--line {
                        position: relative;
                        width: 100%;
                        height: 2px;
                        background-color: $input-bg-color;
                        top: 50%;
                        transform: translateY(-50%);
                    }

                    .input__search--line::after {
                        position: absolute;
                        bottom: -7px;
                        left: 0;
                        content: '';
                        width: 2px;
                        height: 16px;
                        background-color: $light-gray-text-color;
                    }

                    .input__search--line::before {
                        position: absolute;
                        bottom: -7px;
                        right: 0;
                        content: '';
                        width: 2px;
                        height: 16px;
                        background-color: $light-gray-text-color;
                    }

                    .input__search--min {
                        position: absolute;
                        top: 50%;
                        transform: translateY(-50%);
                        right: 0;
                        background-color: $secondary-color-one;
                        width: 14px;
                        height: 14px;
                        border-radius: 7px;
                        box-shadow: 0 0 5px rgba(0,0,0,0.15);
                        cursor: pointer !important;
                    }

                    .input__search--max {
                        position: absolute;
                        top: 50%;
                        transform: translateY(-50%);
                        left: 0;
                        background-color: $secondary-color-one;
                        width: 14px;
                        height: 14px;
                        border-radius: 7px;
                        box-shadow: 0 0 5px rgba(0,0,0,0.15);
                        cursor: pointer !important;
                    }
                }
            }

            label:nth-child(3) {
                justify-self: flex-start;
                margin-right: auto;
            }
        }
        .search__btn {
            font-family: $primary-font;
            background-color: $secondary-color-one;
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
            margin-top: 28px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.20);
            cursor: pointer;

            .search__btn__container {
                overflow: hidden;
                width: 21px;
                margin-left: 10px;

                .search__btn--effect {
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

        .search__btn::after {
            content: 'Search now';
            position: absolute;
            z-index: -1;
            font-size: 1.063rem;
            top: 13px;
            left: 22px;
            color: $shadow-color;
        }
    }
        
</style>