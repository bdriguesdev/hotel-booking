<template>
    <div class="search__container">
        <Header v-on="$listeners" />
        <main v-if="searchType !== null && searchLoading === false" class='search__content'>
            <div class="search__title">
                <span class="search__number--container">
                    <div class="search__number--border"></div>
                    <span class="search__number">{{ searchAmount }}</span>
                </span>
                <div class="search__text">
                    <h2><span>{{ searchTypeTransformized }}(s)</span> were found:</h2>
                    <div class="search__line"></div>
                </div>
            </div>
            <div v-if="searchType === 'room'" class="search__results">
                <RoomSlide v-for="(room, index) in roomSearch" :key="index" :room="room" />
            </div>
            <div v-else-if="searchType === 'hotel'" class="search__results">
                <HotelSlide v-for="(hotel, index) in hotelSearch" :key="index" :hotel="hotel" />
            </div>
            <div class="search__pagination">
                <!-- ??? -->
            </div>
        </main>
        <div v-else class="lds-ellipsis" :style="{marginTop: '40vh'}"><div></div><div></div><div></div><div></div></div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Header from '../../components/Header';
import RoomSlide from './RoomSlide';
import HotelSlide from './HotelSlide';

export default {
    name: 'Search',
    data() {
        return {
            isSectionTitleAnimated: false,
            sectionWidth: null
        }
    },
    components: {
        Header,
        RoomSlide,
        HotelSlide
    },
    mounted() {
        //title animation
        setTimeout(()=> { this.titleAnimation(); }, 1);
        const section = document.querySelector('.search__container');
        this.cardSlidePosition(section.getBoundingClientRect().width);
        window.addEventListener('resize', this.changeSectionWidth);
    },
    updated() {
        const section = document.querySelector('.search__container');
        this.cardSlidePosition(section.getBoundingClientRect().width);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.changeSectionWidth);
    },
    methods: {
        changeSectionWidth() {
            const section = document.querySelector('.search__container');
            this.sectionWidth = section.getBoundingClientRect().width;
        },
        titleAnimation() {
            this.isSectionTitleAnimated = true;

            const titleNumberContainer = document.querySelector('.search__number--container');
            const titleNumber = document.querySelector('.search__number');
            titleNumberContainer.style.width = titleNumberContainer.getBoundingClientRect().width * titleNumber.innerHTML.length + 'px';
            titleNumber.style.top = '-42px';

            const titleNumberBorder = document.querySelector('.search__number--border');
            titleNumberBorder.style.width = '100%';

            const titleTextBorder = document.querySelector('.search__line');
            const titleNumberBorderWidth = titleTextBorder.getBoundingClientRect().width;
            const titleNumberBorderMinWidth = titleTextBorder.style.minWidth;
            titleTextBorder.style.width = '0px';
            titleTextBorder.style.minWidth = '0%';
            titleTextBorder.style.visibility = 'visible';
            titleTextBorder.getBoundingClientRect();
            titleTextBorder.style.transition = '800ms ease-in-out';
            titleTextBorder.style.width = titleNumberBorderWidth + 'px';
            titleTextBorder.style.minWidth = titleNumberBorderMinWidth + 'px';
        },
        cardSlidePosition(newValue) {
            let slideContainers;
            let slideImg;
            if(this.searchType === 'room') {
                slideContainers = document.querySelectorAll('.room__search__slide .search__slide__imgs');
                slideImg = document.querySelector('.room__search__slide .search__slide__imgs img');
            } else if(this.searchType === 'hotel') {
                slideContainers = document.querySelectorAll('.hotel__search__slide .search__slide__imgs');
                slideImg = document.querySelector('.hotel__search__slide .search__slide__imgs img');
            }

            let leftValue = (newValue - slideContainers[0].getBoundingClientRect().width ) / 2;
            if(this.card === 1) {
                leftValue += slideImg.offsetLeft * 2 + slideImg.getBoundingClientRect().width;
            } else if(this.card === 3) {
                leftValue += slideImg.offsetLeft * 2 + slideImg.getBoundingClientRect().width;
            }
            for(let x = 0; x < slideContainers.length; x++) {
                slideContainers[x].style.left = leftValue + 'px';
            }
        }
    },
    computed: {
        ...mapGetters([
            'searchLoading',
            'roomSearch',
            'hotelSearch',
            'searchType',
            'searchAmount'
        ]),
        searchTypeTransformized() {
            let text = this.searchType.split('');
            text[0] = text[0].toUpperCase();
            return text.join("");
        }
    },
    watch: {
        sectionWidth(newValue) {
            this.cardSlidePosition(newValue);
        }
    }
}
</script>

<style lang="scss">
    @import '../../scss/variables.scss';
    @import '../../scss/mixins.scss';

    .search__content {
        max-width: 2000px;
        width: 100%;
        margin: 0 auto;
        margin-top: 100px;
        position: relative;
        overflow: hidden;
        padding-bottom: 10px;

        .search__title {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 61px;
            margin-left: 5%;
            @include small-phone {
                flex-direction: column;
            }

            .search__number--container {
                width: 87px;
                height: 87px;
                background-color: $secondary-color-two;
                overflow: hidden;
                position: relative;

                .search__number--border {
                    background-color: $secondary-color-one;
                    height: 3px;
                    width: 0;
                    transition: 800ms ease-in-out;
                    transition-delay: 600ms;
                }

                .search__number {
                    font-size: 9.375rem;
                    color: $primary-color;
                    font-weight: 700;
                    position: absolute;
                    left: -13px;
                    top: -150px;
                    position: blue;
                    transition: 800ms ease-in-out;
                }
            }

            .search__text {
                display: flex;
                flex-direction: column;
                justify-content: flex-end;
                
                h2 {
                    margin: 0;
                    color: $secondary-color-two;
                    text-align: left;
                    margin-left: 10px;
                    font-size: 1.875rem;
                    font-weight: 400;
                    @include large-phone {
                        font-size: 1.7rem;
                    }

                    span {
                        color: $secondary-color-two;
                        font-size: 1.875rem;
                        font-weight: 300;
                        font-family: $secondary-font;
                        @include large-phone {
                            font-size: 1.7rem;
                        }
                    }
                }

                .search__line {
                    min-width: 80%;
                    visibility: hidden;
                    width: 267px;
                    max-width: 95%;
                    height: 3px;
                    background-color: $secondary-color-two;
                }
            }
        }
    }

</style>