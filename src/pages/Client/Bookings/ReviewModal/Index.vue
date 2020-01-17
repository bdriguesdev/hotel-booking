<template>
    <div class="booking__review__modal" @click="closeModal">
        <div class="booking__review__modal__content">
            <nav class="booking__review__nav">
                <ul>
                    <li>{{ booking.review? "Review": "Create" }}</li>
                </ul>
                <svg v-on:click="$emit('modal')" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <CreateReview v-if="!booking.review" />
            <ViewReview v-if="booking.review" />
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import CreateReview from './CreateReview';
import ViewReview from './ViewReview';

export default {
    name: 'ReviewModal',
    components: {
        CreateReview,
        ViewReview
    },
    data() {
        return {
        }
    },
    created() {
    },
    mounted() {
        /* eslint-disable no-console */
        const modal = document.querySelector('.booking__review__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";
    },
    methods: {
        closeModal(evt) {
            if(evt.target.className === 'booking__review__modal') {
                this.$emit('modal');
            }
        }
    },
    computed: {
        ...mapGetters([
            'booking'
        ]),
    }
}
</script>

<style lang='scss'>
    @import '../../../../scss/variables.scss';
    @import '../../../../scss/mixins.scss';

    .booking__review__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 5;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .booking__review__modal__content {
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

            .booking__review__nav {
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
        }
    }
</style>