<template>
    <div class="error__modal" @mousedown="closeModal">
        <div class="error__modal__content">
            <nav class="error__nav">
                <ul>
                    <li>Error</li>
                </ul>
                <svg v-on:click="closeModal" width="17" height="17" viewBox="0 0 17 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L8.5 8.5M16 16L8.5 8.5M8.5 8.5L16 1L1 16" stroke='white' stroke-width="2"/>
                </svg>
            </nav>
            <div class="error">
                <p class="text">{{ errorMsg }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: 'ErrorModal',
    mounted() {
        const modal = document.querySelector('.error__modal');
        modal.style.height = document.documentElement.scrollHeight + "px";

        const error = document.querySelector('.error__modal__content');
        error.style.marginTop = ((window.innerHeight / 3) - error.getBoundingClientRect().height) + 'px';
    },
    methods: {
        closeModal(evt) {
            if(evt.target.className === 'error__modal') {
                this.$store.dispatch('changeError', null);
            } else if(evt.target.tagName === 'svg' || evt.target.tagName === 'path') {
                this.$store.dispatch('changeError', null);
            }
        },
    },
    computed: {
        ...mapGetters([
            'errorMsg'
        ])
    }
}
</script>

<style lang='scss'>
    @import '../scss/variables.scss';
    @import '../scss/mixins.scss';

    .error__modal {
        top: 0;
        left: 50%;
        width: 100%;
        transform: translateX(-50%);
        position: absolute;
        z-index: 8;
        height: 100vh;
        background-color: rgba(99, 99, 99, 0.5);

        .error__modal__content {
            background-color: $primary-color;
            width: 383px;
            margin: 0 auto;
            margin-top: 10vh;
            @include large-phone {
                width: 350px;
            }
            @include small-phone {
                width: 280px;
            }

            .error__nav {
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
                        font-size: 1.25rem;
                        font-weight: 400;   
                        padding-bottom: 10px; 
                        transition: 250ms ease-in;
                        cursor: pointer;
                        border-bottom: 2px solid $secondary-color-one;
                        color: $secondary-color-one;
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
            
            .error {
                padding: 28px 28px;

                .text {
                    margin: 0;
                    color: $secondary-color-two;
                    font-size: 1.2rem;
                    font-weight: 300;
                }
            }
        }
    }
</style>